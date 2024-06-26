import accounts.views
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Min, Max, F, Case, When, IntegerField,Count
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import JsonResponse, Http404, HttpResponseNotFound, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from urllib.parse import urlencode
from datetime import datetime, timedelta
from jdatetime import date as jalali_date, timedelta as jalali_timedelta
from .models import City, Hotel, Room, Request, Passenger, Facility, ReservasionNumber,SeasonPrice
from .forms import BookingForm, BookingModelForm, ReceiptForm
from .serializer import HotelSerializer, HotelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random, string, time, requests, json
from django.conf import settings


ZP_API_REQUEST = f"https://zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = ''  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/verify'


def PaymentView(request, reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    cardnumber = '6104337840187817'
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('paycheck', kwargs={'reserve': reserve}))
    else:
        form = ReceiptForm()
    room = my_reserve.room
    city = room.hotel.city
    enter = datetime.strptime(my_reserve.enter, '%Y/%m/%d').date()
    exit = datetime.strptime(my_reserve.exit, '%Y/%m/%d').date()
    night = (exit - enter).days

    high_date = SeasonPrice.objects.get(season_status='H', city=city)
    low_date = SeasonPrice.objects.get(season_status='L', city=city)
    format_price = {}

    if my_reserve.enter <= high_date.end_date and my_reserve.exit >= high_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.high_price * night)
    elif my_reserve.enter <= low_date.end_date and my_reserve.exit >= low_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.low_price * night)
    else:
        format_price[room] = '{:,.0f}'.format(room.price * night)
    context = {
        'cardnumber': cardnumber,
        'reserve': my_reserve,
        'format_price':format_price,
        'room': room,
        'form': form
    }
    return render(request, 'hotels/payment.html', context=context)


def PayCheckView(request, reserve):

    context = {
        'reserve': reserve
    }
    return render(request, 'hotels/paycheck.html', context)


def send_request(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']),
                        'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(authority):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data

    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    response = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response


def BankPaymentEndPoint(request, reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    my_reserve.reserve_status = 'D'
    my_reserve.save()
    return render(request, 'hotels/hotel-home.html')


def CheckReservationStatusEndPoint(request, reserve_confirm):
    try:
        reserve_code_status = Request.objects.get(reserve_code=reserve_confirm)
        data = {
            'confirm': reserve_code_status.confirm,
            'reserve_status': reserve_code_status.reserve_status
        }
    except Request.DoesNotExist:
        data = {'confirm': 'W',
                'reserve_status': 'P'}

    return JsonResponse(data)


def GenerateRandomStringEndPoint(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def HotelLikeEndPoint(request, pk):
    if request.user.is_authenticated:
        hotel = Hotel.objects.get(pk=pk)
        if request.method == "POST":
            data = request.POST
            request.user.increase_likes(hotel)
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)
        else:
            return redirect(home)
    return redirect(accounts.views.LoginView)

    return Response({'error': 'متد نامعتبر.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def HotelHomeView(request):
    current_date = jalali_date.today()
    exit_date = current_date + jalali_timedelta(days=4)
    formatted_exit_date = exit_date.strftime('%Y/%m/%d')
    formatted_current_date = current_date.strftime('%Y/%m/%d')
    cities = City.objects.all()
    hotels = Hotel.objects.all()
    suggest_hotels = Hotel.objects.filter(boroobia_suggest=True).all()
    online_reserves_hotels = Hotel.objects.filter(online_reserve=True).all()
    online_reserves_hotels_city = set()
    for o_hotel in online_reserves_hotels:
        online_reserves_hotels_city.add(o_hotel.city)
    facilities = Facility.objects.all()
    kish_count = City.objects.get(faname='کیش').hotel_set.count()
    mashhad_count = City.objects.get(faname='مشهد').hotel_set.count()
    tehran_count = City.objects.get(faname='تهران').hotel_set.count()
    isfahan_count = City.objects.get(faname='اصفهان').hotel_set.count()
    shiraz_count = City.objects.get(faname='شیراز').hotel_set.count()
    tabriz_count = City.objects.get(faname='تبریز').hotel_set.count()
    like_order_hotels = hotels.order_by('-likes')[:4]
    content = {'cities': cities,
               'hotels': hotels,
               'suggest_hotels': suggest_hotels,
               'online_reserves_hotels': online_reserves_hotels,
               'online_reserves_hotels_city': online_reserves_hotels_city,
               'like_order_hotels':like_order_hotels,
               'facilities': facilities,
               'kish_count': kish_count,
               'mashhad_count': mashhad_count,
               'tehran_count': tehran_count,
               'tabriz_count': tabriz_count,
               'shiraz_count': shiraz_count,
               'isfahan_count': isfahan_count,
               'formatted_current_date': formatted_current_date,
               'formatted_exit_date': formatted_exit_date, }

    return render(request, 'hotels/hotel-home.html', content)


def HotelListView(request, city_slug):
    city = get_object_or_404(City, slug=city_slug)
    cities = City.objects.all()
    hotels = Hotel.objects.filter(city=city.id)
    hotels_count = hotels.count()
    rooms = Room.objects.filter(hotel__in=hotels)
    requests = Request.objects.all()
    # دریافت نوع مرتب سازی از پارامتر درخواست کاربر
    sort_type = request.GET.get('sort_select')

    if sort_type == 'suggest':
        # ابتدا برای هتل‌هایی که فیلد boroobia_suggest برابر با True است یک اولویت اعطا می‌کنیم.
        hotels = hotels.annotate(
            suggest_priority=Case(
                When(boroobia_suggest=True, then=1),
                default=2,
                output_field=IntegerField()
            )
        )

        # سپس داده‌ها را بر اساس اولویت و سپس min_price مرتب می‌کنیم.
        hotels = hotels.order_by('suggest_priority')
    elif sort_type == 'cheapest':
        # مرتب سازی بر اساس قیمت کمترین به بیشترین
        hotels = hotels.annotate(min_price=Min('room'))
        hotels = hotels.order_by('min_price')
    elif sort_type == 'expensive':
        # مرتب سازی بر اساس قیمت بیشترین به کمترین
        hotels = hotels.annotate(max_price=Max('room__price'))
        hotels = hotels.order_by('-max_price')
    elif sort_type == 'stars':
        # مرتب سازی بر اساس تعداد ستاره ها
        hotels = hotels.order_by('-stars')
    elif sort_type == 'distance':
        # مرتب سازی بر اساس الفبا (نام هتل)
        hotels = hotels.order_by('distance')
    elif sort_type == 'alphabetical':
        # مرتب سازی بر اساس الفبا (نام هتل)
        hotels = hotels.order_by('name')
    else:
        hotels = hotels.order_by('name')
    hotels_per_page = 10
    paginator = Paginator(hotels, hotels_per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    facilities_url = request.GET.get('facilities')
    if facilities_url:
        facilities_url_split = facilities_url.split(',')
        facilities = Facility.objects.filter(name__in=facilities_url_split)
    else:
        facilities = []

    hotel_execution_status = {}
    for hotel in page:
        hotel_execution_status[hotel] = False

    date = request.GET.get('date')
    date_list = date.split(" - ")
    enter_date = date_list[0]
    exit_date = date_list[1]

    is_reserved = {}
    for room in rooms:
        is_reserved[room] = False
        is_reserved[room.count] = room.count

    for room in rooms:
        for my_request in requests:
            if my_request.room == room:
                if my_request.is_overlapping(enter_date, exit_date):
                    is_reserved[room.count] -= 1
                    if is_reserved[room.count] == 0:
                        is_reserved[room] = True

    content = {
        "city": city,
        "cities": cities,
        "hotels": hotels,
        "hotel_count": hotels_count,
        "rooms": rooms,
        "page": page,
        "sort_type": sort_type,
        "facilities": facilities,
        "is_reserved": is_reserved,
        "hotel_execution_status": hotel_execution_status,  # اضافه کردن دیکشنری به context
    }

    return render(request, 'hotels/hotel-list.html', content)


def HotelSingleView(request, city_slug, hotel_slug):
    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    suggest_hotels = Hotel.objects.filter(boroobia_suggest=True).all()
    rooms = Room.objects.filter(hotel=hotel.id)
    requests = Request.objects.all()
    passengers = int(request.GET.get('passengers'))
    code = GenerateRandomStringEndPoint(10)
    canRequest = True
    if request.user.is_authenticated:
        res = request.user.reserves.all()

        for r in res:
            if r.confirm == 'W':
                canRequest = False

    date = request.GET.get('date')
    date_list = date.split(" - ")
    enter_date = date_list[0]
    exit_date = date_list[1]
    high_date = SeasonPrice.objects.get(season_status='H',city=city)
    low_date = SeasonPrice.objects.get(season_status='L',city=city)
    is_reserved = {}
    for room in rooms:
        is_reserved[room] = False
        is_reserved[room.count] = room.count

    for room in rooms:
        for my_request in requests:
            if my_request.room == room:
                if my_request.is_overlapping(enter_date, exit_date):
                    is_reserved[room.count] -= 1
                    if is_reserved[room.count] == 0:
                        is_reserved[room] = True
    format_price = {}
    for room in rooms:
        if enter_date <= high_date.end_date and exit_date >= high_date.start_date:
            format_price[room]= '{:,.0f}'.format(room.high_price)
        elif enter_date <= low_date.end_date and exit_date >= low_date.start_date:
            format_price[room]=  '{:,.0f}'.format(room.low_price)
        else:
            format_price[room]='{:,.0f}'.format(room.price)

    content = {"city": city,
               "hotel": hotel,
               "hotels": hotels,
               'suggest_hotels': suggest_hotels,
               "rooms": rooms,
               'reserve_code': code,
               'passengers': passengers,
               "is_reserved": is_reserved,
               'format_price': format_price,
               'canRequesr': canRequest
               }

    return render(request, 'hotels/hotel-single.html', content)


@login_required
def ShowRequestConfirm(request, room_slug, confirm_city_slug, hotel_slug, reserve_confirm):
    city = City.objects.get(slug=confirm_city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    room = Room.objects.get(slug=room_slug)
    reserve = Request.objects.get(reserve_code=reserve_confirm)
    date_time_object = datetime.strptime(reserve.reserve_time, '%H:%M')
    countdown_duration = timedelta(minutes=20)
    end_time = date_time_object + countdown_duration
    enter = reserve.enter
    exit = reserve.exit

    high_date = SeasonPrice.objects.get(season_status='H', city=city)
    low_date = SeasonPrice.objects.get(season_status='L', city=city)
    enter = datetime.strptime(enter, '%Y/%m/%d').date()
    exit = datetime.strptime(exit, '%Y/%m/%d').date()
    high_date.start_date = datetime.strptime(high_date.start_date, '%Y/%m/%d').date()
    high_date.end_date = datetime.strptime(high_date.end_date, '%Y/%m/%d').date()
    low_date.start_date = datetime.strptime(low_date.start_date, '%Y/%m/%d').date()
    low_date.end_date = datetime.strptime(low_date.end_date, '%Y/%m/%d').date()
    night = (exit - enter).days


    format_price = {}

    if enter <= high_date.end_date and exit >= high_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.high_price * night)
    elif enter <= low_date.end_date and exit >= low_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.low_price * night)
    else:
        format_price[room] = '{:,.0f}'.format(room.price * night)

    context = {
        'enter': enter,
        'exit': exit,
        'room': room,
        'reserve': reserve,
        'hotel': hotel,
        'city': city,
        'format_price': format_price,
        'end_time': end_time,
    }
    return render(request, 'hotels/hotel-confirm.html', context)


@login_required
def RequestConfirmView(request, room_slug, confirm_city_slug, hotel_slug, reserve_confirm):
    city = get_object_or_404(City, slug=confirm_city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = get_object_or_404(Hotel, slug=hotel_slug)
    room = get_object_or_404(Room, slug=room_slug)

    room_count = request.GET.get('room')
    passengers = int(request.GET.get('passengers'))
    children = int(request.GET.get('children'))

    reservasionnumber = ReservasionNumber.objects.get(hotel=room.hotel)
    start_time = datetime.now()
    date = request.GET.get('date')
    date_list = date.split(" - ")
    enter_date = date_list[0]
    exit_date = date_list[1]
    try:
        my_reserve = Request.objects.get(reserve_code=reserve_confirm)
    except Request.DoesNotExist:

        my_reserve = Request.objects.create(
            room=room,
            room_count=room_count,
            enter=enter_date,
            exit=exit_date,
            passenger_count=passengers,
            child_count=children,
            reserve_code=reserve_confirm,
            reservasion_number=reservasionnumber,
            reserve_time=start_time.strftime('%H:%M')
        )
        request.user.reserves.add(my_reserve)

    # passengers = Passenger.objects.filter(reserves__in=my_reserve)
    # children = my_reserve.child_count
    # room_count = my_reserve.room_count

    high_date = SeasonPrice.objects.get(season_status='H', city=city)
    low_date = SeasonPrice.objects.get(season_status='L', city=city)
    enter = datetime.strptime(my_reserve.enter, '%Y/%m/%d').date()
    exit = datetime.strptime(my_reserve.exit, '%Y/%m/%d').date()
    night = (exit - enter).days

    date_time_object = datetime.strptime(my_reserve.reserve_time, '%H:%M')
    countdown_duration = timedelta(minutes=20)
    end_time = date_time_object + countdown_duration

    format_price = {}

    if enter_date <= high_date.end_date and exit_date >= high_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.high_price * night)
    elif enter_date <= low_date.end_date and exit_date >= low_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.low_price * night)
    else:
        format_price[room] = '{:,.0f}'.format(room.price * night)

    context = {
        'end_time': end_time,
        'room': room,
        'reserve': my_reserve,
        'enter': enter_date,
        'exit': exit_date,
        'hotel': hotel,
        'format_price': format_price,
        'city': city,

    }

    return render(request, 'hotels/hotel-confirm.html', context)


@login_required
def OnlineReserveView(request, room_slug, confirm_city_slug, hotel_slug, reserve_confirm):
    city = City.objects.get(slug=confirm_city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    room = Room.objects.get(slug=room_slug)

    date = request.GET.get('date')
    date_list = date.split(" - ")
    enter_date = date_list[0]
    exit_date = date_list[1]
    high_date = SeasonPrice.objects.get(season_status='H', city=city)
    low_date = SeasonPrice.objects.get(season_status='L', city=city)
    enter = datetime.strptime(enter_date, '%Y/%m/%d').date()
    exit = datetime.strptime(exit_date, '%Y/%m/%d').date()
    night = (exit - enter).days
    passengers = int(request.GET.get('passengers'))
    children = int(request.GET.get('children'))
    room_count = request.GET.get('room')
    reservasionnumber = ReservasionNumber.objects.get(hotel=room.hotel)
    start_time = datetime.now()
    reserve_code_status = ''
    try:
        reserve_code_status = Request.objects.get(reserve_code=reserve_confirm)
    except Request.DoesNotExist:

        reserve_code_status = Request.objects.create(
            room=room,
            room_count=room_count,
            enter=enter,
            exit=exit,
            passenger_count=passengers,
            child_count=children,
            reserve_code=reserve_confirm,
            reservasion_number=reservasionnumber,
            reserve_time=start_time.strftime('%H:%M')
        )
        request.user.reserves.add(reserve_code_status)

    date_time_object = datetime.strptime(reserve_code_status.reserve_time, '%H:%M')

    countdown_duration = timedelta(minutes=20)
    end_time = date_time_object + countdown_duration

    format_price = {}

    if enter_date <= high_date.end_date and exit_date >= high_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.high_price*night)
    elif enter_date <= low_date.end_date and exit_date >= low_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.low_price*night)
    else:
        format_price[room] = '{:,.0f}'.format(room.price*night)

    context = {
        'end_time': end_time,
        'room': room,
        'reserve': reserve_code_status,
        'enter': enter_date,
        'exit': exit_date,
        'hotel': hotel,
        'format_price': format_price,
        'city': city,

    }
    return render(request, 'hotels/hotel-confirm-online.html', context)


def RequestCheckView(request, reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    my_reserve.reserve_status = 'P'
    my_reserve.save()
    room = my_reserve.room
    city = room.hotel.city
    passengers = Passenger.objects.filter(reserves=my_reserve)
    enter = datetime.strptime(my_reserve.enter, '%Y/%m/%d').date()
    exit = datetime.strptime(my_reserve.exit, '%Y/%m/%d').date()
    night = (exit - enter).days

    high_date = SeasonPrice.objects.get(season_status='H', city=city)
    low_date = SeasonPrice.objects.get(season_status='L', city=city)
    format_price = {}

    if my_reserve.enter <= high_date.end_date and my_reserve.exit >= high_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.high_price * night)
    elif my_reserve.enter <= low_date.end_date and my_reserve.exit >= low_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.low_price * night)
    else:
        format_price[room] = '{:,.0f}'.format(room.price * night)

    context = {'reserve': my_reserve,
               'room': room,
               'format_price': format_price,
               'passengers': passengers}
    return render(request, 'hotels/hotel-check.html', context)


def HotelBookingView(request, reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    if my_reserve.room.hotel.online_reserve:
        my_reserve.confirm = "A"

    if (my_reserve.reserve_status == "WC" or my_reserve.reserve_status == "WI") and (my_reserve.confirm == "A"):
        number_of_forms = int(my_reserve.passenger_count) + int(my_reserve.child_count) - 1
        myBookingForm = []

        if request.method == 'POST':

            myBookingForm = [BookingForm(request.POST) for _ in range(number_of_forms)]
            headMyBookingForm = BookingForm(request.POST)

            if headMyBookingForm.is_valid():

                nid = headMyBookingForm.cleaned_data.get('nid')

                my_reserve.needs = headMyBookingForm.cleaned_data.get('needs')
                my_reserve.save()
                passenger = Passenger.objects.filter(nid=nid).first()

                if passenger is None:
                    passenger = Passenger.objects.create(
                        firstname=headMyBookingForm.cleaned_data.get('firstname'),
                        lastname=headMyBookingForm.cleaned_data.get('lastname'),
                        email=headMyBookingForm.cleaned_data.get('email'),
                        phone=headMyBookingForm.cleaned_data.get('phone'),
                        nid=nid,
                        birthdate=headMyBookingForm.cleaned_data.get('birthdate')
                    )

                reserve = get_object_or_404(Request, reserve_code=reserve)
                passenger.reserves.add(reserve)
            for _ in range(number_of_forms):
                handler = {
                    'firstname': "",
                    'lastname': "",
                    'email': "",
                    'phone': "",
                    'nid': "",
                    'birthdate': "",
                }
                if myBookingForm[_].is_valid():
                    for key in request.POST.keys():
                        if key != 'csrfmiddlewaretoken':
                            values = request.POST.getlist(key)
                            # اطلاعات از لیست مقادیر بر اساس اندیس _ خوانده می‌شود
                            value = values[_] if _ < len(values) else ""
                            handler[key] = value

                    nid = handler['nid']

                    passenger = Passenger.objects.filter(nid=nid).first()

                    if passenger is None:
                        passenger = Passenger.objects.create(
                            firstname=handler['firstname'],
                            lastname=handler['lastname'],
                            email=headMyBookingForm.cleaned_data.get('email'),
                            phone=headMyBookingForm.cleaned_data.get('phone'),
                            nid=handler['nid'],
                            birthdate=handler['birthdate']
                        )

                    reserve = get_object_or_404(Request, reserve_code=reserve)
                    passenger.reserves.add(reserve)
            return redirect(reverse('hotel-check', kwargs={'reserve': reserve}))
        else:
            myBookingForm = [BookingForm() for _ in range(number_of_forms)]
            headMyBookingForm = BookingForm()

        room = my_reserve.room
        city = room.hotel.city
        hotels = Hotel.objects.filter(city=city.id)
        hotel = room.hotel

        my_reserve.reserve_status = 'WI'
        my_reserve.save()

        today_jalali = jalali_date.today()
        today_jalali_str = today_jalali.strftime("%Y-%m-%d")

        enter = datetime.strptime(my_reserve.enter, '%Y/%m/%d').date()
        exit = datetime.strptime(my_reserve.exit, '%Y/%m/%d').date()
        night = (exit - enter).days

        high_date = SeasonPrice.objects.get(season_status='H', city=city)
        low_date = SeasonPrice.objects.get(season_status='L', city=city)

        format_price = {}

        if my_reserve.enter <= high_date.end_date and my_reserve.exit >= high_date.start_date:
            format_price[room] = '{:,.0f}'.format(room.high_price * night)
        elif my_reserve.enter <= low_date.end_date and my_reserve.exit >= low_date.start_date:
            format_price[room] = '{:,.0f}'.format(room.low_price * night)
        else:
            format_price[room] = '{:,.0f}'.format(room.price * night)

        content = {"city": city,
                   "hotel": hotel,
                   "hotels": hotels,
                   "room": room,
                   "night": night,
                   "reserve": my_reserve,
                   'today': today_jalali_str,
                   'headMyBookingForm': headMyBookingForm,
                   'format_price': format_price,
                   'myBookingForm': myBookingForm,
                   }

        return render(request, 'hotels/hotel-booking.html', content)
    else:
        raise Http404()


def HotelVoucherView(request, reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    passengers = Passenger.objects.filter(reserves=my_reserve)
    hotelphone = ReservasionNumber.objects.get(hotel=my_reserve.room.hotel)
    room = my_reserve.room
    city = room.hotel.city
    enter = datetime.strptime(my_reserve.enter, '%Y/%m/%d').date()
    exit = datetime.strptime(my_reserve.exit, '%Y/%m/%d').date()
    night = (exit - enter).days

    high_date = SeasonPrice.objects.get(season_status='H', city=city)
    low_date = SeasonPrice.objects.get(season_status='L', city=city)
    format_price = {}

    if my_reserve.enter <= high_date.end_date and my_reserve.exit >= high_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.high_price * night)
    elif my_reserve.enter <= low_date.end_date and my_reserve.exit >= low_date.start_date:
        format_price[room] = '{:,.0f}'.format(room.low_price * night)
    else:
        format_price[room] = '{:,.0f}'.format(room.price * night)
    if my_reserve.reserve_status == 'D':
        context = {
            'reserve': my_reserve,
            'format_price':format_price,
            'room':room,
            'passengers': passengers,
            'hotelphone': hotelphone
        }
        return render(request, 'hotels/hotel-voucher.html', context)

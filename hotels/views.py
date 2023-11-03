import accounts.views
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Min,F
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect
from django.http import JsonResponse,Http404,HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from urllib.parse import urlencode
from datetime import datetime, timedelta
from jdatetime import date as jalali_date,timedelta as jalali_timedelta
from main.models import City,Hotel,Room,Request,Passenger,Facility
from main.forms import BookingForm,BookingModelForm
from .serializer import HotelSerializer,HotelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import random
import string
import time

# Create your views here.
def check_reservation_status(request, reserve_confirm):
    try:
        reserve_code_status = Request.objects.get(reserve_code=reserve_confirm)
        data = {'confirm': reserve_code_status.confirm}
    except Request.DoesNotExist:
        data = {'confirm': 'W'}  # یا مقدار دلخواه دیگری

    return JsonResponse(data)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def hotellike(request, pk):
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

def home(request):
    current_date = jalali_date.today()
    exit_date=current_date + jalali_timedelta(days=4)
    formatted_exit_date = exit_date.strftime('%Y/%m/%d')
    formatted_current_date = current_date.strftime('%Y/%m/%d')
    cities = City.objects.all()
    hotels = Hotel.objects.all()
    suggest_hotels = Hotel.objects.filter(boroobia_suggest=True).all()
    facilities = Facility.objects.all()
    kish_count = City.objects.get(faname='کیش').hotel_set.count()
    mashhad_count = City.objects.get(faname='مشهد').hotel_set.count()
    qeshm_count = City.objects.get(faname='قشم').hotel_set.count()
    isfahan_count = City.objects.get(faname='اصفهان').hotel_set.count()
    shiraz_count = City.objects.get(faname='شیراز').hotel_set.count()
    tabriz_count = City.objects.get(faname='تبریز').hotel_set.count()
    # hotel = Hotel.objects.get(slug=hotels.slug)
    content = {'cities': cities,
               'hotels':hotels,
               'suggest_hotels':suggest_hotels,
               'facilities':facilities,
               'kish_count':kish_count,
               'mashhad_count':mashhad_count,
               'qeshm_count':qeshm_count,
               'tabriz_count':tabriz_count,
               'shiraz_count':shiraz_count,
               'isfahan_count':isfahan_count,
               'formatted_current_date':formatted_current_date,
               'formatted_exit_date':formatted_exit_date,}
    return render(request, 'hotels/hotel-home.html', content)




def list(request, city_slug):
    city = City.objects.get(slug=city_slug)
    cities = City.objects.all()
    hotels = Hotel.objects.filter(city=city.id)
    hotels_count = Hotel.objects.filter(city=city.id).count()

    # دریافت نوع مرتب سازی از پارامتر درخواست کاربر
    sort_type = request.GET.get('sort-select')

    if sort_type == 'suggest':
        # مرتب سازی بر اساس قیمت کمترین به بیشترین
        hotels = hotels.annotate(min_price=Min('room__price'))
        hotels = hotels.order_by('min_price')
    elif sort_type == 'cheapest':
        # مرتب سازی بر اساس قیمت کمترین به بیشترین
        hotels = hotels.annotate(min_price=Min('room__price'))
        hotels = hotels.order_by('min_price')
    elif sort_type == 'expensive':
        # مرتب سازی بر اساس قیمت بیشترین به کمترین
        hotels = hotels.annotate(max_price=Max('room__price'))
        hotels = hotels.order_by('-max_price')
    elif sort_type == 'stars':
        # مرتب سازی بر اساس تعداد ستاره ها
        hotels = hotels.order_by('-starts')
    elif sort_type == 'alphabetical':
        # مرتب سازی بر اساس الفبا (نام هتل)
        hotels = hotels.order_by('name')

    hotels_per_page = 2
    paginator = Paginator(hotels, hotels_per_page)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    content = {"city": city,
               "cities": cities,
               "hotels": hotels,
               "hotel_count": hotels_count,
               "page": page,
               "sort_type": sort_type}  # اضافه کردن نوع مرتب سازی به متغیرهای تمپلیت

    return render(request, 'hotels/hotel-list.html', content)


@login_required
def confirm(request,room_slug,confirm_city_slug,hotel_slug,reserve_confirm):

    city = City.objects.get(slug=confirm_city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    rooms = Room.objects.get(slug=room_slug)

    date = request.GET.get('date')
    date_list = date.split(" - ")
    enter = date_list[0]
    exit = date_list[1]
    passengers = int(request.GET.get('passengers'))
    children = int(request.GET.get('children'))
    room_count = request.GET.get('room')

    start_time = datetime.now()
    reserve_code_status = ''
    try:
        reserve_code_status = Request.objects.get(reserve_code=reserve_confirm)
    except Request.DoesNotExist:

        reserve_code_status = Request.objects.create(
            room=rooms,
            room_count=room_count,
            enter=enter,
            exit=exit,
            passenger_count=passengers,
            child_count=children,
            reserve_code=reserve_confirm,
            reserve_time = start_time.strftime('%H:%M')
        )


    date_time_object = datetime.strptime(reserve_code_status.reserve_time, '%H:%M')


    countdown_duration = timedelta(minutes=20)
    end_time = date_time_object + countdown_duration



    context = {
        'end_time': end_time,
        'room':rooms,
        'reserve':reserve_code_status,
        'enter':enter,
        'exit':exit,
        'hotel':hotel,
        'city':city,

    }
    return render(request, 'hotels/hotel-confirm.html', context)


def check(request,reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    my_reserve.reserve_status = 'P'
    my_reserve.save()
    passengers = Passenger.objects.filter(reserves=my_reserve)

    context = {'reserve': my_reserve, 'passengers': passengers}
    return render(request,'hotels/hotel-check.html',context)


def single(request, city_slug, hotel_slug):

    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    suggest_hotels = Hotel.objects.filter(boroobia_suggest=True).all()
    rooms = Room.objects.filter(hotel=hotel.id)
    code = generate_random_string(10)


    content = {"city": city,
               "hotel": hotel,
               "hotels": hotels,
               'suggest_hotels': suggest_hotels,
               "rooms": rooms,
               'reserve_code':code
               }

    return render(request, 'hotels/hotel-single.html', content)


def booking(request,reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    if (my_reserve.reserve_status =="WC" or my_reserve.reserve_status=="WI") and (my_reserve.confirm == "A"):
        number_of_forms = int(my_reserve.passenger_count) + int(my_reserve.child_count)-1
        myBookingForm = []

        if request.method == 'POST':

            myBookingForm = [BookingForm(request.POST) for _ in range(number_of_forms)]
            headMyBookingForm = BookingForm(request.POST)

            if headMyBookingForm.is_valid():

                nid = headMyBookingForm.cleaned_data.get('nid')
                print(nid)

                my_reserve.needs = headMyBookingForm.cleaned_data.get('needs')
                print(my_reserve.needs)
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
                    print(nid)

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

            return redirect(
                        reverse('hotel-check', kwargs={'reserve': reserve}))  # به عنوان مثال، ریدایرکت در اینجا


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

        content = {"city": city,
                   "hotel": hotel,
                   "hotels":hotels,
                   "room":room,
                   "night":night,
                   "reserve": my_reserve,
                   'today': today_jalali_str,
                   'headMyBookingForm': headMyBookingForm,
                   'myBookingForm': myBookingForm,
                   }

        return render(request, 'hotels/hotel-booking.html',content)
    else:
        raise Http404()


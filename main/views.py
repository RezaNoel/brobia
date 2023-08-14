from django.shortcuts import render,redirect,get_object_or_404
from .models import City,Hotel,Room,Request,Passenger
from jdatetime import date as jalali_date,timedelta as jalali_timedelta
from django.db.models import Min
from django.urls import reverse
from .forms import BookingForm,BookingModelForm
from datetime import datetime, timedelta
from django.shortcuts import redirect
from urllib.parse import urlencode
from django.http import JsonResponse,Http404,HttpResponseNotFound
from django.contrib import messages
# from jdatetime import datetime as j


import random
import string
import time

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
def home(request):
    current_date = jalali_date.today()
    exit_date=current_date + jalali_timedelta(days=4)
    formatted_exit_date = exit_date.strftime('%Y/%m/%d')
    formatted_current_date = current_date.strftime('%Y/%m/%d')
    # print(formatted_new_date)

    cities = City.objects.all()
    hotels = Hotel.objects.all()
    kish_count = City.objects.get(faname='کیش').hotel_set.count()
    mashhad_count = City.objects.get(faname='مشهد').hotel_set.count()
    qeshm_count = City.objects.get(faname='قشم').hotel_set.count()
    isfahan_count = City.objects.get(faname='اصفهان').hotel_set.count()
    shiraz_count = City.objects.get(faname='شیراز').hotel_set.count()
    tabriz_count = City.objects.get(faname='تبریز').hotel_set.count()
    # hotel = Hotel.objects.get(slug=hotels.slug)
    content = {'cities': cities,
               'hotels':hotels,
               'kish_count':kish_count,
               'mashhad_count':mashhad_count,
               'qeshm_count':qeshm_count,
               'tabriz_count':tabriz_count,
               'shiraz_count':shiraz_count,
               'isfahan_count':isfahan_count,
               'formatted_current_date':formatted_current_date,
               'formatted_exit_date':formatted_exit_date,}
    return render(request, 'hotel-home.html', content)

def list(request, city_slug):
    city = City.objects.get(slug=city_slug)
    cities = City.objects.all()
    hotels_count = Hotel.objects.filter(city=city.id).count()
    hotels = Hotel.objects.filter(city=city.id)

    content = {"city": city,
               "cities": cities,
               "hotels": hotels,
               "hotel_count": hotels_count}

    return render(request, 'hotel-list.html', content)

def single(request, city_slug, hotel_slug):

    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    rooms = Room.objects.filter(hotel=hotel.id)
    code = generate_random_string(10)


    content = {"city": city,
               "hotel": hotel,
               "hotels": hotels,
               "rooms": rooms,
               'reserve_code':code
               }

    return render(request, 'hotel-single.html', content)


def confirm(request,room_slug,city_slug,hotel_slug,reserve_confirm):


    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    rooms = Room.objects.get(slug=room_slug)

    enter = request.GET.get('enter')
    exit = request.GET.get('exit')
    passengers = int(request.GET.get('passengers'))
    children = int(request.GET.get('children'))
    room_count = request.GET.get('room')
    print(room_count)
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
            reserve_code=reserve_confirm
        )


    start_time = datetime.now()
    countdown_duration = timedelta(minutes=20)
    end_time = start_time + countdown_duration



    context = {
        'end_time': end_time,
        'room':rooms,
        'reserve':reserve_code_status,
        'enter':enter,
        'exit':exit,
        'hotel':hotel,
        'city':city,

    }
    return render(request, 'hotel-confirm.html', context)


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

        return render(request, 'hotel-booking.html',content)
    else:
        return HttpResponseNotFound()
def check(request,reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    my_reserve.reserve_status = 'P'
    my_reserve.save()
    context = {'reserve':my_reserve}
    return render(request,'hotel-check.html',context)



def login(request):
    return render(request, 'login.html')



from django.shortcuts import render,redirect
from .models import City,Hotel,Room,Request,Passenger
from jdatetime import date as jalali_date
from django.db.models import Min
from django.urls import reverse
from .forms import BookingForm,BookingModelForm
from datetime import datetime, timedelta
from django.shortcuts import redirect
from urllib.parse import urlencode
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages


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
    cities = City.objects.all()
    hotels = Hotel.objects.all()
    kish_count = City.objects.get(faname='کیش').hotel_set.count()
    mashhad_count = City.objects.get(faname='مشهد').hotel_set.count()
    qeshm_count = City.objects.get(faname='قشم').hotel_set.count()
    isfahan_count = City.objects.get(faname='اصفهان').hotel_set.count()
    shiraz_count = City.objects.get(faname='شیراز').hotel_set.count()
    tabriz_count = City.objects.get(faname='تبریز').hotel_set.count()
    # hotel = Hotel.objects.get(slug=hotels.slug)
    content = {'cities': cities,'hotels':hotels,'kish_count':kish_count,'mashhad_count':mashhad_count,'qeshm_count':qeshm_count,'tabriz_count':tabriz_count,'shiraz_count':shiraz_count,'isfahan_count':isfahan_count}
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
    # headers = request.META

    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    rooms = Room.objects.get(slug=room_slug)

    enter = request.GET.get('enter')
    # user_agent = request.META.get('Confirm', None)
    # print(user_agent)
    exit = request.GET.get('exit')
    passengers = int(request.GET.get('passengers'))
    children = int(request.GET.get('children'))
    room_count = request.GET.get('room')
    print(room_count)
    reserve_code_status = ''
    try:
        reserve_code_status = Request.objects.get(reserve_code=reserve_confirm)
    except Request.DoesNotExist:
        # رکورد با این کد رزرو وجود ندارد، بنابراین آن را ایجاد کنید
        reserve_code_status = Request.objects.create(
            room=rooms,
            room_count=room_count,
            enter=enter,
            exit=exit,
            passenger_count=passengers,
            child_count=children,
            reserve_code=reserve_confirm
            # دیگر فیلدهای مورد نیاز را اینجا پر کنید
        )

    # reserve_code_status = Request.objects.get(reserve_code=reserve_confirm)
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


def booking(request,city_slug,hotel_slug,room_slug,reserve):


    # print(reserve)
    if request.method == 'POST':
        bookingForm = BookingForm(request.POST)
        if bookingForm.is_valid():
            nid = bookingForm.cleaned_data.get('nid')

            passenger = Passenger.objects.filter(nid=nid).first()

            if passenger is None:
                passenger = Passenger.objects.create(
                    firstname=bookingForm.cleaned_data.get('firstname'),
                    lastname=bookingForm.cleaned_data.get('lastname'),
                    email=bookingForm.cleaned_data.get('email'),
                    phone=bookingForm.cleaned_data.get('phone'),
                    nid=nid,
                    birthdate=bookingForm.cleaned_data.get('birthdate')
                )


            reserve = get_object_or_404(Request, reserve_code=reserve)
            passenger.reserves.add(reserve)

            return redirect(reverse('hotel-check', kwargs={'reserve': reserve}))

    else:
        bookingForm = BookingForm()

    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    room = Room.objects.get(slug=room_slug)
    my_reserve = Request.objects.get(reserve_code=reserve)
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
               'bookingForm': bookingForm}
    return render(request, 'hotel-booking.html',content)

def check(request,reserve):
    my_reserve = Request.objects.get(reserve_code=reserve)
    my_reserve.reserve_status = 'P'
    my_reserve.save()
    context = {'reserve':my_reserve}
    return render(request,'hotel-check.html',context)



def login(request):
    return render(request, 'login.html')



from django.shortcuts import render,redirect
from .models import City,Hotel,Room
from jdatetime import date as jalali_date
from django.db.models import Min
from django.urls import reverse
from .forms import BookingForm,BookingModelForm
from datetime import datetime, timedelta
import time

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

    content = {"city": city,
               "hotel": hotel,
               "hotels": hotels,
               "rooms": rooms}

    return render(request, 'hotel-single.html', content)

def booking(request,city_slug,hotel_slug,room_slug):


    print(request.method)
    if request.method == 'POST':
        bookingForm = BookingForm(request.POST)
        if bookingForm.is_valid():
            print(bookingForm.cleaned_data)
            return redirect(reverse('hotel-confirm'))
    else:
        bookingForm = BookingForm()
    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    room = Room.objects.get(slug=room_slug)
    today_jalali = jalali_date.today()
    today_jalali_str = today_jalali.strftime("%Y-%m-%d")


        #

    content = {"city": city,
               "hotel": hotel,
               "hotels":hotels,
               "room":room,
               'today': today_jalali_str,
               'bookingForm': bookingForm}
    return render(request, 'hotel-booking.html',content)


def login(request):
    return render(request, 'login.html')

def confirm(request,room_slug,city_slug,hotel_slug):
    city = City.objects.get(slug=city_slug)
    hotels = Hotel.objects.filter(city=city.id)
    hotel = Hotel.objects.get(slug=hotel_slug)
    rooms = Room.objects.get(slug=room_slug)
    room = rooms.faname
    room_count = request.GET.get('room')
    enter = request.GET.get('enter')
    exit = request.GET.get('exit')
    passengers = request.GET.get('passengers')
    children = request.GET.get('children')
    passengers_count = int(passengers)+int(children)
    print(room_count,enter,exit,passengers_count)

    start_time = datetime.now()
    countdown_duration = timedelta(minutes=1)
    end_time = start_time + countdown_duration

    context = {
        'end_time': end_time,
    }
    return render(request, 'hotel-confirm.html', context)



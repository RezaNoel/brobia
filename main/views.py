from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Min
from django.urls import reverse
from django.shortcuts import redirect
from django.http import JsonResponse,Http404,HttpResponseNotFound
from django.contrib import messages
from urllib.parse import urlencode
from datetime import datetime, timedelta
from jdatetime import date as jalali_date,timedelta as jalali_timedelta
from .models import City,Hotel,Room,Request,Passenger
from .forms import BookingForm,BookingModelForm

import random
import string
import time


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







def custom_404(request, exception):
    return render(request, '404.html', status=404)


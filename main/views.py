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

def about(request):
    pass

def contact(request):
    pass





def custom_404(request, exception):
    return render(request, '404.html', status=404)


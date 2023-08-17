from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse

import main

# Create your views here.

def LoginView(request):
    if request.method =='POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse(main.views.home))
            else:
                context = {
                    'username':username,
                    'error_message':'اطلاعات اشتباه است'
                }
                return render(request, 'accounts/login.html', context)
    else:
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

    return render(request, 'accounts/login.html', context)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(main.views.home))

def RegisterView(request):
    if request.method =='POST':
        register_form = RegisterForm(request.POST)
        context = {
            'register_form': register_form
        }
        return render(request, 'hotel-home.html', context)
    else:
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

    return render(request, 'accounts/register.html', context)




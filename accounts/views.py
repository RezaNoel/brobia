import hotels.views
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
from .forms import LoginForm,RegisterForm
import main


# Create your views here.

def LoginView(request):
    if request.method =='POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            user = authenticate(request,username=phone,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse(hotels.views.home))
            else:
                loginForm = LoginForm()
                context = {
                    'loginForm': loginForm,
                    'error_message':'نام کاربری یا رمز عبور اشتباه است.'
                }
                return render(request, 'accounts/login.html', context)
    else:
        loginForm = LoginForm()
        context = {
            'loginForm': loginForm
        }

    return render(request, 'accounts/login.html', context)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(hotels.views.home))

def RegisterView(request):
    if request.method =='POST':
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            # Variables

            email = registerForm.cleaned_data.get('email')
            password = registerForm.cleaned_data.get('password')
            first_name = registerForm.cleaned_data.get('first_name')
            last_name = registerForm.cleaned_data.get('last_name')
            phone = registerForm.cleaned_data.get('phone')
            nid = registerForm.cleaned_data.get('nid')
            username = phone
            # Create User
            user = User(username=username,email=email,first_name=first_name,last_name=last_name,phone=phone,nid=nid)
            user.set_password(password)
            user.save()

            # Login User
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return HttpResponseRedirect(reverse(main.views.home))
        context = {
            'registerForm': registerForm
        }

        return render(request, 'hotel-home.html', context)
    else:
        registerForm = RegisterForm()
        context = {
            'registerForm': registerForm
        }

    return render(request, 'accounts/register.html', context)


def UserProfileView(request):
    return render(request, 'accounts/user_profile.html')

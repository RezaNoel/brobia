import hotels.views
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User,HotelManagerModel
from .forms import LoginForm,RegisterForm,CustomPasswordChangeForm
import main



# Create your views here.

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

            return HttpResponseRedirect(reverse(hotels.views.HotelHomeView))
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

def LoginView(request):
    if request.method =='POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            user = authenticate(request,username=phone,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse(hotels.views.HotelHomeView))
            elif len(password)<8:
                loginForm = LoginForm()
                context = {
                    'loginForm': loginForm,
                    'error_message': 'رمز عبور باید حداقل 8 کاراکتر باشد.'
                }
                return render(request, 'accounts/login.html', context)
            elif password==None:
                loginForm = LoginForm()
                context = {
                    'loginForm': loginForm,
                    'error_message': 'رمز عبوراجباریست.'
                }
                return render(request, 'accounts/login.html', context)
            elif len(phone)!=11:
                loginForm = LoginForm()
                context = {
                    'loginForm': loginForm,
                    'error_message': 'شماره همراه باید 11 کاراکتر باشد.'
                }
                return render(request, 'accounts/login.html', context)
            else:
                loginForm = LoginForm()
                context = {
                    'loginForm': loginForm,
                    'error_message':'شماره همراه یا رمز عبور اشتباه است.'
                }
                return render(request, 'accounts/login.html', context)
    else:
        loginForm = LoginForm()
        context = {
            'loginForm': loginForm
        }

    return render(request, 'accounts/login.html', context)
@login_required
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(hotels.views.HotelHomeView))

@login_required
def UserProfileView(request):
    try:
        myHotel = HotelManagerModel.objects.get(user=request.user)
        isHotelManager = True
    except HotelManagerModel.DoesNotExist:
        isHotelManager = False
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)

    context = {
        'form': form,
        'isHotelManager': isHotelManager
    }
    return render(request, 'accounts/user_profile.html', context)

@login_required
def HotelAdminView(request,page):
    myHotel = HotelManagerModel.objects.get(user=request.user)
    template_name = f'accounts/hotel_panel_{page}.html'

    context = {
        'myHotel': myHotel
    }
    return render(request, template_name, context)


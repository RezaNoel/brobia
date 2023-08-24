from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ProfileModel
import main
from django.contrib.auth.models import User


# Create your views here.

def LoginView(request):
    if request.method =='POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse(main.views.home))
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
    return HttpResponseRedirect(reverse(main.views.home))

def RegisterView(request):
    if request.method =='POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():

            user = User.objects.create_user(
                username = registerForm.cleaned_data['username'],
                email = registerForm.cleaned_data['email'],
                password = registerForm.cleaned_data['password'],
            )


            user.save()

            # profileModel = ProfileModel(user = user,
            #                             name = registerForm.cleaned_data.get('first_name'),
            #                             family = registerForm.cleaned_data.get('last_name'),
            #                             phone = registerForm.cleaned_data.get('phone'),
            #                             nid = registerForm.cleaned_data.get('nid'),
            #                             birthday = registerForm.cleaned_data.get('birthday'))
            # profileModel.save()
            return HttpResponseRedirect(reverse(main.views.home))
        context = {
            'registerForm': registerForm
        }

        return render(request, 'hotel-home.html', context)
    else:
        registerForm = RegisterForm()
        context = {
            'registerForm': RegisterForm
        }

    return render(request, 'accounts/register.html', context)




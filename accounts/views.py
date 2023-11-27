import hotels.views
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User,HotelManagerModel
from hotels.models import Facility,Room
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import LoginForm,RegisterForm,CustomPasswordChangeForm,UserProfileForm,CustomPasswordResetForm,ProfileForm
import main
from kavenegar import KavenegarAPI,APIException,HTTPException
from random import randint, randrange



# Create your views here.

class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password_reset/done'
    form_class = CustomPasswordResetForm
    success_message = "لینک بازیابی رمز عبور به ایمیل شما ارسال شد."

    def send_sms(self, code, receptor):
        messages = f"{code} رمز یکبار مصرف ورود به بروبیا:"
        api = KavenegarAPI('736C5461342F426C7630656C346C38726D576E734D5A4536726F30773245546361693471632F682B2B316F3D')
        params = {'sender': '2000500666', 'receptor': receptor, 'message': messages}
        response = api.sms_send(params)

    def form_valid(self, form):
        response = super().form_valid(form)
        # ارسال کد تایید به شماره تلفن
        code = str(randrange(1000, 9999))
        self.send_sms(code, form.cleaned_data['email'])
        return response
def kave_negar_token_send(request):
    code =str( randrange(1000, 9999))
    messages = code + " " + 'رمز یکبار مصرف ورود به بروبیا:'
    api = KavenegarAPI('736C5461342F426C7630656C346C38726D576E734D5A4536726F30773245546361693471632F682B2B316F3D')
    params = {'sender': '2000500666', 'receptor': '09129471382', 'message': messages}
    response = api.sms_send(params)
    return HttpResponseRedirect(reverse(LoginView))
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

        return HttpResponseRedirect(reverse(hotels.views.HotelHomeView))
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

            # api = KavenegarAPI(
            #     '736C5461342F426C7630656C346C38726D576E734D5A4536726F30773245546361693471632F682B2B316F3D')
            # params = {'sender': '1000689696', 'receptor': '09129471382', 'message': '.'}
            # response = api.sms_send(params)

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
    form = CustomPasswordChangeForm(request.user)
    updateProfileForm = UserProfileForm()
    myProfileForm = ProfileForm()
    if request.method == 'POST':
        if 'first_name' in request.POST:
            updateProfileForm = UserProfileForm(request.POST, request.FILES, instance=request.user)
            if updateProfileForm.is_valid():
                updateProfileForm.save()
        if 'profile' in request.POST:
            print('profile')
            print(request.POST)
            print(request.FILES)
            myProfileForm = ProfileForm(request.POST,request.FILES)
            if myProfileForm.is_valid():
                print('profile is valid')
                profile = UserProfileForm(profile=request.FILES["profile"])
                profile.save()
        elif 'old_password' in request.POST:
            form = CustomPasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                updateProfileForm = YourUpdateProfileForm()

    else:
        form = CustomPasswordChangeForm(request.user)
        updateProfileForm = UserProfileForm()

    context = {
        'form': form,
        'updateProfileForm':updateProfileForm,
        'myProfileForm':myProfileForm,
        'isHotelManager': isHotelManager
    }
    return render(request, 'accounts/user_profile.html', context)

@login_required
def HotelAdminView(request,page):
    myHotel = HotelManagerModel.objects.get(user=request.user)
    hotelFacilities = Facility.objects.filter(related='H')
    roomFacilities = Facility.objects.filter(related='R')
    rooms = Room.objects.filter(hotel=myHotel.hotel)
    facilities = myHotel.hotel.facilities.all()
    if request.method == 'POST':
        if 'hotelShortAbout' in request.POST:
            myHotel.hotel.description = request.POST.get('hotelShortAbout')
            myHotel.hotel.explanation = request.POST.get('hotelLongAbout')
            myHotel.hotel.terms = request.POST.get('hotelRules')
            myHotel.hotel.save()
        elif 'roomName' in request.POST:
            room_name = request.POST.get('roomName')
            bed_count = int(request.POST.get('bedCounts'))
            room_price = int(request.POST.get('roomPrice'))

            new_room = Room(name=room_name,faname=room_name,bed=bed_count,price=room_price, hotel=myHotel.hotel)
            new_room.save()
            for facility in roomFacilities:
                checkbox_name = f'facility_checkbox_{facility.id}'
                if checkbox_name in request.POST:
                    new_room.facilities.add(facility)
                else:
                    new_room.facilities.remove(facility)

        else:
            for facility in hotelFacilities:
                checkbox_name = f'facility_checkbox_{facility.id}'
                if checkbox_name in request.POST:
                    myHotel.hotel.facilities.add(facility)
                else:
                    myHotel.hotel.facilities.remove(facility)


    template_name = f'accounts/hotel-panel/hotel_panel_{page}.html'
    context = {
        'myHotel': myHotel,
        'rooms': rooms,
        'hotelFacilities': hotelFacilities,
        'roomFacilities': roomFacilities,
        'facilities':facilities
    }
    return render(request, template_name, context)

def RoomSingleView(request,page, room_slug):
    myHotel = HotelManagerModel.objects.get(user=request.user)
    room = Room.objects.get(slug=room_slug)

    content = {"room": room,
                "myHotel": myHotel
               }

    return render(request, 'accounts/hotel-panel/hotel_panel_room_single.html', content)




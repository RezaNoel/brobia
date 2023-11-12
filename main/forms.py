from django import forms
from .models import Request
from jalali_date.fields import JalaliDateField
from django.core.validators import RegexValidator


class BookingForm(forms.Form):
    firstname = forms.CharField(label='* نام',error_messages={'required':'وارد کردن نام اجباری است.'},widget=forms.TextInput(attrs={'id': 'firstname','class':'form-control','placeholder':'علی'}))
    lastname = forms.CharField(label='* نام خانوادگی',error_messages={'required':'وارد کردن نام اجباری است.'},widget=forms.TextInput(attrs={'id': 'lastname','class':'form-control','placeholder':'اوجی'}))
    email = forms.EmailField(required=False,label='ایمیل',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'test@gmail.com'}))
    phone = forms.CharField(
        required=False,
        label='* شماره موبایل',
        error_messages={'required': 'وارد کردن شماره موبایل اجباری است.'},
        validators=[RegexValidator(r'^[0-9]*$', 'شماره موبایل باید تنها شامل اعداد باشد.')],
    widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '09121234567'})
    )
    nid = forms.CharField(
        label='* کدملی',
        error_messages={'required': 'وارد کردن کد ملی اجباری است.'},
        validators=[RegexValidator(r'^[0-9]*$', 'کد ملی باید تنها شامل اعداد باشد.')],
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0123456789'})
    )
    birthdate = forms.CharField(
        label='* تاریخ تولد',
        widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': '1402/04/15'}),
        error_messages={'required': 'وارد کردن تاریخ تولد اجباری است.'}
    )
    needs = forms.CharField(required=False, label='نیازمندی های ویژه',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'ویلچر ، تخت اضافه...'}))

class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Request
        fields =['room', 'room_count', 'enter','exit','passenger_count']



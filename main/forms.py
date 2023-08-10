from django import forms
from .models import Request
from jalali_date.fields import JalaliDateField

class BookingForm(forms.Form):
    firsrname = forms.CharField(label='* نام',error_messages={'required':'وارد کردن نام اجباری است.'},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'علی'}))
    lastname = forms.CharField(label='* نام خانوادگی',error_messages={'required':'وارد کردن نام اجباری است.'},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'اوجی'}))
    email = forms.EmailField(required=False,label='ایمیل',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'test@gmail.com'}))
    number = forms.IntegerField(label='شماره موبایل',error_messages={'required':'وارد کردن شماره موبایل اجباری است.'},widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'09121234567'}))
    nid = forms.IntegerField(label='کدملی',error_messages={'required':'وارد کردن کد ملی اجباری است.'},widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'0123456789'}))
    birthdate = forms.CharField(
        label='تاریخ تولد',
        widget=forms.TextInput(attrs={'class': 'form-control datepic data-jdp', 'placeholder': '1402-04-15'}),
        error_messages={'required': 'وارد کردن تاریخ تولد اجباری است.'}
    )
    neeeds = forms.CharField(required=False, label='نیازمندی های ویژه',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'ویلچر ...'}))

    # class BookingModelForm(forms.ModelForm):
    #     class Meta:
    #         model = Request
    #         fields =['']
    #
    #

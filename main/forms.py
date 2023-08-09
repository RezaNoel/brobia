from django import forms


class BookingForm(forms.Form):
    firsrname = forms.CharField(label='* نام',error_messages={'required':'وارد کردن نام اجباری است.'},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'علی'}))
    lastname = forms.CharField(label='* نام خانوادگی',error_messages={'required':'وارد کردن نام اجباری است.'},widget=forms.TextInput(attrs={'class':'form-control','placeholder':'اوجی'}))
    email = forms.EmailField(required=False,label='ایمیل',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'test@gmail.com'}))
    number = forms.IntegerField(label='شماره موبایل',error_messages={'required':'وارد کردن شماره موبایل اجباری است.'},widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'09121234567'}))
    nid = forms.IntegerField(label='کدملی',error_messages={'required':'وارد کردن کد ملی اجباری است.'},widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'0123456789'}))
    birthdate = forms.DateField(label='تاریخ تولد')
    neeeds = forms.CharField(required=False, label='نیازمندی های ویژه',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'ویلچر ...'}))
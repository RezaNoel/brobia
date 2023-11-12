from django import forms
from .models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm,PasswordChangeForm


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="آدرس ایمیل", max_length=254, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'آدرس ایمیل خود را وارد کنید'}
    ))

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="رمز عبور جدید",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'old_password'})
    )
    new_password1 = forms.CharField(
        label="رمز عبور جدید",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password',
                                          'oninvalid': "setCustomValidity('لطفا رمز عبور جدید خود را وارد کنید')",
                                          'onchange': "try{setCustomValidity('')}catch(e){}", 'spellcheck': 'false',
                                          'autocorrect': 'off', 'autocapitalize': 'off', 'name': 'current-password',
                                          'autocomplete': 'current-password'})
    )

    new_password2 = forms.CharField(
        label="تکرار رمز عبور جدید",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirm_password',
                                          'oninvalid': "setCustomValidity('لطفا رمز عبور جدید را مجددا وارد کنید')",
                                          'onchange': "try{setCustomValidity('')}catch(e){}", 'spellcheck': 'false',
                                          'autocorrect': 'off', 'autocapitalize': 'off', 'name': 'current-password',
                                          'autocomplete': 'current-password'})
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="رمز عبور جدید",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'oninvalid': "setCustomValidity('لطفا رمز عبور جدید خود را وارد کنید')",'onchange': "try{setCustomValidity('')}catch(e){}", 'spellcheck': 'false', 'autocorrect': 'off', 'autocapitalize': 'off', 'name': 'current-password', 'autocomplete': 'current-password'})
    )

    new_password2 = forms.CharField(
        label="تکرار رمز عبور جدید",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'confirm_password', 'oninvalid': "setCustomValidity('لطفا رمز عبور جدید را مجددا وارد کنید')",'onchange': "try{setCustomValidity('')}catch(e){}", 'spellcheck': 'false', 'autocorrect': 'off', 'autocapitalize': 'off', 'name': 'current-password', 'autocomplete': 'current-password'})
    )

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="نام",max_length=100,required=False, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'نام خود را وارد کنید'}
    ))
    last_name = forms.CharField(label="نام خانوادگی",max_length=100,required=False, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'نام خانوادگی خود را وارد کنید'}
    ))

    password = forms.CharField(label="رمز عبور",max_length=100,required=True,validators=[
        MinLengthValidator(limit_value=8, message="پسورد باید حداقل 8 کاراکتر داشته باشد.")
    ], widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'رمز عبور خود را وارد کنید'}
    ))
    confirm_password = forms.CharField(label="تکرار رمز عبور", max_length=100,required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور خود را وارد کنید'}
    ))
    email = forms.CharField(label="ایمیل",max_length=100,required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control','placeholder': 'ایمیل خود را وارد کنید'}
    ))
    nid = forms.CharField(label="کدملی",validators=[
        MinLengthValidator(limit_value=10, message="کدملی باید حداقل 10 کاراکتر داشته باشد."),
        MaxLengthValidator(limit_value=10, message="کدملی نمی‌تواند بیش از 10 کاراکتر داشته باشد.")
    ])
    phone = forms.CharField(label="شماره همراه",validators=[
        MinLengthValidator(limit_value=11, message="شماره همراه باید حداقل 11 کاراکتر داشته باشد."),
        MaxLengthValidator(limit_value=11, message="شماره همراه نمی‌تواند بیش از 11 کاراکتر داشته باشد.")
    ])

    class Meta:
        model = User
        fields = ['phone', 'nid','birthdate']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': '09XXXXXXXXX'})
        self.fields['nid'].widget.attrs.update({'class': 'form-control', 'placeholder': 'کد ملی خود را وارد کنید'})
        self.fields['birthdate'].widget.attrs.update({'class': 'form-control', 'placeholder': 'تاریخ تولد خود را وارد کنید'})

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if not re.match(r'^09\d{9}$', phone):
    #         raise forms.ValidationError('شماره تماس را به درستی وارد کنید (با قالب 09xxxxxxxxx)')
    #     return phone


class LoginForm(forms.ModelForm):
    # username = forms.CharField(label="نام کاربری",max_length=100, widget=forms.TextInput(
    #     attrs={'class': 'form-control','placeholder': 'نام کاربری خود را وارد کنید'}
    # ))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control','id':'password','placeholder': 'رمز عبور خود را وارد کنید', 'oninvalid': "setCustomValidity('لطفا رمز عبور خود را وارد کنید')",'onchange': "try{setCustomValidity('')}catch(e){}", 'spellcheck': 'false', 'autocorrect': 'off', 'autocapitalize': 'off', 'name': 'current-password', 'autocomplete': 'current-password'}
    ))

    class Meta:
        model = User
        fields = ['phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '09XXXXXXXXX'})


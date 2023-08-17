from django import forms
from .models import ProfileModel
class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="نام",max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'نام خود را وارد کنید'}
    ))
    last_name = forms.CharField(label="نام خانوادگی",max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'نام خانوادگی خود را وارد کنید'}
    ))
    username = forms.CharField(label="نام کاربری",max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'نام کاربری خود را وارد کنید'}
    ))
    password = forms.CharField(label="رمز عبور",max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'رمز عبور خود را وارد کنید'}
    ))
    email = forms.CharField(label="ایمیل",max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control','placeholder': 'ایمیل خود را وارد کنید'}
    ))

    class Meta:
        model = ProfileModel
        fields = ['phone', 'nid', 'birthdate']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'شماره تماس خود را وارد کنید'})
        self.fields['nid'].widget.attrs.update({'class': 'form-control', 'placeholder': 'کد ملی خود را وارد کنید'})
        self.fields['birthdate'].widget.attrs.update({'class': 'form-control', 'placeholder': 'تاریخ تولد خود را وارد کنید'})

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^09\d{9}$', phone):
            raise forms.ValidationError('شماره تماس را به درستی وارد کنید (با قالب 09xxxxxxxxx)')
        return phone


class LoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری",max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'نام کاربری خود را وارد کنید'}
    ))
    # email = forms.EmailField(label="ایمیل",max_length=100, widget=forms.EmailInput(
    #     attrs={'class': 'form-control','placeholder': 'ایمیل خود را وارد کنید'}
    # ))
    password = forms.CharField(label="رمز عبور",max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control','placeholder': 'رمز عبور خود را وارد کنید'}
    ))

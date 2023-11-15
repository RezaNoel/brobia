from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import CustomPasswordResetForm,CustomSetPasswordForm


urlpatterns = [
    path('login', views.LoginView,name='login'),
    path('logout', views.LogoutView,name='logout'),
    path('register', views.RegisterView,name='register'),
    path('profile', views.UserProfileView,name='profile'),
    path('hotel-panel/<str:page>', views.HotelAdminView, name='hotel-panel'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        success_url='/password_reset/done/',
        form_class=CustomPasswordResetForm
    ), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url='/reset/complete/',
        form_class=CustomSetPasswordForm
    ), name='password_reset_confirm'),
    path('reset/complete/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
]
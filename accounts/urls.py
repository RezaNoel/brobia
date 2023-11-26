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
    path('kave', views.kave_negar_token_send,name='sms'),
    path('hotel-panel/<str:page>', views.HotelAdminView, name='hotel-panel'),
    path('hotel-panel/<str:page>/<slug:room_slug>', views.RoomSingleView, name='room-single'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(
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
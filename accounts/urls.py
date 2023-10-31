from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView


urlpatterns = [
    path('login', views.LoginView,name='login'),
    path('logout', views.LogoutView,name='logout'),
    path('register', views.RegisterView,name='register'),
    path('profile', views.UserProfileView,name='profile'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('forgot-password', views.ForgotPasswordView,name='forgot_password'),
    # path('change-password', views.ChangePasswordView,name='change_password'),
    # path('sgPHbLsZYSFAuYEMIdPmwV', views.CheckPhoneView,name='check-phone-correct'),
]
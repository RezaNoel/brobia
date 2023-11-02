from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView,name='login'),
    path('logout', views.LogoutView,name='logout'),
    path('register', views.RegisterView,name='register'),
    path('profile', views.UserProfileView,name='profile'),
    path('forgot-password', views.ForgotPasswordView,name='forgot_password'),
    path('change-password', views.ChangePasswordView,name='change_password'),
    path('successful-link', views.SuccessfulLinkView,name='successful_link'),
    path('successful-change', views.SuccessfulChangeView,name='successful_change'),
]
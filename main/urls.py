from django.urls import path
from . import views

urlpatterns = [
    path('about-us', views.about, name='about-us'),
    path('contact-us', views.contact, name='contact-us'),
]

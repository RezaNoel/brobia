from django.urls import path
from . import views

urlpatterns = [

    path('<slug:city_slug>', views.list,name='hotel-list'),

]

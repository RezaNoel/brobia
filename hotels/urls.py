from django.urls import path
from . import views

urlpatterns = [

    path('<slug:city_slug>', views.list,name='hotel-list'),
    path('<str:reserve>/informations', views.booking, name='hotel-booking'),
    path('<slug:city_slug>/<slug:hotel_slug>', views.single, name='hotel-single'),
    path('<str:reserve>/confirm', views.check, name='hotel-check'),
    path('<slug:confirm_city_slug>/<slug:hotel_slug>/<slug:room_slug>/<str:reserve_confirm>', views.confirm,
         name='hotel-confirm'),

    path('rV7mGkP8fFv6zLjYtNq2/<str:reserve_confirm>/', views.check_reservation_status,
         name='check-reservation-status'),

]

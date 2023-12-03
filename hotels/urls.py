from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.HotelHomeView, name='home'),
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify, name='verify'),
    path('voucher', views.HotelVoucherView, name='voucher'),
    path('rL7mikP8JFv66LjYtNq2/<int:pk>',views.HotelLikeEndPoint,name='likepk'),
    path('bankpage/<str:reserve>',views.BankPaymentEndPoint,name='bankpayment'),
    path('<str:reserve>/informations', views.HotelBookingView, name='hotel-booking'),
    path('<str:reserve>/confirm', views.RequestCheckView, name='hotel-check'),
    path('<slug:confirm_city_slug>/<slug:hotel_slug>/<slug:room_slug>/<str:reserve_confirm>?v=profile', views.ShowRequestConfirm,
         name='show-hotel-confirm'),
    path('<slug:confirm_city_slug>/<slug:hotel_slug>/<slug:room_slug>/<str:reserve_confirm>', views.RequestConfirmView,
         name='hotel-confirm'),
    path('<slug:confirm_city_slug>/<slug:hotel_slug>/<slug:room_slug>/<str:reserve_confirm>/online', views.OnlineReserveView,
         name='hotel-confirm-online'),
    path('rV7mGkP8fFv6zLjYtNq2/<str:reserve_confirm>/', views.CheckReservationStatusEndPoint,
         name='check-reservation-status'),
    path('<slug:city_slug>', views.HotelListView,name='hotel-list'),
    path('<slug:city_slug>/<slug:hotel_slug>', views.HotelSingleView, name='hotel-single'),
]

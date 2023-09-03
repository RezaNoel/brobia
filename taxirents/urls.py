from django.urls import path
from . import views

urlpatterns = [

    path('taxi',views.home,name='taxi-home'),

]

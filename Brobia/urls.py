"""
URL configuration for Aramesh_Parvaz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
# from user.serializer import UserViewSet
# from product.serializer import ProductViewSet
# from product.views import index
from main import views

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login', views.login,name='login'),
    path('<slug:city_slug>', views.list,name='hotel-list'),
    path('<slug:city_slug>/<slug:hotel_slug>', views.single,name='hotel-single'),
    path('<slug:city_slug>/<slug:hotel_slug>/<slug:room_slug>', views.booking,name='hotel-booking'),
    path('confirm/', views.confirm,name='hotel-confirm'),
    # path('home',index),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
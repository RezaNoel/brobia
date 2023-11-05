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


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
handler404 = 'main.views.custom_404'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),
    path('', include('blogs.urls')),
    path('', include('main.urls')),
    path('', include('hotels.urls')),
    path('', include('taxirents.urls')),


    # path('home',index),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

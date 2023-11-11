from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView,name='blog-list'),
]

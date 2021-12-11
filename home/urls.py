from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
]
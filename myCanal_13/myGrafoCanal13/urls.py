from django.contrib import admin
from django.urls import path,include
from .views import index,login,logout_vista,registro

urlpatterns = [
    path('', login, name='LOGIN'),
    path('logout_vista',logout_vista,name='LOGOUT'),
    path('panel/',index,name='INDEX'),
    path('registro/',registro,name='REG'),
]

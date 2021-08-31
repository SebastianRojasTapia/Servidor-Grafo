from django.contrib import admin
from django.urls import path,include
from .views import index,login,logout_vista,carga,red,panel

urlpatterns = [
    path('', login, name='LOGIN'),
    path('index/',index,name='INDEX'),
    path('logout_vista',logout_vista,name='LOGOUT'),
    path('cargar-CSV/',carga,name='C'),
    path('red/',red,name='R'),
    path('panel/',panel,name='P'),
]

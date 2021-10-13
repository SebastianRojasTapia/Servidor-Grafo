from django.contrib import admin
from django.urls import path,include
from .views import index,login,logout_vista,carga,red,panel,panelFacebook,panelTwitter,panelInstagram
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login, name='LOGIN'),
    path('Index/',index,name='INDEX'),
    path('Logout_vista',logout_vista,name='LOGOUT'),
    path('Cargar-CSV/',carga,name='C'),
    path('Red/',red,name='R'),
    path('Panel-General/',panel,name='P'),
    path('Panel-Facebook/',panelFacebook,name='PF'),
    path('Panel-Instagram/',panelInstagram,name='PI'),
    path('Panel-Twitter/',panelTwitter,name='PT'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
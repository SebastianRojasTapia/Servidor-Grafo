from django.contrib import admin
from django.urls import path,include
from .views import index,login,logout_vista,carga,red,panel
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login, name='LOGIN'),
    path('index/',index,name='INDEX'),
    path('logout_vista',logout_vista,name='LOGOUT'),
    path('cargar-CSV/',carga,name='C'),
    path('red/',red,name='R'),
    path('panel/',panel,name='P'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
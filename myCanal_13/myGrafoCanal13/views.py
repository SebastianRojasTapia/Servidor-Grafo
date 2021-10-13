from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.models import User
# adjuntamos la libreria de autenticar 
from django.contrib.auth import authenticate,logout,login as login_autent
#agregar decorador para impedir el ingreso a las paginas sin estar registrado
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.storage import FileSystemStorage
from .functions import *
from .queries import *
import pyodbc
import tweepy
import json
from sentiment_analysis_spanish import sentiment_analysis

from .key import *

def logout_vista(request):
    logout(request)
    return render(request,'web/login.html')

def login(request):
    if request.POST:
        user = request.POST.get("user")
        password = request.POST.get("pass")
        us = authenticate(request,username=user,password=password)
        if us is not None and us.is_active:
            login_autent(request,us)
            return render(request,'web/index.html',{'user':us})
        else:
            return render(request,'web/login.html',{'msg':'Usuario o contraseña incorrecta'})
    return render(request,'web/login.html')

@login_required(login_url='/login/')
def index(request):
    return render(request,'web/index.html')

@login_required(login_url='/login/')
def carga(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        print('C:\\Users\\sebas\\Downloads\\Servidor Grafo\\myCanal_13\\media\\{0}'.format(uploaded_file.name))
        if (uploaded_file.name == "LI_concatenado.csv"):
            print('\n--- CARGA DE LISTENING INSIGHTS ---\n')
            df = cleanListeningInsights(r'C:\Users\sebas\Downloads\Servidor Grafo\myCanal_13\media\{0}'.format(uploaded_file))
            print(cargarData(df, file_type='listeningInsights'))
        if (uploaded_file.name == "post_performance.csv"):
            print('\n--- CARGA DE POST PERFORMANCE ---\n')
            df_2 = cleanPostPerformance(r'C:\Users\sebas\Downloads\Servidor Grafo\myCanal_13\media\{0}'.format(uploaded_file))
            print(cargarData(df_2, file_type = 'postPerformance'))
    return render(request,'web/carga.html')

@login_required(login_url='/login/')
def red(request):
    return render(request,'web/red.html')

@login_required(login_url='/login/')
def panel(request):
    return render(request,'web/panel.html')

@login_required(login_url='/login/')
def panelFacebook(request):
    data = Grafico_engagement_date().get_data('facebook')
    print(data)
    return render(request,'web/panelFacebook.html',  {"my_data": data})

@login_required(login_url='/login/')
def panelInstagram(request):
    return render(request,'web/panelInstagram.html')

@login_required(login_url='/login/')
def panelTwitter(request):
    return render(request,'web/panelTwitter.html')


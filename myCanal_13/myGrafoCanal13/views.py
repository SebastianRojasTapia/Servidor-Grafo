from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.models import User
# adjuntamos la libreria de autenticar 
from django.contrib.auth import authenticate,logout,login as login_autent
#agregar decorador para impedir el ingreso a las paginas sin estar registrado
from django.contrib.auth.decorators import login_required, permission_required

import tweepy
import json
from sentiment_analysis_spanish import sentiment_analysis

from .key import *

sentiment = sentiment_analysis.SentimentAnalysisSpanish()

# Create your views here.

class TweetsListener(tweepy.StreamListener):
    def on_connect(self):
      print ("Estoy Conectado!")
    
    def on_status(self,status):
      print (status.created_at,status.text,status.source)

    def on_error(self,status_code):
      print ("Error", status_code)



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
    return render(request,'web/carga.html')

@login_required(login_url='/login/')
def red(request):
    return render(request,'web/red.html')

@login_required(login_url='/login/')
def panel(request):
    
    if request.POST:
        auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
        stream = TweetsListener()
        streamingApi=tweepy.Stream(auth=api.auth,listener=stream)
        streamingApi.filter(
            locations=[-82.894652146,-56.1959888356,-64.2317965251,13.5111203983],
            track = {'T13','13','Chile'}),
            
        data={
            'tweest':stream}
        return render(request,'web/panel.html',data)
    return render(request,'web/panel.html')


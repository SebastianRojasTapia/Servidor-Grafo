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

class MaxListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        self.process_data(raw_data)
        return True

    def process_data(self, raw_data):
        
        global sentiment
        # text -> diccionario
        tweet = json.loads(raw_data) 
        print(tweet)
        sent = sentiment.sentiment(tweet['text'])
        tweet_exportable = json.dumps(tweet, ensure_ascii=False).encode('utf8').decode()

    def on_error(self, status_code):
        if status_code == 420:
            #retorna falso en on_data desconecta el vivo
            return False
#se crea el vivo
class MaxStream():
    
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)
        
    def start(self, keyword_list):
        self.stream.filter(track=keyword_list)

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
        sentiment = sentiment_analysis.SentimentAnalysisSpanish()
        #comienza vivo
        listener = MaxListener()

        auth = tweepy.OAuthHandler(c_k,c_s)
        auth.set_access_token(a_t,a_t_s)

        stream = MaxStream(auth, listener)
        stream.start(['T13', 't13'])
        return render(request,'web/panel.html')
    return render(request,'web/panel.html')


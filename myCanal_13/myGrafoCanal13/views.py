from django.shortcuts import render
from django.contrib.auth.models import User
# adjuntamos la libreria de autenticar 
from django.contrib.auth import authenticate,logout,login as login_autent
#agregar decorador para impedir el ingreso a las paginas sin estar registrado
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


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

def registro(request):
    if request.method == 'POST':
        userC = request.POST.get('newuser')
        emailC = request.POST.get('newemail')
        passC = request.POST.get('newpass')
        
        try:
            u = User.objects.get(email=correo)
            data['mensaje'] = 'Correo ya ingresado'
            u = User.objects.get(username=usuario)
            data['mensaje'] = 'Usuario ya ingresado'
            return render(request,'web/login.html',data)
        except:
            u = User()
            u.username = userC
            u.email=emailC
            u.set_password(passC)
            u.save()
            data['mensaje'] = 'Agregado correctamente'
        else:
            data['mensaje'] = 'No se ha podido guardar'
        return render(request,'web/login.html',data)
    return render(request,'web/login.html',data)
    

def logout_vista(request):
    logout(request)
    return render(request,'web/login.html')

@login_required(login_url='/login/')
def index(request):
    return render(request,'web/index.html')


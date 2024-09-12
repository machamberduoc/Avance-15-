from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')  
        else:
            messages.error(request, 'Error al crear el usuario. Por favor, revisa los datos e intenta de nuevo.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f'Username: {username}, Password: {password}')  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('welcome')
            else:
                messages.error(request, 'Credenciales incorrectas. Inténtelo de nuevo.')
        else:
            messages.error(request, 'Formulario inválido. Por favor, revise los campos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return redirect('login') 

def logout_view(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente')
    return redirect('login')  

def welcome(request):
    return render(request, 'welcome.html')  

def menu(request):
    return render(request, 'menu.html')

def inicio(request):
    return render(request, 'inicio.html')

def monitoreo(request):
    return render(request, 'monitoreo.html')

from django.http import JsonResponse
from .models import Monitor  

def obtener_datos_monitor(request):
    # Consulta todos los datos del modelo Monitor
    datos = Monitor.objects.all().values('id', 'serverm', 'standartm', 'disknamem', 'totalsizem','freemegabytesm')
    # Devuelve los datos en formato JSON
    return JsonResponse(list(datos), safe=False)

def analisispredictivo(request):
    return render(request, 'analisispredictivo.html')

def auditoria(request):
    return render(request, 'auditoria.html')

def analisisdedatos(request):
    return render(request, 'analisisdedatos.html')

def recomendaciones(request):
    return render(request, 'recomendaciones.html')




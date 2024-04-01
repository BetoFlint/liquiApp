from django.shortcuts import render
from django.http import HttpResponse
from main.models.usuario import Usuario
from main.functions import apiObtenerParidad
import requests
# Create your views here.
def index(request):
    return HttpResponse("Hola po choro")

def home(request):
    paridad, valor = apiObtenerParidad('dolar', '13-03-2024')
        # Renderizar una plantilla con los datos
    return render(request, "home.html", { 'data': paridad, 'valor':valor}) 

def signup(request):
    return render(request, "signup.html")

def forgotview(request):
    return render(request, "forgot.html")

def inicioview(request):
    return render(request, "inicio.html")



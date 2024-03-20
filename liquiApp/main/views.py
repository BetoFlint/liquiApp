from django.shortcuts import render
from django.http import HttpResponse
from main.models import Usuario, Gente
import requests
# Create your views here.
def index(request):
    return HttpResponse("Hola po choro")

def home(request):
    gente = Gente.objects.all()
    response = requests.get('https://mindicador.cl/api/uf/13-03-2024')
#    if response.status_code == 200:
        # Procesar los datos recibidos
    datas = response.json()
    data = datas['nombre']
    valor= datas['serie'][0]['valor']
   
        # Renderizar una plantilla con los datos
    return render(request, "home.html", { "gente": gente , 'data': data, 'valor':valor}) 

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def forgot(request):
    return render(request, "forgot.html")

def liquidacion(request):
    return render(request, "liquidacion.html")# Create your views here.

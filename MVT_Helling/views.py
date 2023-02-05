from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def inicio(request):
    return HttpResponse("Bienvenidos a Planificación de Vuelos AEP") 

def about_us(request):
    return render(request, 'about_us.html', context={})



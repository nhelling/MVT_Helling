from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def inicio(request):
    return HttpResponse("Bienvenidos a Planificación de Vuelos AEP") 


#en vez de base va programacion o para probar base
def programaciones(request):
    return render(request, 'base.html', context={})
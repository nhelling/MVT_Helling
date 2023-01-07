from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def inicio(request):
    return HttpResponse("Inicio Programaciones") 

def programaciones(request):
    return render(request, 'programacion.html', context={})
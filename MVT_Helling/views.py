from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def inicio_programaciones(request):
    return HttpResponse("Inicio Programaciones") 

def fecha_actual(request):
    hoy = datetime.now()
    return HttpResponse(f'La fecha actual es: {hoy}')

def aeropuerto(request, apto):
    return HttpResponse(f'El aeropuerto ingresado es: {apto}')

def programaciones(request):
    return render(request, 'programacion.html', context={})
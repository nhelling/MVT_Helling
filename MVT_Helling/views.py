from django.http import HttpResponse
from django.shortcuts import render
from initial.models import Initial

def list_initial(request):
    return render(request, 'index.html', context={})

def inicio(request):
    return HttpResponse("Bienvenidos a Planificación de Vuelos AEP") 

def about_us(request):
    return render(request, 'about_us.html', context={})

def index(request):
    all_initial = Initial.objects.all()
    print(all_initial)
    context = {
        'initials':all_initial,        
    }
    return render(request, 'index.html', context=context)


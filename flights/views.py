from django.shortcuts import render
from django.http import HttpResponse
from flights.models import Fligths

from flights.forms import FlightForm

def create_fligth(request):
    if request.method == 'GET':
        context = {
            'form' : FlightForm()
        }
        return render(request, 'create_flight.html', context = context)
    
    elif request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            Fligths.objects.create(aeropuerto = form.cleaned_data['aeropuerto'],
                tipo=form.cleaned_data['tipo'],
                cia_vuelo = form.cleaned_data['cia_vuelo'],
                acft = form.cleaned_data['acft'],
                fecha_hora = form.cleaned_data['fecha_hora'],
                ruta = form.cleaned_data['ruta'],
                observacion = form.cleaned_data['observacion'],
                clase = form.cleaned_data['clase'],
                cia = form.cleaned_data['cia'],
                pax = form.cleaned_data['pax'],
            )   
            context = {
                'message': 'Vuelo creado exitosamente'
            }
            return render(request, 'create_flight.html', context = context)       
        else:
            context = {
                'form_errors':form.errors,
                'form': FlightForm()
            }   
            return render(request, 'create_flight.html', context = context)
        

def list_fligths(request):
    if 'search' in request.GET:
        search = request.GET['search']
        flights = Fligths.objects.filter(cia_vuelo__contains = search)
    else:
        flights = Fligths.objects.all()    
    #print(all_flights)
    context = {
        'flights':flights,
    }
    return render(request, 'list_fligths.html', context=context)

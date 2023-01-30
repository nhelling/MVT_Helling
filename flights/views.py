from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView

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
        else:
            context = {
                'form_errors':form.errors,
                'form': FlightForm()
            }   
        return render(request, 'create_flight.html', context = context)
        
class FlightCreateView(CreateView):
    model = Fligths
    template_name = 'create_flight.html'
    fields = '__all__'
    success_url = '/flights/list_fligths/'

def list_fligths(request):
    if 'search' in request.GET:
        search = request.GET['search']
        flights = Fligths.objects.filter(cia_vuelo__contains = search)
    else:
        flights = Fligths.objects.all()    
    
    context = {
        'flights':flights,
    }
    return render(request, 'list_fligths.html', context=context)

class FlightsListView(ListView):
    model = Fligths
    template_name = 'list_fligths.html'
    


def update_flight(request,pk):
    flight = Fligths.objects.get(id=pk)
    
    if request.method == 'GET':
        context = {
            'form' : FlightForm(                
                initial={
                    'aeropuerto': flight.aeropuerto,
                    'tipo': flight.tipo,
                    'cia_vuelo': flight.cia_vuelo,
                    'acft': flight.acft,
                    'fecha_hora': flight.fecha_hora,
                    'ruta': flight.ruta,
                    'observacion': flight.observacion,
                    'clase': flight.clase,
                    'cia': flight.cia,
                    'pax': flight.pax,                    
                }
            )
        }
        return render(request, 'update_flight.html', context = context)
    
    elif request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():            
            flight.aeropuerto = form.cleaned_data['aeropuerto'],
            flight.tipo = form.cleaned_data['tipo'],
            flight.cia_vuelo = form.cleaned_data['cia_vuelo'],
            flight.acft = form.cleaned_data['acft'],
            flight.fecha_hora = form.cleaned_data['fecha_hora'],
            flight.ruta = form.cleaned_data['ruta'],
            flight.observacion = form.cleaned_data['observacion'],
            flight.clase = form.cleaned_data['clase'],
            flight.cia = form.cleaned_data['cia'],
            flight.pax = form.cleaned_data['pax']
            flight.save()  
            context = {
                'message': 'Vuelo actualizado exitosamente'
            }             
        else:
            context = {
                'form_errors':form.errors,
                'form': FlightForm()
            }   
        return render(request, 'update_flight.html', context = context)
    

class FlightDeleteView(DeleteView):
    model = Fligths
    template_name = 'delete_flight.html'
    success_url = '/flights/list_fligths/'
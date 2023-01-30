from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DeleteView

from fleet.models import Fleet
from fleet.forms import FleetForm

def create_fleet(request):
    if request.method == 'GET':
        context = {
            'form' : FleetForm()
        }
        return render(request, 'create_fleet.html', context = context)    
    elif request.method == 'POST':
        form = FleetForm(request.POST)
        if form.is_valid():
            Fleet.objects.create(aircraft= form.cleaned_data['aircraft'],
                iata_code =form.cleaned_data['iata_code'], 
                seats = form.cleaned_data['seats'],               
                
            )
            context = {
                'message': 'Aeronave creada exitosamente'
            }        
            
        else:
            context = {
                'form_errors':form.errors,
                'form': FleetForm()
            }   
        return render(request, 'create_fleet.html', context = context)


def list_fleet(request):
    all_fleet = Fleet.objects.all()
    print(all_fleet)
    context = {
        'fleets':all_fleet,        
    }
    return render(request, 'list_fleet.html', context=context)


def update_fleet(request,pk):
    fleet = Fleet.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form' : FleetForm(
                initial={
                    'aircraft': fleet.aircraft,
                    'iata_code':fleet.iata_code,
                    'seats':fleet.seats ,                   
                }                
            )
        }
        return render(request, 'update_fleet.html', context = context)   
     
    elif request.method == 'POST':
        form = FleetForm(request.POST)
        if form.is_valid():
            fleet.aircraft= form.cleaned_data['aircraft'],
            fleet.iata_code =form.cleaned_data['iata_code'], 
            fleet.seats = form.cleaned_data['seats']               
            fleet.save()    
            
            context = {
                'message': 'Aeronave creada exitosamente'
            }        
            
        else:
            context = {
                'form_errors':form.errors,
                'form': FleetForm()
            }   
        return render(request, 'update_fleet.html', context = context)

class FleetDeleteView(DeleteView):
    model = Fleet
    template_name = 'delete_fleet.html'
    success_url = '/fleet/list_fleets/'












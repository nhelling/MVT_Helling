from django.shortcuts import render
from django.http import HttpResponse
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
            return render(request, 'create_fleet.html', context = context)
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













from django.shortcuts import render
from django.http import HttpResponse
from fleet.models import Fleet

def create_fleet(request):
    new_fleet = Fleet.objects.create(aircraft="Boeing 738",iata_code="738", seats = 186 )
    return HttpResponse('Se ha cargado la nueva aeronave')


def list_fleet(request):
    all_fleet = Fleet.objects.all()
    print(all_fleet)
    context = {
        'fleets':all_fleet,        
    }
    return render(request, 'fleet.html', context=context)










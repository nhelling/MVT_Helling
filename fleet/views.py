from django.shortcuts import render
from django.http import HttpResponse
from fleet.models import Fleet

def create_fleet(request):
    if request.method == 'GET':
        return render(request, 'create_fleet.html', context = {})
    elif request.method == 'POST':
        Fleet.objects.create(aircraft = request.POST['aircraft'],iata_code = request.POST['iata_code'], seats = request.POST['seats'] )
        return render(request, 'create_fleet.html', context = {})
    
    


def list_fleet(request):
    all_fleet = Fleet.objects.all()
    print(all_fleet)
    context = {
        'fleets':all_fleet,        
    }
    return render(request, 'fleet.html', context=context)













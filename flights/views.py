from django.shortcuts import render
from django.http import HttpResponse
from flights.models import Fligths

def create_fligth(request):
    new_fligth =  Fligths.objects.create(aeropuerto='AEP', tipo='Partida',cia_vuelo='FO3114', acft='738', fecha_hora='11/12/2022 14:12:00', ruta='USH', observacion='n/a', clase='F', cia='FO', pax=147)
    print(new_fligth)
    return HttpResponse('Se ha cargado el nuevo vuelo')


def list_fligths(request):
    all_flights = Fligths.objects.all()    
    print(all_flights)
    context = {
        'flights':all_flights,
    }
    return render(request, 'list_fligths.html', context=context)

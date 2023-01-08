from django.shortcuts import render
from django.http import HttpResponse
from routes.models import Route

def create_route(request):
    new_route = Route.objects.create(route = 'Cordoba', iata_code='COR', domestico = True, internacional = False )
    print(new_route)
    return HttpResponse('Se ha cargado la nueva ruta')


def list_routes(request):
    all_routes = Route.objects.all()    
    print(all_routes)
    context = {
        'routes':all_routes,
    }
    return render(request, 'routes.html', context=context)
    


    
    




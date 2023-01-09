from django.shortcuts import render
from django.http import HttpResponse
from routes.models import Route

from routes.forms import RouteForm

def create_route(request):
    if request.method == 'GET':
        context = {
            'form' : RouteForm()
        }
        return render(request, 'create_route.html', context = context)    
    elif request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            Route.objects.create(route= form.cleaned_data['route'],
                iata_code =form.cleaned_data['iata_code'], 
                domestico = form.cleaned_data['domestico'], 
                internacional = form.cleaned_data['internacional'],              
                
            )
            context = {
                'message': 'Ruta creada exitosamente'
            }        
            return render(request, 'create_route.html', context = context)
        else:
            context = {
                'form_errors':form.errors,
                'form': RouteForm()
            }   
            return render(request, 'create_route.html', context = context)
    
def list_routes(request):
    all_routes = Route.objects.all()    
    print(all_routes)
    context = {
        'routes':all_routes,
    }
    return render(request, 'list_routes.html', context=context)
    


    
    




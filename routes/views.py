from django.shortcuts import render
from django.views.generic import  DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
            Route.objects.create(
                route_image = form.cleaned_data['route_image'],
                route= form.cleaned_data['route'],
                iata_code =form.cleaned_data['iata_code'], 
                domestico = form.cleaned_data['domestico'], 
                internacional = form.cleaned_data['internacional'],              
                
            )
            context = {
                'message': 'Ruta creada exitosamente'
            }        
            
        else:
            context = {
                'form_errors':form.errors,
                'form': RouteForm()
            }   
        return render(request, 'create_route.html', context = context)

@login_required
def list_routes(request):
    all_routes = Route.objects.all()    
    print(all_routes)
    context = {
        'routes':all_routes,
    }
    return render(request, 'list_routes.html', context=context)

@login_required
def update_route(request, pk):
    route = Route.objects.get(id=pk)    
    if request.method == 'GET':
        context = {
            'form' : RouteForm(
                initial={
                'route_image':route.route_image,
                'route': route.route,
                'iata_code': route.iata_code ,
                'domestico': route.domestico , 
                'internacional': route.internacional ,
                }                
            )
        }
        return render(request, 'update_route.html', context = context)    
    
    elif request.method == 'POST':
        form = RouteForm(request.POST,request.FILES)
        if form.is_valid():
            route.route_image = form.cleaned_data['route_image']
            route.route= form.cleaned_data['route']
            route.iata_code =form.cleaned_data['iata_code']
            route.domestico = form.cleaned_data['domestico']
            route.internacional = form.cleaned_data['internacional']          
            route.save()    
            
            context = {
                'message': 'Ruta actualizada exitosamente'
            }        
            
        else:
            context = {
                'form_errors':form.errors,
                'form': RouteForm()
            }   
        return render(request, 'update_route.html', context = context)

class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    template_name = 'delete_route.html'
    success_url = '/routes/list_routes/'   
    




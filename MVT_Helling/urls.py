from django.contrib import admin
from django.urls import path, include
from MVT_Helling.views import inicio, index


urlpatterns = [
    path('',index, name = 'index'),
    path('admin/', admin.site.urls),
    path('Inicio/',inicio),
    
    
    
    #path ('fleet/', include ('fleet.url')),
    path('flights/', include('flights.url')),
    #path('routes/', include('routes.url')),
    
]

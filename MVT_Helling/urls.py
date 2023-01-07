from django.contrib import admin
from django.urls import path, include
from MVT_Helling.views import inicio,programaciones


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inicio/',inicio),
    
    path('programaciones/', programaciones),
    
    #path ('fleet/', include ('fleet.url')),
    path('flights/', include('flights.url')),
    #path('routes/', include('routes.url')),
    
]

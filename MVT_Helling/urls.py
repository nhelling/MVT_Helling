from django.contrib import admin
from django.urls import path
from MVT_Helling.views import inicio_programaciones,fecha_actual,aeropuerto,programaciones
from flights.views import create_fligth, list_fligths

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inicio/',inicio_programaciones),
    path('fecha/',fecha_actual),
    path('aeropuerto/<str:apto>/',aeropuerto ),
    path('programaciones/', programaciones),
    
    
    path('new_fligth/', create_fligth),
    path('list_fligths/', list_fligths),
]

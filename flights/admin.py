from django.contrib import admin

from flights.models import Fligths

@admin.register(Fligths)

class FlightAdmin(admin.ModelAdmin):
    list_display = ('aeropuerto', 'tipo', 'cia_vuelo', 'acft', 'fecha_hora','ruta', 'clase', 'cia', 'pax' )
    list_filter = ( 'tipo',  'acft','ruta' )
    search_fields = ('cia_vuelo', )
    
    
  




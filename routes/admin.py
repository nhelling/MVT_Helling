from django.contrib import admin

from routes.models import Route

@admin.register(Route)

class FlightAdmin(admin.ModelAdmin):
    list_display = ('route', 'iata_code', 'domestico', 'internacional')
    list_filter = ('iata_code',)
    search_fields = ('iata_code', )
    
    
   

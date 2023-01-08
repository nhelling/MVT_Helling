from django.contrib import admin

from fleet.models import Fleet

@admin.register(Fleet)

class FleetAdmin(admin.ModelAdmin):
    list_display = ('aircraft', 'iata_code', 'seats')
    list_filter = ( 'iata_code', )
    search_fields = ( 'iata_code', 'seats')






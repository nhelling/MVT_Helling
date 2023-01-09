from django.urls import path
from fleet.views import create_fleet, list_fleet

urlpatterns = [
    path('create_fleet/', create_fleet),
    path('list_fleets/', list_fleet),
    
]




from django.urls import path
from fleet.views import create_fleet, list_fleet, update_fleet, FleetDeleteView, FleetListView

urlpatterns = [
    path('create_fleet/', create_fleet),
    path('list_fleets/', list_fleet),
    path('update_fleet/<int:pk>/',update_fleet),
    path('delete_fleet/<int:pk>/',FleetDeleteView.as_view()),
]




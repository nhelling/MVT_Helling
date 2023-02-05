from django.urls import path
from flights.views import create_fligth,update_flight,FlightsListView,FlightCreateView, FlightDeleteView


urlpatterns = [
    path('create_fligth/',create_fligth),
    path('list_fligths/',FlightsListView.as_view()),
    path('update_flight/<int:pk>/',update_flight),
    path('delete_flight/<int:pk>/',FlightDeleteView.as_view()),
]
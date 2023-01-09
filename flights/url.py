from django.urls import path
from flights.views import create_fligth, list_fligths


urlpatterns = [
    path('create_fligth/',create_fligth),
    path('list_fligths/',list_fligths),
    
]
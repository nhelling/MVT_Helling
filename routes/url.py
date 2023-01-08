from django.urls import path
from routes.views import create_route, list_routes

urlpatterns = [
    path('new_route/', create_route),
    path('list_routes/', list_routes),
    
]


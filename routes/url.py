from django.urls import path
from routes import create_route, list_routes

urlpatterns = [
    path('new_route/', create_route),
    path('list_routes/', list_routes),
    
]

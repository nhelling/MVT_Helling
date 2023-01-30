from django.urls import path
from routes.views import create_route, list_routes, update_route, RouteDeleteView

urlpatterns = [
    path('create_route/', create_route),
    path('list_routes/', list_routes),
    path('update_routes/<int:pk>/',update_route),
    path('delete_route/<int:pk>/',RouteDeleteView.as_view()),
    
]


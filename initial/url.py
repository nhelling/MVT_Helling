from django.urls import path
from initial.views import imagen_inicio

urlpatterns = [
    path('index/', imagen_inicio),
    
]

from django.shortcuts import render
from initial.models import Initial


def imagen_inicio(request):
    imagen = Initial.initial_image
    return render(request, 'index.html', imagen)

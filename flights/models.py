from django.db import models
from datetime import datetime


class Fligths(models.Model):
    aeropuerto = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)
    cia_vuelo = models.CharField(max_length=10)
    acft = models.CharField(max_length=10)
    fecha_hora = models.CharField(max_length=40)
    ruta = models.CharField(max_length=3)
    observacion = models.CharField(max_length=100)
    clase = models.CharField(max_length=10)
    cia = models.CharField(max_length=2)
    pax = models.IntegerField()


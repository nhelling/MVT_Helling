from django.db import models
from datetime import datetime


class Fligths(models.Model):
    aeropuerto = models.CharField(max_length=50, verbose_name= 'APTO')
    tipo = models.CharField(max_length=10, verbose_name= 'Tipo')
    cia_vuelo = models.CharField(max_length=10, verbose_name= 'CIA-Nro. Vuelo')
    acft = models.CharField(max_length=10, verbose_name= 'ACFT')
    fecha_hora = models.CharField(max_length=40, verbose_name= 'Fecha - Hora')
    ruta = models.CharField(max_length=3, verbose_name= 'Ruta')
    observacion = models.CharField(max_length=100, verbose_name= 'Obs.')
    clase = models.CharField(max_length=10, verbose_name= 'Clase')
    cia = models.CharField(max_length=2,verbose_name= 'Cia')
    pax = models.IntegerField(verbose_name='Cant. PAX')
    
    def __str__(self):
        return self.cia_vuelo
    
    class Meta:
        verbose_name = 'Vuelo'
        verbose_name_plural = 'Vuelos'


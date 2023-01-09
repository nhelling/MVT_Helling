from django.db import models

class Route(models.Model):
    route = models.CharField(max_length=50, verbose_name='Ruta')
    iata_code = models.CharField(max_length=3, verbose_name='Codigo IATA')
    domestico = models.BooleanField(verbose_name='Domestico', default= True)
    internacional = models.BooleanField(verbose_name='Internacional', default= False)
    
    def __str__(self):
        return self.route
    
    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
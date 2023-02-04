from django.db import models

class Fleet(models.Model):
    acft_image = models.ImageField(upload_to= 'profile_images',null= True, blank= True)
    aircraft = models.CharField(max_length=50, verbose_name= 'Aeronave')
    iata_code = models.CharField(max_length=3, verbose_name= 'Codigo IATA')
    seats = models.IntegerField(verbose_name= 'Capacidad')
    
    def __str__(self):
        return self.aircraft
    
    class Meta:
        verbose_name = 'Flota'
        verbose_name_plural = 'Aeronaves'
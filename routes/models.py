from django.db import models

class Route(models.Model):
    route = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=3)
    nature = models.BooleanField()
    

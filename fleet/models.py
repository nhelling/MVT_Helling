from django.db import models

class Fleet(models.Model):
    aircraft = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=3)
    seats = models.IntegerField()
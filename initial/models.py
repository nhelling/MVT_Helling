from django.db import models

class Initial(models.Model):
    initial_image = models.ImageField(upload_to= 'profile_images',null= True, blank= True)

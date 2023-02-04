from django import forms  
from .models import Fleet

class FleetForm(forms.Form):
    acft_image = forms.ImageField(required=False, label='Foto Acft.')
    aircraft = forms.CharField(max_length=50)
    iata_code = forms.CharField(max_length=3)
    seats = forms.IntegerField()
    
    class Meta:
        model = Fleet
        fields = ['acft_image', 'aircraft','iata_code','seats']
    
 
        





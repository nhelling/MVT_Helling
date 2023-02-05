from django import forms  
from .models import Fligths

class FlightForm(forms.Form):
    flight_image = forms.ImageField(required=False, label='Foto Vuelo.')
    aeropuerto = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=10)
    cia_vuelo = forms.CharField(max_length=10)
    acft = forms.CharField(max_length=10)
    fecha_hora = forms.CharField(max_length=40)
    ruta = forms.CharField(max_length=3)
    observacion = forms.CharField(max_length=100)
    clase = forms.CharField(max_length=10)
    cia = forms.CharField(max_length=2)
    pax = forms.IntegerField()
    
    class Meta:
        model = Fligths
        fields = ['apto_image', 'aeropuerto','tipo','cia_vuelo','acft','fecha_hora','ruta','observacion','clase','cia','pax']

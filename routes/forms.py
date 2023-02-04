from django import forms  
from .models import Route

class RouteForm(forms.Form):
    route_image = forms.ImageField(required=False, label='Foto Acft.')
    route = forms.CharField(max_length=50)
    iata_code = forms.CharField(max_length=3)
    domestico = forms.BooleanField(required=False)
    internacional = forms.BooleanField(required=False)
    
class Meta:
    model = Route
    fields = ['route_image', 'route', 'iata_code', 'domestico', 'internacional']
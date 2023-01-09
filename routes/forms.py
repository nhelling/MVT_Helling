from django import forms  

class RouteForm(forms.Form):
    route = forms.CharField(max_length=50)
    iata_code = forms.CharField(max_length=3)
    domestico = forms.BooleanField(required=False)
    internacional = forms.BooleanField(required=False)
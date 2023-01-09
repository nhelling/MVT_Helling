from django import forms  

class FleetForm(forms.Form):
    aircraft = forms.CharField(max_length=50)
    iata_code = forms.CharField(max_length=3)
    seats = forms.IntegerField()





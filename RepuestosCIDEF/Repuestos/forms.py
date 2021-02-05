from django.forms import *
from .models import Localidades, Comuna

class TestForm(Form):
    localidades = ModelChoiceField(
        queryset = Localidades.objects.all(), 
        widget   = Select(attrs={
        'class': 'form-control'
    }))
    
    comunas = ModelChoiceField(
        queryset  = Comuna.objects.none(), 
        widget    = Select(attrs={
        'class': 'form-control'
    }))
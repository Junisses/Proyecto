from django.forms import *
from .models import *

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
    
class FiltroForm(Form):
    marcas = ModelChoiceField(
        queryset = MarcaAuto.objects.all(), 
        widget   = Select(attrs={
        'class': 'form-control'
    }))
    
    modelos = ModelChoiceField(
        queryset  = Modelo.objects.none(), 
        widget    = Select(attrs={
        'class': 'form-control'
    }))
    

    categoria = ModelChoiceField(
        queryset  = Categoria.objects.all(), 
        widget    = Select(attrs={
        'class': 'form-control'
    }))
    
    repuestos = ModelChoiceField(
        queryset  = Repuesto.objects.none(), 
        widget    = Select(attrs={
        'class': 'form-control'
    }))
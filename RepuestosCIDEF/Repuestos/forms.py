from django.forms import *
from .models import *


class FiltroForm(Form):
    categorias    = ModelChoiceField(
        queryset  = Categoria.objects.all(), 
        widget    = Select(attrs={
        'class'   : 'form-control'
    }))
    
    repuestos     = ModelChoiceField(
        queryset  = Repuesto.objects.none(), 
        widget    = Select(attrs={
        'class'   : 'form-control'
    }))
      
    partes       = ModelChoiceField(
        queryset = Partes.objects.none(), 
        widget   = Select(attrs={
        'class'  : 'form-control'
    }))
        
    marcas       = ModelChoiceField(
        queryset = MarcaAuto.objects.none(), 
        widget   = Select(attrs={
        'class'  : 'form-control'
    }))
    
    modelos       = ModelChoiceField(
        queryset  = Modelo.objects.none(), 
        widget    = Select(attrs={
        'class'   : 'form-control'
    }))
    
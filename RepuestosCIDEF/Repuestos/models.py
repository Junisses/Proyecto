from django.db import models

#Repuestos

class Categoria(models.Model):
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Repuesto(models.Model):
    categoria        = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    nombreRepuesto   = models.TextField(max_length=60)
    codigo           = models.DecimalField(max_digits=13, decimal_places=0)
    descripcion      = models.TextField(max_length = 200)
    stock            = models.IntegerField()
    precioVenta      = models.IntegerField()

    def __str__(self):
        return self.nombreRepuesto

class Partes(models.Model):
    nombreRepuesto    = models.ForeignKey(Repuesto, blank=True, null=True, on_delete=models.SET_NULL)   
    nombre            = models.TextField(max_length=60)
    codigo            = models.DecimalField(max_digits=13, decimal_places=0)
    descripcion       = models.TextField(max_length = 200)
    stock             = models.IntegerField()
    precioVenta       = models.IntegerField()

    def __str__(self):
        return self.nombre
        
class MarcaAuto(models.Model):
    parte         = models.ForeignKey(Partes, blank=True, null=True, on_delete=models.SET_NULL)
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre
       
class Modelo(models.Model):
    marca         = models.ForeignKey(MarcaAuto, blank=True, null=True, on_delete=models.SET_NULL)
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre
        
        

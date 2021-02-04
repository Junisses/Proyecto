from django.db import models

#Repuestos
class MarcaAuto(models.Model):
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    marca         = models.ForeignKey(MarcaAuto, blank=True, null=True, on_delete=models.SET_NULL)
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Repuesto(models.Model):
    marca            = models.ForeignKey(MarcaAuto, blank=True, null=True, on_delete=models.SET_NULL)
    categoria        = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    modelo           = models.ForeignKey(Modelo, blank=True, null=True, on_delete=models.SET_NULL)
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
        
        
        
#Regiones
class Localidades(models.Model):
    id                = models.AutoField(primary_key = True)
    nombre            = models.TextField(max_length=60)

    def __str__(self):
        return '{0}'.format(self.nombre)
        
class Comuna(models.Model):
    localidad         = models.ForeignKey(Localidades, blank=True, null=True, on_delete=models.SET_NULL)
    id                = models.AutoField(primary_key = True)
    nombre            = models.TextField(max_length=60)

    def __str__(self):
        return '{0}'.format(self.nombre)
        

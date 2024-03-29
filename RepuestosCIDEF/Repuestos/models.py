from django.db import models

class Categoria(models.Model):
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    categoria     = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class MarcaAuto(models.Model):
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    marca         = models.ForeignKey(MarcaAuto, blank=True, null=True, on_delete=models.SET_NULL)
    nombre        = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre

class Repuesto(models.Model):
    categoria        = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.SET_NULL)
    marca            = models.ForeignKey(MarcaAuto, blank=True, null=True, on_delete=models.SET_NULL)
    modelo           = models.ForeignKey(Modelo, blank=True, null=True, on_delete=models.SET_NULL)
    tipo             = models.ForeignKey(Tipo, blank=True, null=True, on_delete=models.SET_NULL)
    nombreRepuesto   = models.TextField(max_length=60)
    imagen           = models.ImageField('Foto', upload_to='repuesto/', null=True, blank=True)
    codigo           = models.TextField(max_length = 60)
    descripcion      = models.TextField(max_length = 200)
    stock            = models.IntegerField()
    precioVenta      = models.IntegerField()
    

    def __str__(self):
        return self.nombreRepuesto
     
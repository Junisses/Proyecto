from django.contrib import admin
from .models import *


# Register your models here.

class marcaAutoAdmin(admin.ModelAdmin):
    list_display   = ['nombre'] 
admin.site.register(MarcaAuto, marcaAutoAdmin)

class categoriaAdmin(admin.ModelAdmin):
    list_display   = ['nombre'] 
admin.site.register(Categoria, categoriaAdmin)

class repuestoAdmin(admin.ModelAdmin):
    list_display   = ['nombreRepuesto'] 
admin.site.register(Repuesto, repuestoAdmin)

class modeloAdmin(admin.ModelAdmin):
    list_display   = ['nombre'] 
admin.site.register(Modelo, modeloAdmin)

class tipoAdmin(admin.ModelAdmin):
    list_display   = ['nombre'] 
admin.site.register(Tipo, tipoAdmin)


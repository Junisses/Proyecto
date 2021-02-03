from django.contrib import admin
from .models import MarcaAuto
from .models import Categoria
from .models import Repuesto
from .models import Modelo
from .models import Partes
from .models import Localidades
from .models import Comuna
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

class parteAdmin(admin.ModelAdmin):
    list_display   = ['nombre'] 
admin.site.register(Partes, parteAdmin)

class localidadAdmin(admin.ModelAdmin):
    list_display   = ['nombre'] 
admin.site.register(Localidades, localidadAdmin)

class comunaAdmin(admin.ModelAdmin):
    list_display   = ['nombre'] 
admin.site.register(Comuna, comunaAdmin)
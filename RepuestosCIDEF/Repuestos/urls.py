from django.urls import path, include
from . import views
#from django.conf import settings
#from django.conf.urls.static import static
#from .views import ProductoViewSet
#from rest_framework import routers

urlpatterns = [
    #Inicio de la página
    path('',views.prueba, name='prueba'),
    
    #Plantilla de pruebas
    path('tienda',views.tienda, name='tienda'),
    
    #Nivel Básico
    path('contactoRepuestos',views.contactoRepuestos, name='contactoRepuestos'),
    
    #Nivel Experto
    path('Repuestos',views.Repuestos, name='inicio'),
    
    #Inicio Repuestos
    path('inicioRepuestos',views.inicioRepuestos, name='inicioRepuestos'),
    
    #Apartado de DFM
    path('repuestosDongFeng',views.repuestosDongFeng,name='repuestosDongFeng'),
    
    #Apartado de Foton
    path('repuestosFoton',views.repuestosFoton,name='repuestosFoton'),
    
    #Pruebas
    path('probar',views.probar,name='probar'),
    
    #Busqueda
    path('busqueda',views.buscar,name='buscar'),
    
    #Páginas de DFM
    path('repuestosDongFeng/FengshenS30',views.fengshen,name='S30'),
    path('repuestosDongFeng/AX4',views.DongfengAX4,name='AX4'),
    path('repuestosDongFeng/AX7-PRO',views.DongfengAX7_PRO,name='AX7-PRO'),
]
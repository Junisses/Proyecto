from django.urls import path, include
from . import views
#from django.conf import settings
#from django.conf.urls.static import static
#from .views import ProductoViewSet
#from rest_framework import routers

urlpatterns = [
    path('',views.prueba, name='prueba'),
    path('tienda',views.tienda, name='tienda'),
    path('contactoRepuestos',views.contactoRepuestos, name='contactoRepuestos'),
    path('Repuestos',views.Repuestos, name='inicio'),
    path('inicioRepuestos',views.inicioRepuestos, name='inicioRepuestos'),
    path('repuestosDongFeng',views.repuestosDongFeng,name='repuestosDongFeng'),
    path('repuestosFoton',views.repuestosFoton,name='repuestosFoton'),
    path('probar',views.probar,name='probar'),
    path('busqueda',views.buscar,name='buscar'),
]
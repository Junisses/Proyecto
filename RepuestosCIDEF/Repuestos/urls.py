from django.urls import path, include
from . import views
#from django.conf import settings
#from django.conf.urls.static import static
#from .views import ProductoViewSet
#from rest_framework import routers


urlpatterns = [
    path('',views.prueba, name='prueba'),
    path('tienda',views.tienda, name='tienda'),
    path('repuestosDongFeng',views.repuestos, name='respuestos'),
    path('Repuestos',views.inicio, name='inicio'),
    path('inicioRepuestos',views.inicioRepuestos, name='inicioRepuestos'),
    path('repuestosAvanzados',views.repuestosAvanzados,name='repuestosAvanzados'),
]
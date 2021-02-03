from django.urls import path, include
from . import views
from django.core import *
#from django.conf import settings
#from django.conf.urls.static import static
#from .views import ProductoViewSet
#from rest_framework import routers

urlpatterns = [
    path('',views.prueba, name='prueba'),
    path('tienda',views.tienda, name='tienda'),
    path('contactoRepuestos',views.contactoRepuestos, name='contactoRepuestos'),
    path('Repuestos',views.inicio, name='inicio'),
    path('inicioRepuestos',views.inicioRepuestos, name='inicioRepuestos'),
    path('repuestosDongFeng',views.repuestosDongFeng,name='repuestosDongFeng'),
    #test
    path('test/', views.TestView.as_view(), name='test'),
]
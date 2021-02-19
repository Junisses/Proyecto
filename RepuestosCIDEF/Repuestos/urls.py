from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import ProductoViewSet
#from rest_framework import routers

urlpatterns = [
    #Inicio de la página
    path('',views.prueba, name='prueba'),
    
    #Nivel Básico
    path('contactoRepuestos', views.contactoRepuestos, name='contactoRepuestos'),
    
    #Nivel Experto
    path('Repuestos', views.Repuestos, name='inicio'),
    
    #Inicio Repuestos
    path('inicioRepuestos', views.inicioRepuestos, name='inicioRepuestos'),
    
    #Apartado de DFM
    path('repuestosDongFeng', views.repuestosDongFeng,name='repuestosDongFeng'),
    #Páginas de DFM
    path('repuestosDongFeng/FengshenS30', views.fengshen,name='S30'),
    path('repuestosDongFeng/AX4', views.AX4,name='AX4'),
    path('repuestosDongFeng/AX7-PRO', views.AX7_PRO,name='AX7-PRO'),
    path('repuestosDongFeng/NEW-AX7', views.NEW_AX7,name='NEW-AX7'),
    path('repuestosDongFeng/A60', views.A60,name='A60'),
    
    #Apartado de Foton
    path('repuestosFoton', views.repuestosFoton,name='repuestosFoton'),
    #Páginas de Foton
    path('repuestosFoton/Midi-Truck-Simple', views.Midi_Simple,name='Midi_Truck_simple'),
    path('repuestosFoton/Midi-Van', views.Midi_Van,name='Midi-Van'),
    path('repuestosFoton/Midi-Truck-Doble', views.Midi_Doble,name='Midi-Doble'),
    path('repuestosFoton/TM-Doble', views.tm_doble,name='TM-DOBLE'),
    path('repuestosFoton/TM-Simple', views.tm_simple,name='TM-Simple'),
    path('repuestosFoton/FT-500', views.ft_500,name='FT-500'),
    path('repuestosFoton/FT-CREW', views.FT_CREW,name='ft-crew'),
    path('repuestosFoton/FT-BOX', views.FT_BOX,name='ft-box'),
    path('repuestosFoton/K1', views.K1,name='k1'),

    #Pruebas
    path('probar', views.probar,name='probar'),
    
    #Busqueda
    path('busqueda', views.buscar,name='buscar'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
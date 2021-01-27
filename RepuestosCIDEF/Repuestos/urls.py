from django.urls import path, include
from . import views
#from django.conf import settings
#from django.conf.urls.static import static
#from .views import ProductoViewSet
#from rest_framework import routers


urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('tienda',views.tienda, name='tienda'),
    path('repuestos',views.repuestos, name='respuestos'),
]
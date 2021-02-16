from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from Repuestos.models import *
from django.conf import settings


#Vistas
def Repuestos(request):
    return render(request,'inicio.html', {})
        
def probar(request):
    item = {}
        
    if request.method == "POST":
        buscar = request.POST['categoria']    
        if 'categoria' in request.POST:
            item = Repuesto.objects.filter(categoria_id = buscar)

    return render(request,'Probar.html', {'item': item})

def buscar(request):
    item = {}
    
    if request.method == "POST":
        buscar = request.POST['txtBuscar']
        
        if 'txtBuscar' in request.POST:
            item = Repuesto.objects.filter(nombreRepuesto__contains = buscar)
            
           
    return render(request,'buscar.html', {'item':item}) 
    
def tienda(request):
    return render(request,'tienda.html', {})
    
def repuestos(request):
    return render(request,'repuestos.html', {})
    
def prueba(request):
    return render(request,'prueba.html', {})
    
def inicioRepuestos(request):
    return render(request,'inicioRepuestos.html', {})
    
def repuestosDongFeng(request):
    return render(request,'repuestosDongFeng.html', {})
    
def repuestosFoton(request):
    return render(request,'repuestosFoton.html', {})
    
def contactoRepuestos(request):
    if request.method== 'POST':

        subject=request.POST["Asunto"]

        message=request.POST["mensaje"]+'\n'+ "────────────────────────────────────"+'\n'+"Datos del cliente"+'\n'+ "Nombre : " + request.POST["nombre"]+ request.POST["apellidos"] +'\n'+ "Email : " + request.POST["email"]+'\n'+ "Telefono :" + request.POST["fono"]+'\n'+ "Region : " + request.POST["pais"] +'\n'+ "Comuna : " + request.POST["provincia"]+'\n'+ "────────────────────────────────────"+'\n'+ "Datos del Vehiculo"+'\n'+"Marca : " + request.POST["marca"] +'\n'+ "Modelo : " + request.POST["modelo"]+'\n'+ "N° Chasis :" + request.POST["chasis"]
 
        from_email=settings.EMAIL_HOST_USER

        recipient_list=["junissesamanda.03@gmail.com"]

        send_mail(subject, message, from_email, recipient_list)

        return render(request,"contactoRepuestos.html")

    return render (request,'contactoRepuestos.html')

#Páginas de DFM

def fengshen(request):
    return render(request,'fengshenS30.html', {})

def DongfengAX4(request):
    return render(request,'AX4.html', {})

def DongfengAX7_PRO(request):
    return render(request,'AX7-PRO.html', {})
    
def NEW_AX7(request):
    return render(request,'AX7-New.html', {})

def A60(request):
    return render(request,'A60.html', {})
    
#Páginas de Foton
def Midi_Simple(request):
    return render(request,'midi-simple.html', {})

def Midi_Van(request):
    return render(request,'midi-van.html', {})
    
def Midi_Doble(request):
    return render(request,'Midi-Doble.html', {})

def tm_doble(request):
    return render(request,'tm-doble.html',{})
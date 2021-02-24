from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from Repuestos.models import *
from django.conf import settings


#Vistas
def Repuestos(request):
    return render(request,'inicio.html', {})
        
def probar(request):
    item = Repuesto.objects.all()

    return render(request,'Probar.html', {'item': item})

def buscar(request):
    item = {}
    
    if request.method == "POST":
        buscar = request.POST['txtBuscar']
        
        if 'txtBuscar' in request.POST:
            item = Repuesto.objects.filter(nombreRepuesto__contains = buscar)
           
    return render(request,'buscar.html', {'item':item}) 
    
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
    ver = Repuesto.objects.filter(modelo__nombre='Fengshen S30')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='Fengshen S30')
                
    contexto = {'lista' : lista, 'ver' : ver}   
    return render(request,'fengshenS30.html', contexto)

def AX4(request):
    ver = Repuesto.objects.filter(modelo__nombre='AX4')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='AX4')
                
    contexto = {'lista' : lista, 'ver' : ver} 
    return render(request,'AX4.html', contexto)

def AX7_PRO(request):
    ver = Repuesto.objects.filter(modelo__nombre='AX7-PRO')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='AX7-PRO')
                
    contexto = {'lista' : lista, 'ver' : ver}
    return render(request,'AX7-PRO.html', contexto)
    
def NEW_AX7(request):
    ver = Repuesto.objects.filter(modelo__nombre = "NEW-AX7")
    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='NEW-AX7')
                
    contexto = {'lista' : lista, 'ver' : ver} 
    return render(request,'AX7-New.html', contexto)

def A60(request):
    ver = Repuesto.objects.filter(modelo__nombre='A60')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='A60')
                
    contexto = {'lista' : lista, 'ver' : ver}   
    return render(request,'A60.html', contexto)
    
#Páginas de Foton
def Midi_Simple(request):
    ver = Repuesto.objects.filter(modelo__nombre='MIDI Truck Simple')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='MIDI Truck Simple')
                
    contexto = {'lista' : lista, 'ver' : ver}   
    return render(request,'midi-simple.html', contexto)

def Midi_Van(request):
    ver = Repuesto.objects.filter(modelo__nombre='MIDI Van Furgon')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='MIDI Van Furgon')
                
    contexto = {'lista' : lista, 'ver' : ver}   
    return render(request,'midi-van.html', contexto)
    
def Midi_Doble(request):
    ver = Repuesto.objects.filter(modelo__nombre='MIDI Truck Doble')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='MIDI Truck Doble')
                
    contexto = {'lista' : lista, 'ver' : ver}
    return render(request,'Midi-Doble.html', contexto)

def tm_doble(request):
    ver = Repuesto.objects.filter(modelo__nombre='TM-Doble')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='TM-Doble')
                
    contexto = {'lista' : lista, 'ver' : ver}
    return render(request,'tm-doble.html',contexto)
    
def tm_simple(request):
    ver = Repuesto.objects.filter(modelo__nombre='TM-Simple')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='TM-Simple')
                
    contexto = {'lista' : lista, 'ver' : ver}   
    return render(request,'TM-Simple.html', contexto)

def ft_500(request):
    ver = Repuesto.objects.filter(modelo__nombre='FT-500')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='FT-500')
                
    contexto = {'lista' : lista, 'ver' : ver}
    return render(request,'Ft-500.html', contexto)
    
def FT_CREW(request):
    ver = {}
    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='FT-CREW')
        
        elif 'btnTodos' in request.POST:
            ver = Repuesto.objects.filter(modelo__nombre='FT-CREW')
        
    contexto = {'lista' : lista, 'ver' : ver}
    return render(request,'FT-CREW.html', contexto)
    
def FT_BOX(request):
    ver = Repuesto.objects.filter(modelo__nombre='FT-BOX')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='FT-BOX')
                
    contexto = {'lista' : lista, 'ver' : ver}
    return render(request,'FT-BOX.html',contexto)
    
def K1(request):
    ver = Repuesto.objects.filter(modelo__nombre='K1')

    lista = {}

    if request.method == "POST":
        id            = int("0" + request.POST["categoria"])
        tipo          = request.POST["repuesto"]

        if 'btnListar' in request.POST:
            lista = Repuesto.objects.filter(categoria_id = id).filter(tipo__nombre = tipo).filter(modelo__nombre='K1')
                
    contexto = {'lista' : lista, 'ver' : ver}
    return render(request,'K1.html', contexto)
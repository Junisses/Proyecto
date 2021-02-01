from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'inicio.html', {})
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
def contactoRepuestos(request):
    return render(request,'contactoRepuestos.html', {})
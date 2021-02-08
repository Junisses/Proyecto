from django.shortcuts import render
from .forms import TestForm
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import  csrf_exempt
from Repuestos.models import Localidades
from Repuestos.models import Comuna
from django.core.mail import send_mail
from django.conf import settings


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
class TestView(TemplateView):
    template_name = 'contactoRepuestos.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_comuna_id':
                data = []
                for i in Comuna.objects.filter(localidad_id=request.POST['id']):
                    data.append({'id': i.id, 'name': i.nombre})
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidado'
        context['form'] = TestForm
        return context

def repuestosFoton(request):
    return render(request,'repuestosFoton.html', {})

def correo(request):
    if request.method== 'POST':

        subject=request.POST["Asunto"]

        message=request.POST["mensaje"]+ " " + request.POST["email"] 

        from_email=settings.EMAIL_HOST_USER

        recipient_list=["javier.orellana2001@gmail.com"]

        send_mail(subject, message, from_email, recipient_list)

        return render(request,"gracias.html")

    return render (request,"correo.html")

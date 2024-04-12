from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from django.conf import settings
from decouple import config

from gestionPedidos.models import Articulos
from gestionPedidos.forms import Contact_Form

# Create your views here.
def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')

def search(request):
    if request.GET['prd']:
        producto = request.GET['prd']
        
        if len(producto) > 20:
            message = 'El texto es demasiado largo'
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultados.html',{'articulos':articulos,'query':producto})
    else:
        message = 'No se ha buscado nada'
    
    return HttpResponse(message)
    
    
def contacto(request):
    
    if request.method == 'POST':
        mi_formulario = Contact_Form(request.POST)
        
        if mi_formulario.is_valid():
            inf_Formulario = mi_formulario.cleaned_data
            
            send_mail(inf_Formulario['asunto'], inf_Formulario['mensaje'], inf_Formulario.get('email',config('EMAIL_HOST_USER')), [config('EMAIL_RECEIVER_USER')],)
            
            return render(request, 'gracias.html')
        
    else:
        mi_formulario = Contact_Form()
        
    return render(request, 'formulario_contacto.html',{'form':mi_formulario})
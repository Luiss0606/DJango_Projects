from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


from decouple import config
from .models import Pedido, LineaPedido
from Carro.carro import Carro


# Create your views here.
@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido,
        ))
        
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.user.username,
        email_usuario=request.user.email,
    )
    messages.success(request, "Pedido procesado con exito")
    
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombre_usuario": kwargs.get("nombre_usuario"),
    })
    
    mensaje_texto = strip_tags(mensaje)
    from_email = config("EMAIL_HOST_USER")
    # to = kwargs.get["email_usuario"]
    to = "luis.huingo.c@uni.pe"
    
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

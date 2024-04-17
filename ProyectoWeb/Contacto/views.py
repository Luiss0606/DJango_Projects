from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

from decouple import config

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    
    if request.method == "POST":
        formulario_contacto = FormularioContacto(request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            
            email = EmailMessage("Mensaje enviado desde App Django", 
                                    "El usuario con nombre {} con direccion {} escribe el siguiente contenido: {}".format(nombre, email, contenido),
                                    config("EMAIL_HOST_USER"),[config("EMAIL_RECEIVER_USER")], reply_to=[email])
            
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")
    
    return render(request, "Contacto/contacto.html", {"mi_formulario": formulario_contacto})
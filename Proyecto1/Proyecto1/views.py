from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request):


    p1 = Persona("David", "Martinez")

    return render(request, "miplantilla.html",{
        'nombre_persona': p1.nombre,
        'apellido_persona': p1.apellido,
        'hora': datetime.datetime.now(),
        'cursos': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    })


def despedida(request):
    return HttpResponse("Hasta luegoesta es nuestra segunda pagina con Django")

def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
    <body>
    <h1>Hola mundo esta es nuestra primer pagina con Django</h1>
    <h2>Hasta luegoesta es nuestra segunda pagina con Django</h2>
    <h3>La fecha es: %s</h3>
    </body>
    </html>
    """ % fecha_actual
    return HttpResponse(documento)


def calcularEdad(request,edad, year):
    # edadActual = 18
    periodo = int(year) - datetime.datetime.now().year
    edad_futura = edad + periodo

    documento = """
    <html>
    <body>
    <h1>You are %d years old</h1>
    <h2>You will be %d in %d</h2>
    </body>
    </html>
    """ % (edad,edad_futura, year)
    return HttpResponse(documento)


def cursoC(request):
    fecha = datetime.datetime.now()

    return render(request, "cursoC.html", {'dame_Fecha': fecha})

def cursoCSS(request):
    fecha = datetime.datetime.now()

    return render(request, "cursoCSS.html", {'dame_Fecha': fecha})
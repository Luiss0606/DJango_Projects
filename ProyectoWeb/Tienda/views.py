from django.shortcuts import render
from .models import CatProducto, Producto

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "Tienda/tienda.html",{"productos":productos})
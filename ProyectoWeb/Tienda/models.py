from django.db import models

# Create your models here.
class CatProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'categoriaPro'
        verbose_name_plural = 'categoriasProd'
        
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50,)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='tienda', blank=True, null=True)
    categoria = models.ForeignKey(CatProducto, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
    def __str__(self):
        return self.nombre
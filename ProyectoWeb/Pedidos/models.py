from django.db import models
from django.contrib.auth import get_user_model
from Tienda.models import Producto
from django.db.models import Sum, F, FloatField

User = get_user_model()

# Create your models here.
class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    @property
    def total(self):
        return self.linea_pedidos.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"] or FloatField(0)
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']
        
    def __str__(self) -> str:
        return str(self.id)

        
class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table = 'linea_pedidos'
        verbose_name = 'linea de pedido'
        verbose_name_plural = 'lineas de pedido'
        ordering = ['id']
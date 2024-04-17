from django.contrib import admin
from .models import CatProducto, Producto

# Register your models here.
class CatProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
    
admin.site.register(CatProducto, CatProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
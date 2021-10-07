from django.contrib import admin
from .models.producto import Producto
from .models.carrito import Carrito

admin.site.register(Producto)
admin.site.register(Carrito)


from django.db import models
from .producto import Producto 
# Aquí van los atributos e información relevante a la tabla "carrito"

class Carrito(models.Model):
    """
    Clase que establece el modelo de la tabla 'carrito'
    en la base de datos correspondiente.
    """
    id = models.AutoField(primary_key=True)
    id_producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    valor_total = models.IntegerField(default=0)
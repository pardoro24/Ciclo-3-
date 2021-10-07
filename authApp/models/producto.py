from django.db import models 
#Aquí van los atributos e información relevante a la tabla "producto"

class Producto(models.Model):
    """
    Clase que establece el modelo de la tabla 'producto'
    en la base de datos correspondiente.
    """
    id_producto = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    tipo= models.CharField(max_length=50)
    lote= models.CharField(max_length=50)
    precio_uni = models.IntegerField()

    
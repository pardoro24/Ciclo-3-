from rest_framework import serializers
from authApp.models.producto import Producto


class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'tipo', 'lote', 'precio_uni']


        
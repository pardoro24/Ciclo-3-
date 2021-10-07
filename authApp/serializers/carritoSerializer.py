from rest_framework import serializers
from authApp.models.carrito import Carrito

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ['id_producto', 'cantidad', 'valor_total']

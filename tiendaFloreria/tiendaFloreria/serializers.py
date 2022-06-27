from dataclasses import fields
from rest_framework import serializers
from productos.models import Producto
from ordenes.models import Ordenes

class Producto_srlz(serializers.ModelSerializer):
    
    class Meta:
        model=Producto
        fields = '__all__'

class Ordenes_srlz(serializers.ModelSerializer):
    
    class Meta:
        model=Ordenes
        fields = '__all__'
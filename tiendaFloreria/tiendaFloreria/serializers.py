from dataclasses import fields
from rest_framework import serializers
from productos.models import Producto

class Producto_srlz(serializers.ModelSerializer):
    
    class Meta:
        model=Producto
        fields = '__all__'
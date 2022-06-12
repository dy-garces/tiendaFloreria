from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
# Create your models here.

class Carrito(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)#relacion uno a muchos
    productos = models.ManyToManyField(Producto)
    subtotal = models.IntegerField(default = 0)
    total = models.IntegerField(default = 0)
    fecha_carrito = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id) 
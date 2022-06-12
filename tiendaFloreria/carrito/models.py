from tkinter import CASCADE
import uuid
from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from django.db.models.signals import pre_save,m2m_changed
# Create your models here.

class Carrito(models.Model):
    carrito_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)#relacion uno a muchos
    productos = models.ManyToManyField(Producto, through='CarritoProductos')
    subtotal = models.IntegerField(default = 0)
    fecha_carrito = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.carrito_id 
    
    def actualizar_subtotal(self):
        self.subtotal =  sum([producto.precio for producto in self.productos.all()]) 
        self.save()

class CarritoProductos(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    creacion = models.DateField(auto_now_add=True)
    
def set_carrito_id(sender, instance, *args, **kwargs):
    if not instance.carrito_id:
        instance.carrito_id = str(uuid.uuid4())
        
def actualizar_subtotal(sender, instance, action ,*args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.actualizar_subtotal()

pre_save.connect(set_carrito_id, sender=Carrito)
m2m_changed.connect(actualizar_subtotal,sender=Carrito.productos.through)

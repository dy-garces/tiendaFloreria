import uuid
from django.db.models.signals import pre_save
from django.db import models
from django.contrib.auth.models import User
from carrito.models import Carrito

from direccion_envio.models import DireccionEnvio
# Create your models here.

class status(models.Model):
   
    nombre = models.CharField(max_length=50,blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.nombre 

class Ordenes(models.Model):
    orden_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete = models.CASCADE)
    status = models.ForeignKey(status, on_delete= models.PROTECT)
    total = models.IntegerField(default=0)
    envio = models.IntegerField(default=15000)
    creacion = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.CharField( max_length=200 ,null=True , blank=True,)
    
    def __str__(self):
        return self.orden_id

    def update_total(self):
        self.total = self.get_total()
        self.save()
    
    def get_total(self):
        print( self.carrito.subtotal)
        return self.carrito.subtotal + self.envio
    
def set_orden_id(sender, instance, *args, **kwargs):
    if not instance.orden_id:
        instance.orden_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwargs):
    instance.total = instance.get_total()
    
pre_save.connect(set_orden_id, sender=Ordenes)
pre_save.connect(set_total, sender=Ordenes)
import uuid
from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from django.db.models.signals import pre_save
# Create your models here.


    
    
def set_carrito_id(sender,instance, *args, **kwargs):
    if not instance.carrito_id:
        instance.carrito_id = str(uuid.uuid4())

pre_save.connect(set_carrito_id,sender=Carrito)
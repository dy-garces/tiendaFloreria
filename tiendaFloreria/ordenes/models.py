from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from carrito.models import Carrito
from enum import Enum
# Create your models here.

class OrdenesStatus(Enum):
    CREADO = 'CREADO'
    PAGADO = 'PAGADO'
    COMPLETADO = 'COMPLETADO'
    CANCELADO = 'CANCELADO'
    
choices = [( tag, tag.value) for  tag in OrdenesStatus]


class Ordenes(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete = models.CASCADE)
    status = models.CharField(max_length=50, choices=choices, default=OrdenesStatus.CREADO)
    total = models.IntegerField(default=0)
    creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return ''
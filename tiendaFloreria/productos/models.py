from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre =  models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    creacion = models.DateTimeField(auto_now_add=True)
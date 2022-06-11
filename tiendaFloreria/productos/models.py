from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre =  models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos",null=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    creacion = models.DateTimeField(auto_now_add=True)
    categoria =  models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre
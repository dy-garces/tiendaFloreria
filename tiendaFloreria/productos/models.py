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
    precio = models.IntegerField(default=0)
    slug = models.SlugField(null=False, blank=False , unique=True)
    creacion = models.DateTimeField(auto_now_add=True)
    categoria =  models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre
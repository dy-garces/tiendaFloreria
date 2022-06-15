from django.db import models

# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    nombre_usuario=models.CharField(primary_key=True,max_length=50)
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    rut=models.CharField(unique=True,max_length=10)
    fecha_nac=models.DateField()
    direccion=models.CharField(max_length=250)
    correo = models.EmailField()
    numero = models.IntegerField()
    comuna = models.ForeignKey(Comuna,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos/usuarios",null=True, blank=True)
    vendedor=models.BooleanField(default=False)
    suscrito=models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre + " "+self.apellido


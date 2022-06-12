from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre =  models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="productos",null=False, blank=False)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0)
    slug = models.SlugField(null=False, blank=False , unique=True)
    creacion = models.DateTimeField(auto_now_add=True)
    categoria =  models.ForeignKey(Categoria, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre
    
def set_slug(sender, instance, *args, **kwargs):
    if instance.nombre and not instance.slug:
        slug = slugify(instance.nombre) 
        while Producto.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nombre, str(uuid.uuid4())[:8] )
            )
        instance.slug = slug
        
pre_save.connect(set_slug,sender=Producto)
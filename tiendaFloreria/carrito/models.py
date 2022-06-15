import uuid
from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from django.db.models.signals import pre_save,m2m_changed, post_save
# Create your models here.

class Carrito(models.Model):
    carrito_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) #relacion uno a muchos
    productos = models.ManyToManyField(Producto, through='CarritoProductos')
    subtotal = models.IntegerField(default = 0)
    total = models.IntegerField(default= 0)
    fecha_carrito = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.carrito_id 
    
    def update_subtotal(self):
        self.update_subtotal()
        if self.orden:
            self.orden.actualizar_subtotal()
            
    def actualizar_subtotal(self):
        self.subtotal =  sum([
           cp.cantidad * cp.producto.precio for cp in self.productos_relacion()
        ]) 
        self.save()

    def productos_relacion(self):
        return self.carritoproductos_set.select_related('producto')
    
    @property
    def orden(self):
        return self.ordenes_set.first() 


class CarritoProductosManager(models.Manager):
    
    def crear_o_actualizar_cantidad(self,carrito, producto, cantidad=1):
        object , created = self.get_or_create(carrito = carrito , producto = producto )
        if not created:
            cantidad = object.cantidad + cantidad
        object.actualizar_cantidad(cantidad)
        return object
        

class CarritoProductos(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    creacion = models.DateField(auto_now_add=True)
    objects = CarritoProductosManager()
    
    def actualizar_cantidad(self, cantidad = 1 ):
        self.cantidad = cantidad
        self.save()
    
def set_carrito_id(sender, instance, *args, **kwargs):
    if not instance.carrito_id:
        instance.carrito_id = str(uuid.uuid4())
        
def actualizar_subtotal(sender, instance, action ,*args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.actualizar_subtotal()

def post_save_actualizar_subtotal(sender, instance, *args, **kwargs):
    instance.carrito.actualizar_subtotal()

pre_save.connect(set_carrito_id, sender=Carrito)
post_save.connect(post_save_actualizar_subtotal, sender=CarritoProductos)
m2m_changed.connect(actualizar_subtotal,sender=Carrito.productos.through)

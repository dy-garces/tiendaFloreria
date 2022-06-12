
from django.shortcuts import render
from .utilis import obtener_o_crear_carrito
from productos.models import Producto
# Create your views here.

def carrito(request):
    carrito = obtener_o_crear_carrito(request)
    
    return render(request, 'carrito/carrito.html')

def agregar(request):
    cart = obtener_o_crear_carrito(request)
    producto = Producto.objects.get(pk=request.POST.get('producto_id'))
    
    print(producto)
    
    cart.productos.add(producto)
    
    return render(request,'carrito/agregar.html',{
        'producto':producto
    })
import imp
from django.shortcuts import get_object_or_404, render
from .utilis import obtener_o_crear_carrito
from productos.models import Producto
# Create your views here.

def carrito(request):
    carrito = obtener_o_crear_carrito(request)
    
    return render(request, 'carrito/carrito.html')

def agregar(request):
    carrito = obtener_o_crear_carrito(request)
    producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))
    
    print(producto)
    
    carrito.productos.add(producto)
    
    contexto={
        'producto': producto
    }
    return render(request,'carrito/agregar.html',contexto)
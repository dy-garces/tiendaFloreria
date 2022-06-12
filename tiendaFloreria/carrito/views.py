
from django.shortcuts import get_object_or_404, render
from .utilis import obtener_o_crear_carrito
from productos.models import Producto
# Create your views here.

def carrito(request):
    carrito = obtener_o_crear_carrito(request)
    
    return render(request,'carrito/carrito.html')

def agregar(request):
    carrito = obtener_o_crear_carrito(request)
    producto =  Producto(pk=request.POST.get('product_id'))
    
    print(producto)
    carrito.producto.add(producto)
    
    return render(request, 'agregar.html', {'producto': producto})

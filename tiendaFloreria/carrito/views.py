import imp
from django.shortcuts import get_object_or_404, render
from .models import Carrito
from .models import Producto
# Create your views here.

def carrito(request):
    usuario = request.user if request.user.is_authenticated else None
    carrito_id = request.session.get('carrito_id')
    carrito = Carrito.objects.filter(id = carrito_id).first()
    
    if carrito is None:
        carrito = Carrito.objects.create(usuario = usuario)
        
    if usuario and carrito.usuario is None:
        carrito.usuario = usuario
        carrito.save()
        
    request.session['carrito_id'] = carrito.id
    
    return render(request, 'carrito/carrito.html')

def agregar(request):
    usuario = request.user if request.user.is_authenticated else None
    carrito_id = request.session.get('carrito_id')
    carrito = Carrito.objects.filter(id = carrito_id).first()
    
    if carrito is None:
        carrito = Carrito.objects.create(usuario = usuario)
        
    if usuario and carrito.usuario is None:
        carrito.usuario = usuario
        carrito.save()
        
    request.session['carrito_id'] = carrito.id
    
    producto = get_object_or_404(Producto,id=request.POST.get('producto_id'))
    print(producto)
    print(carrito)
    
    carrito.productos.add(producto)
    
    contexto={
        'producto': producto
    }
    return render(request,'carrito/agregar.html',contexto)



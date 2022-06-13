
from django.shortcuts import get_object_or_404, redirect, render
from .models import Carrito, CarritoProductos
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
    
    return render(request, 'carrito/carrito.html',{ 'carrito' : carrito})

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
    cantidad = int(request.POST.get('cantidad',1))

    carrito_producto = CarritoProductos.objects.crear_o_actualizar_cantidad(carrito=carrito, 
                                                    producto=producto, 
                                                    cantidad = cantidad)
    
    return render(request,'carrito/agregar.html',{'producto': producto, })

def eliminar(request):
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
    
    carrito.productos.remove(producto)
    
    return redirect('carrito:carrito')

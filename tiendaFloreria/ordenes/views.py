from django.shortcuts import render
from .models import Ordenes
from carrito.models import Carrito
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def orden(request):
    usuario = request.user if request.user.is_authenticated else None
    carrito_id = request.session.get('carrito_id')
    carrito = Carrito.objects.filter(id = carrito_id).first()
    
    if carrito is None:
        carrito = Carrito.objects.create(usuario = usuario)
        
    if usuario and carrito.usuario is None:
        carrito.usuario = usuario
        carrito.save()
        
    request.session['carrito_id'] = carrito.id
    
    orden = Ordenes.objects.filter(carrito = carrito).first()
    
    if orden is None and request.user.is_authenticated:
        orden = Ordenes.objects.create(carrito = carrito, usuario = request.user)
        
    if orden:
        request.session['orden_id'] = orden.orden_id
    
    return render(request, 'ordenes/orden.html',{ 
        'carrito':carrito,
        'orden' :orden 
        })
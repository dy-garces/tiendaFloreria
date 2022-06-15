
from django.shortcuts import get_object_or_404, redirect, render
from .models import Ordenes
from carrito.models import Carrito
from django.contrib.auth.decorators import login_required
from .utilis import breadcrumb, destruir_orden
from direccion_envio.models import DireccionEnvio
from django.contrib import messages
from carrito.utilis import destruir_carrito
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

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
        'orden' :orden ,
        'breadcrumb' : breadcrumb()
        })
    
@login_required(login_url='login')   
def direccion(request):
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
        
    direccion_envio = DireccionEnvio.objects.filter(user = usuario).first()
    
    if request.user != orden.usuario:
        return redirect('carrito:carrito')
    
    if direccion_envio:
        orden.direccion_envio = str(direccion_envio)
        orden.save()
        
    return render(request, 'ordenes/direccion.html',{
        'carrito':carrito,
        'orden' :orden ,
        'direccion_envio':direccion_envio,
        'breadcrumb' : breadcrumb(direccion=True)
    })
    
@login_required(login_url='login')
def confirmacion(request):
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
    
    if request.user != orden.usuario:
        return redirect('carrito:carrito')
        
    direccion = orden.direccion_envio

    if direccion is None:
        return redirect('ordenes:direccion.html')
    
    return render(request, 'ordenes/confirmacion.html',{
        'carrito':carrito,
        'orden' :orden ,
        'breadcrumb' : breadcrumb(direccion=True, confirmacion=True)
    })
 
@login_required(login_url='login')       
def cancelar(request):
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
    
    if request.user != orden.usuario:
        return redirect('carrito:carrito')
        
    orden.cancelar()
    
    destruir_carrito(request)
    destruir_orden(request)
    
    messages.error(request, 'Orden Cancelada')
    return redirect('home')

@login_required(login_url='login') 
def completar(request):
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
        
    if request.user != orden.usuario:
        return redirect('carrito:carrito')
    
    orden.completar()
    
    destruir_carrito(request)
    destruir_orden(request)
    
    messages.success(request, 'Compra Completada exitosamente')
    return redirect('home')
    
class OrdenesListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    modelo = Ordenes
    template_name = 'ordenes/ordenes.html'
    
    def get_queryset(self):
        return Ordenes.objects.filter(usuario = self.request.user).order_by('-id')

@login_required(login_url='login') 
def detalleCompra(request, carrito_id):

    carrito_id = get_object_or_404(Carrito, id=carrito_id)
    orden = Ordenes.objects.filter(carrito = carrito_id).first()
    
    return render(request, 'ordenes/detalleCompra.html',{ 
        'carrito' : carrito_id,
        'orden' : orden
        })

@login_required(login_url='login')   
def seguimientoCompra(request,id):
    
    orden = Ordenes.objects.filter(id = id).first()
    
    return render(request, 'ordenes/seguimientoCompra.html',{
        'orden' : orden
    })
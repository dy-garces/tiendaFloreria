from django.shortcuts import render

from productos.models import Producto
from rest_framework import viewsets
from .serializers import Producto_srlz


def home(request):
    productos = Producto.objects.all()
    contexto ={
        'productos' : productos
    }
    return render(request,'home.html',contexto)

def quienesSomos(request):
    return render(request,'quienesSomos.html')

def contacto(request):
    return render(request,'contacto.html')

def flores(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,'flores.html',contexto)

def plantas(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,'plantas.html',contexto)

def arboles(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,'arboles.html',contexto)

def maceteros(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,"maceteros.html",contexto)

def jardineria(request):
    productos = Producto.objects.all()
    contexto = {
        'productos': productos
    }
    return render(request,"jardineria.html",contexto)

def producto(request):
    
    return render(request,"producto.html")

class productosViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = Producto_srlz

# class ordenesViewSet(viewsets.ModelViewSet):
#     queryset = Ordenes.objects.all()
#     serializer_class = Ordenes_srlz
    
    
    
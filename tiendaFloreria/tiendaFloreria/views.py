from django.shortcuts import get_object_or_404, render, redirect

from productos.models import Producto

from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


def home(request):
    productos = Producto.objects.all()
    contexto ={
        'productos' : productos
    }
    return render(request,'home.html',contexto)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to='home')
        data["form"] = formulario    
    return render(request,"registration/registro.html",data)

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

def producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'producto' : producto
    }
    return render(request,"producto.html",data)
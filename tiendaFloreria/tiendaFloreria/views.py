from django.shortcuts import render, redirect

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

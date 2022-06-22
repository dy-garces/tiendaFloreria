from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from tiendaFloreria.forms import frmPerfilUsuario
from usuarios.models import PerfilUsuario
from django.contrib.auth import authenticate,login

# Create your views here.


def registro(request):
    form=UserCreationForm(request.POST or None)
    contexto={
        "frm":form
    }
    
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            credenciales=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
            login(request,credenciales)
            return redirect(to="perfilusuario")
    
    return render(request,"registration/registro.html",contexto)

def perfilusuario(request):
    form=frmPerfilUsuario(request.POST or None)
    contexto={
        "frm":form
    }
    if request.method=="POST":
        form=frmPerfilUsuario(data=request.POST, files=request.FILES)
        if form.is_valid():
            datos=form.cleaned_data
            perfil=PerfilUsuario()
            perfil.rut=datos.get("rut")
            perfil.nombre=datos.get("nombre")
            perfil.apellido=datos.get("apellido")
            perfil.fecha_nac=datos.get("fecha_nac")
            perfil.correo=datos.get("correo")
            perfil.numero=datos.get("numero")
            perfil.comuna=datos.get("comuna")
            perfil.imagen=datos.get("imagen")
            perfil.vendedor=datos.get("vendedor")
            perfil.suscrito=datos.get("suscrito")
            perfil.nombre_usuario=request.user.username
            perfil.save()         
            return redirect(to="home")
        
    return render(request,"registration/perfilusuario.html",contexto)

def perfil(request):
    perfil = PerfilUsuario.objects.all()
    data = {
        'perfil' : perfil
    }
    return render(request,"perfil.html",data)

def modificarusuario(request,id):
    perfilusuario=get_object_or_404(PerfilUsuario,nombre_usuario=id)
    frm=frmPerfilUsuario(instance=perfilusuario)
    
    contexto={
        "frm":frm
    }
    if request.method=="POST":
        frm=frmPerfilUsuario(data=request.POST,files=request.FILES,instance=perfilusuario)
        if frm.is_valid():
            perfilusuario_mod=PerfilUsuario.objects.get(nombre_usuario=perfilusuario.nombre_usuario)
            datos=frm.cleaned_data
            perfilusuario_mod.rut=datos.get("rut")
            perfilusuario_mod.nombre=datos.get("nombre")
            perfilusuario_mod.apellido=datos.get("apellido")
            perfilusuario_mod.direccion=datos.get("direccion")
            perfilusuario_mod.fecha_nac=datos.get("fecha_nac")
            perfilusuario_mod.correo=datos.get("correo")
            perfilusuario_mod.numero=datos.get("numero")
            perfilusuario_mod.comuna=datos.get("comuna")
            perfilusuario_mod.imagen=datos.get("imagen")
            perfilusuario_mod.vendedor=datos.get("vendedor")
            perfilusuario_mod.suscrito=datos.get("suscrito")
            perfilusuario_mod.save()
            return redirect(to="perfil")
            
        
    return render(request,"modificarusuario.html",contexto)

def cambiarpassword(request):
    form=PasswordChangeForm(request.POST or None)
    contexto={
        "frm":form
    }
    
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="perfil")
    
    return render(request,"registration/cambiarpassword.html",contexto)


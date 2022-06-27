from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.urls import reverse_lazy
from tiendaFloreria.forms import frmPerfilUsuario
from usuarios.models import Comuna, PerfilUsuario, Region
from django.contrib.auth import authenticate,login
from usuarios.forms import FormularioRegion, FormularioComuna
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views  import SuccessMessageMixin
from django.views.generic import UpdateView, DeleteView

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

def formRegion(request):
    form = FormularioRegion(request.POST or None)
    if request.method == 'POST' :
        form = FormularioRegion(data = request.POST, files=request.FILES)
        if form.is_valid():
            region = form.save(commit=False)
            region.save()
            messages.success(request, 'region creada exitosamente')
            return redirect('home')
    
    return render(request,'registration/formRegion.html',{'form': form})

def listadoRegion(request):
    region = Region.objects.all()
    return render(request, 'registration/listadoRegion.html', { 'region':region })

class RegionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Region
    form_class = FormularioRegion
    template_name = 'registration/updateRegion.html'
    
    def get_success_url(self):
        return resolve_url('listadoRegion')

class RegionDeleteView(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    login_url = 'login'
    model = Region
    template_name = 'registration/borrarRegion.html'
    success_url = reverse_lazy('listadoRegion')
    success_message = 'Region eliminada exitosamente'

def formComuna(request):
    form = FormularioComuna(request.POST or None)
    if request.method == 'POST' :
        form = FormularioComuna(data = request.POST, files=request.FILES)
        if form.is_valid():
            comuna = form.save(commit=False)
            comuna.save()
            messages.success(request, 'Comuna creada exitosamente')
            return redirect('home')
    
    return render(request,'registration/formComuna.html',{'form': form})

def listadoComuna(request):
    comuna = Comuna.objects.all()
    return render(request, 'registration/listadoComuna.html', { 'comuna':comuna })

class ComunaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Comuna
    form_class = FormularioComuna
    template_name = 'registration/updateComuna.html'
    
    def get_success_url(self):
        return resolve_url('listadoComuna')

class ComunaDeleteView(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    login_url = 'login'
    model = Comuna
    template_name = 'registration/borrarComuna.html'
    success_url = reverse_lazy('listadoComuna')
    success_message = 'Comuna eliminada exitosamente'



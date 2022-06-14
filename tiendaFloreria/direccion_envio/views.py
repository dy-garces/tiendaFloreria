

from django.shortcuts import get_object_or_404, redirect, render,resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView,DeleteView
from .models import DireccionEnvio
from .forms import DireccionEnvioForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views  import SuccessMessageMixin

# Create your views here.

class DireccionEnviosListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    modelo = DireccionEnvio
    template_name = 'direccion_envio/direccion_envio.html'
    
    def get_queryset(self):
        return DireccionEnvio.objects.filter(user = self.request.user)


class DireccionEnviosUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = DireccionEnvio
    form_class = DireccionEnvioForms
    template_name = 'direccion_envio/update.html'
    
    def get_success_url(self):
        return resolve_url('direccion_envio:direccion_envio')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect('carrito:carrito')

        return super(DireccionEnviosUpdateView, self).dispatch(request, *args, **kwargs)

class DireccionEnviosDeleteView(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    login_url = 'login'
    model = DireccionEnvio
    template_name = 'direccion_envio/borrar.html'
    success_url = reverse_lazy('direccion_envio:direccion_envio')
    success_message = 'Direccion eliminado exitosamente'

@login_required(login_url='login')
def crear(request):
    
    form = DireccionEnvioForms(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        direccion_envio = form.save(commit=False)
        direccion_envio.user = request.user
        direccion_envio.default = not DireccionEnvio.objects.filter(user = request.user).exists()
        direccion_envio.save()
        
        messages.success(request, 'Direccion creada exitosamente')
        return redirect('direccion_envio:direccion_envio')
    
    return render(request, 'direccion_envio/crear.html', {'form':form})

    
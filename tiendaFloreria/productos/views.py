from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, resolve_url
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from productos.models import Producto
from django.urls import reverse_lazy
from .forms import FormularioProducto
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views  import SuccessMessageMixin
# Create your views here.

class PrductoListaView(ListView):
    template_name='home.html'
    queryset = Producto.objects.all().order_by('-id')
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) 
        context['productos'] = context['producto_list']
                
        return context
    
class ProductoDetalleView(DetailView):
    model = Producto
    template_name = 'productos/producto.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)    
        return context

class ProductoBuscarListView(ListView):
    template_name = 'productos/buscador.html'
    
    def get_queryset(self):
        
        return Producto.objects.filter(nombre__icontains=self.query())
    
    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = context['producto_list']
        context['query'] = self.query()
        context['count'] = context['producto_list'].count()

        return context  

@login_required(login_url='login')
def formProducto(request):
    form = FormularioProducto(request.POST or None)
    if request.method == 'POST' :
        form = FormularioProducto(data = request.POST, files=request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            messages.success(request, 'Producto creado exitosamente')
            return redirect('home')
    
    return render(request,'productos/formProducto.html',{'form': form})

class productoListado(LoginRequiredMixin, ListView):
    login_url = 'login'
    modelo = Producto
    template_name = 'productos/productoListado.html'
    
    def get_queryset(self):
        return Producto.objects.filter(usuario = self.request.user).order_by('-id')
    
class ProductoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Producto
    form_class = FormularioProducto
    template_name = 'productos/update.html'
    
    def get_success_url(self):
        return resolve_url('productos:productoListado')
    
    def dispatch(self, request, *args, **kwargs):
        print( self.get_object().usuario)
        print(request.user)
        if request.user != self.get_object().usuario:
            return redirect('home')
        return super(ProductoUpdateView, self).dispatch(request, *args, **kwargs)
            
class ProductoDeleteView(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    login_url = 'login'
    model = Producto
    template_name = 'productos/borrar.html'
    success_url = reverse_lazy('productos:productoListado')
    success_message = 'Producto eliminado exitosamente'

      
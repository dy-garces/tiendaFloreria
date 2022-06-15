from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Producto
from .forms import FormularioProducto
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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
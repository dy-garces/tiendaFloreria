from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Producto
from django.db.models import Q

# Create your views here.

class PrductoListaView(ListView):
    template_name='home.html'
    queryset = Producto.objects.all().order_by('-id')
    
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
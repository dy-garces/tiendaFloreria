from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from productos.models import Producto

# Create your views here.

class PrductoListaView(ListView):
    template_name='home.html'
    queryset = Producto.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) 
        context['message'] = 'Listado de Productos'
        context['productos'] = context['producto_list']
        
        print(context)
        
        return context
    

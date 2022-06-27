from cProfile import label
from dataclasses import field
from django import forms
from .models import Categoria, Producto


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre","imagen","descripcion","precio","stock","categoria"]
        label = {
           'nombre'      : 'Nombre del Producto',
           'imagen'      : 'Imagen',
           'descripcion' : 'Descripcion del Producto',
           'precio'      : 'Precio',
           'categoria'   : 'Categoria del Producto'
        }
        

class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]
        label = {
           'nombre' : 'Nombre de la categoria',
        }
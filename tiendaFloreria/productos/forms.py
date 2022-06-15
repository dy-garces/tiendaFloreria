from cProfile import label
from dataclasses import field
from django import forms
from .models import Producto


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre","imagen","descripcion","precio","categoria"]
        label = {
           'nombre'      : 'Nombre del Producto',
           'imagen'      : 'Imagen',
           'descripcion' : 'Descripcion del Producto',
           'precio'      : 'Precio',
           'categoria'   : 'Categoria del Producto'
        }
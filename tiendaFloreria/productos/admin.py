from django.contrib import admin
from .models import Producto,Categoria
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    fields =( 'nombre','imagen','descripcion','precio','categoria' )
    list_display = ('__str__','slug','creacion')

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Categoria)

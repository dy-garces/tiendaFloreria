from unicodedata import name
from django.urls import path
from .import views

app_name = 'ordenes'

urlpatterns = [
    path('',views.orden, name="orden"),
    path('direccion', views.direccion, name="direccion"),
    path('confirmacion', views.confirmacion, name='confirmacion'),
    path('cancelar', views.cancelar, name='cancelar'),
    path('completar', views.completar, name='completar'),
    path('completados', views.OrdenesListView.as_view(), name='completados'),
    path('detalleCompra/<int:carrito_id>',views.detalleCompra, name="detalleCompra"),
    path('seguimientoCompra/<categoria>',views.seguimientoCompra , name='seguimientoCompra'),
    
]



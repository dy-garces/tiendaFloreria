from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('buscador', views.ProductoBuscarListView.as_view(), name='buscador'),
    path('<slug:slug>', views.ProductoDetalleView.as_view(),name='producto'),
    path('formProducto/',views.formProducto,name='formProducto'),
    path('productoListado/', views.productoListado.as_view(), name='productoListado'),
]

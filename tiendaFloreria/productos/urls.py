from django.urls import path, include
from . import views

app_name = 'productos'



urlpatterns = [
    path('buscador', views.ProductoBuscarListView.as_view(), name='buscador'),
    path('<slug:slug>', views.ProductoDetalleView.as_view(),name='producto'),
    path('formProducto/',views.formProducto,name='formProducto'),
    path('productoListado/', views.productoListado.as_view(), name='productoListado'),
    path('update/<int:pk>',views.ProductoUpdateView.as_view(),name='update'),
    path('borrar/<int:pk>',views.ProductoDeleteView.as_view(),name='borrar'),
    path('formCategoria/',views.formCategoria,name='formCategoria'),
    path('listadoCategoria/',views.listadoCategoria, name='listadoCategoria'),
    path('updateCategoria/<int:pk>',views.CategoriaUpdateView.as_view(),name='updateCategoria'),
    path('borrarCategoria/<int:pk>',views.CategoriaDeleteView.as_view(),name='borrarCategoria'),

]

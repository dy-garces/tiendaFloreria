from django.urls import path
from . import views

urlpatterns = [
    path('buscador', views.ProductoBuscarListView.as_view(), name='buscador'),
    path('<slug:slug>', views.ProductoDetalleView.as_view(),name='producto'),

]

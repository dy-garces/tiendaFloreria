from django.urls import path
from . import views


app_name = 'carrito'

urlpatterns = [
    path('',views.carrito,name='carrito'),
    path('agregar/',views.agregar,name='agregar'),
]



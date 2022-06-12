from django.urls import path
from . import views
urlpatterns = [
    path('<slug:slug>', views.ProductoDetalleView.as_view(),name='producto')
]

from django.urls import path
from . import views
urlpatterns = [
    path('<pk>', views.ProductoDetalleView.as_view(),name='producto')
]

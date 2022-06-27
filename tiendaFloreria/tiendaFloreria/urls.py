"""tiendaFloreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios.views import cambiarpassword, modificarusuario, perfil, perfilusuario, registro, formRegion , RegionDeleteView , RegionUpdateView , listadoRegion, formComuna , ComunaDeleteView, ComunaUpdateView , listadoComuna
from productos.views import PrductoListaView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import productosViewSet
from rest_framework import  routers

router = routers.DefaultRouter()
router.register("productos",productosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PrductoListaView.as_view(),name="home"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('flores/',views.flores,name="flores"),
    path('plantas/',views.plantas,name="plantas"),
    path('arboles/',views.arboles,name="arboles"),
    path('maceteros',views.maceteros,name="maceteros"),
    path('jardineria/',views.jardineria,name="jardineria"),
    path('productos/',include('productos.urls')),
    path('carrito/',include('carrito.urls')),
    path('direcciones/',include('direccion_envio.urls')),
    path('orden/',include('ordenes.urls')),
    path('quienesSomos/',views.quienesSomos,name="quienesSomos"),
    path('contacto/',views.contacto,name="contacto"),
    path('perfilusuario/',perfilusuario,name="perfilusuario"),
    path('registro',registro, name="registro"),
    path('perfil',perfil, name="perfil"),
    path('modificarusuario/<id>',modificarusuario, name="modificarusuario"),
    path('cambiarpassword',cambiarpassword, name="cambiarpassword"),
    path('formRegion/',formRegion ,name='formRegion'),
    path('listadoRegion/',listadoRegion, name='listadoRegion'),
    path('updateRegion/<int:pk>',RegionUpdateView.as_view(),name='updateRegion'),
    path('borrarRegion/<int:pk>',RegionDeleteView.as_view(),name='borrarRegion'),
    
    path('formComuna/',formComuna ,name='formComuna'),
    path('listadoComuna/',listadoComuna, name='listadoComuna'),
    path('updateComuna/<int:pk>',ComunaUpdateView.as_view(),name='updateComuna'),
    path('borrarComuna/<int:pk>',ComunaDeleteView.as_view(),name='borrarComuna'),
    
    
    
    path('api/',include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

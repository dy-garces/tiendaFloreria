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

from productos.views import PrductoListaView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PrductoListaView.as_view(),name="home"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro',views.registro, name="registro"),
    path('flores/',views.flores,name="flores"),
    path('plantas/',views.plantas,name="plantas"),
    path('arboles/',views.arboles,name="arboles"),
    path('maceteros',views.maceteros,name="maceteros"),
    path('jardineria/',views.jardineria,name="jardineria"),
    path('productos/',include('productos.urls')),
    path('carrito/',include('carrito.urls')),
    path('orden/',include('ordenes.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

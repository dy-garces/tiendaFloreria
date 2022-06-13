
from django.urls import reverse


def breadcrumb(productos = True, direccion = False , pago = False, confirmacion = False):
    return [
        
        {'title': 'Productos', 'active':productos , 'url':reverse('ordenes:orden')},
        {'title': 'Direccion', 'active':direccion , 'url':reverse('ordenes:orden')},
        {'title': 'Pago', 'active':pago , 'url':reverse('ordenes:orden')},
        {'title': 'Confirmacio', 'active':confirmacion , 'url':reverse('ordenes:orden')},
        
    ]
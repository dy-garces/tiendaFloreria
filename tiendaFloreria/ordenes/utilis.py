
from django.urls import reverse


def breadcrumb(productos = True, direccion = False , confirmacion = False, pago = False):
    return [
        
        {'title': 'Productos', 'active':productos , 'url':reverse('ordenes:orden')},
        {'title': 'Direccion', 'active':direccion , 'url':reverse('ordenes:direccion')},
        {'title': 'Confirmacio', 'active':confirmacion , 'url':reverse('ordenes:confirmacion')},
        {'title': 'Pago', 'active':pago , 'url':reverse('ordenes:orden')},
        
        
    ]

def destruir_orden(request):
    request.session['orden_id'] = None
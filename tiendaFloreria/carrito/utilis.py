from .models import Carrito


def destruir_carrito(request):
    request.session['carrito_id'] = None
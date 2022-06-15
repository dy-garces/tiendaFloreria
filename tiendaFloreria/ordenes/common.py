from enum import Enum

class OrdenesStatus(Enum):
    CREADO = 'CREADO'
    PAGADO = 'PAGADO'
    COMPLETADO = 'COMPLETADO'
    CANCELADO = 'CANCELADO'
    EMPAQUETADO = 'EMPAQUETADO'
    DESPACHADO = 'DESPACHADO'
    
choices = [( tag, tag.value) for  tag in OrdenesStatus]
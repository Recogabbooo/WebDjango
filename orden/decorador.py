from .utils import funcionOrden
from carts.funciones import funcionCarrito


def validate_cart_and_order(function):
    def wrap(request, *args, **kwargs):

        cart = funcionCarrito(request)
        orden = funcionOrden(cart, request)

        return function(request, cart, orden, *args, **kwargs)
    
    return wrap

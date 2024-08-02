from django.shortcuts import render
from carts.funciones import funcionCarrito
from .models import Orden
from .utils import funcionOrden


def orden(request):
    cart = funcionCarrito(request)
    orden = funcionOrden(cart, request)
    
    return render(request, 'orden/orden.html',{
        'cart':cart
    })
from django.shortcuts import get_object_or_404, redirect, render
from .models import Orden
from .utils import deleteOrden, funcionOrden
from django.contrib.auth.decorators import login_required
from .utils import breadcrumb
from DirEnvio.models import DireccionEnvio
from django.contrib import messages
from carts.funciones import deleteCart, funcionCarrito
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import EmptyQuerySet
from .decorador import validate_cart_and_order

class OrdenViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    template_name = 'orden/ordenes.html'
    
    def get_queryset(self):
        return self.request.user.ordenes_completadas()


@login_required(login_url='login')
@validate_cart_and_order
def orden(request, cart, orden):
    
    return render(request, 'orden/orden.html',{
        'cart':cart,
        'orden':orden,
        'breadcrumb':breadcrumb(),
    })


@login_required(login_url='login')
@validate_cart_and_order
def direccion(request, cart, orden):

    direccion_envio = orden.get_or_set_direccion_envio()
    contDireccion = request.user.direccionenvio_set.count() > 1

    return render(request, 'orden/direccion.html',{
        'cart':cart,
        'orden':orden,
        'direccion_envio': direccion_envio,
        'contDireccion':contDireccion,
        'breadcrumb':breadcrumb,
        
    })


@login_required(login_url='login')
def select_direccion(request):
    direccion_envios = request.user.direccionenvio_set.all()
    return render(request, "orden/select_direccion.html", {
    'breadcrumb':breadcrumb(address=True),
    'direccion_envios': direccion_envios,

    }) 


@login_required(login_url='login')
@validate_cart_and_order
def check_direccion(request,cart,orden, pk):
    direccion_envio = get_object_or_404(DireccionEnvio, pk=pk)

    if request.user.id != direccion_envio.user_id:
        return redirect('index')

    orden.update_direccion_envio(direccion_envio)

    return redirect('direccion')

@login_required(login_url='login')
@validate_cart_and_order
def confirmacion(request, cart, orden):

    direccion_envio = orden.direccion_envio
    if direccion_envio is None:
        return redirect('direccion')

    return render(request, 'orden/confirmacion.html',{
    'cart': cart,
    'orden': orden,
    'direccion_envio': direccion_envio,
    'breadcrumb': breadcrumb(address=True, confirmation=True),
    
    })

@login_required(login_url='login')
@validate_cart_and_order
def cancelar_orden(request, cart, orden):
    
    if request.user.id != orden.user_id:
        return redirect('index')

    orden.cancelar()
    deleteCart(request)
    deleteOrden(request)

    messages.error(request, 'Orden eliminada correctamente')
    return redirect('index')

@login_required(login_url='login')
@validate_cart_and_order
def completado(request, cart, orden):

    if request.user.id != orden.user_id:
        return redirect('index')

    orden.completado()

    deleteCart(request)
    deleteOrden(request)

    messages.success(request, 'Compra completada pronto llegara a destino')
    return redirect('index')
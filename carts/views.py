from django.shortcuts import render
from .models import Cart
from products.models import Product
from .funciones import funcionCarrito
from django.shortcuts import redirect

def cart(request):
    cart = funcionCarrito(request)
    
   
    return render(request, 'carts/cart.html', {
        'cart': cart
    })

def add(request):
    cart = funcionCarrito(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.add(product)
    
    return render(request, 'carts/add.html', {
        'product': product
    })
    
def remove(request):
        cart = funcionCarrito(request)
        product = Product.objects.get(pk=request.POST.get('product_id'))
        
        cart.products.remove(product)

        return redirect('cart')
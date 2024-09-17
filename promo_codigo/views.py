from django.shortcuts import render
from django.http import JsonResponse
from .models import PromoCodigo
from orden.decorador import validate_cart_and_order


@validate_cart_and_order
def validar(request, cart, orden): 
        codigo = request.GET.get('code')
        promo_codigo = PromoCodigo.objects.get_validar(codigo)

        if promo_codigo is None:
            print("HOLA")
            return JsonResponse({
                'status': False,
            }, status = 404)

        orden.aplicarCodigo(promo_codigo)

        return JsonResponse({
            'status': True,
            'codigo': promo_codigo.codigo,
            'descuento': promo_codigo.descuento,
            'total': orden.total
        })
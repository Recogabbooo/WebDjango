from django.shortcuts import render
from django.http import JsonResponse
from .models import PromoCodigo


def validar(request): 
        codigo = request.GET.get('code')
        promo_codigo = PromoCodigo.objects.filter(codigo=codigo).first()

        if promo_codigo is None:
            print("HOLA")
            return JsonResponse({
                'status': False,
            }, status = 404)


        return JsonResponse({
            'status': True,
            'codigo': promo_codigo.codigo,
            'descuento': promo_codigo.descuento
        })
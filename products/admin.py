from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ('titles', 'description', 'price', 'image')
    list_display = ('__str__', 'slug', 'created_at')
              
              
admin.site.register(Product, ProductAdmin)

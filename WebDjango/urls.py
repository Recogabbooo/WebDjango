from django.contrib import admin
from django.urls import path, include
from products.views import ProductListView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',ProductListView.as_view(), name="index" ),
    path('usuarios/login', views.login, name="login"),
    path('usuarios/salir', views.salir, name="salir"),
    path('usuarios/registro', views.registro, name="registro"),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('productos/', include('products.urls')),
    path('carrito/', include('carts.urls')),
    path('orden/', include('orden.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
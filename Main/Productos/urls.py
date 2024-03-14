from django.conf import settings
from django.urls import include, path
from . import views, views_carrito
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name= 'home'),
  path('shop', views.shop, name='shop'),
  path('pedido2', views.pedido_correcto, name = 'pedido2'),
  path('pedido/', views_carrito.pedido, name='pedido'),
  path('carrito/', views_carrito.carrito, name='carrito'),
  path('carrito/agregar/<int:producto_id>/', views_carrito.agregar_al_carrito, name='agregar_al_carrito'),
  path('eliminar_del_carrito/<int:producto_id>/', views_carrito.eliminar_del_carrito, name='eliminar_del_carrito'),
  path('carrito/eliminar/', views_carrito.eliminar_carrito, name='eliminar_carrito'),
  path('carrito/aumentar/<int:detalle_id>/', views_carrito.aumentar_cantidad, name='aumentar_cantidad'),
  path('carrito/disminuir/<int:detalle_id>/', views_carrito.disminuir_cantidad, name='disminuir_cantidad'),
]  
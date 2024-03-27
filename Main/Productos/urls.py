from django.conf import settings
from django.urls import include, path
from . import views, views_carrito
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name= 'home'),
  path('shop', views.shop, name='shop'),
  path('crear_pedido/', views_carrito.crear_pedido, name='crear_pedido'),
  path('pedido/<int:pedido_id>/', views_carrito.vista_pedido, name='vista_pedido'),
  path('carrito/', views_carrito.carrito, name='carrito'),
  path('carrito/agregar/<int:producto_id>/', views_carrito.agregar_al_carrito, name='agregar_al_carrito'),
  path('eliminar_del_carrito/<int:producto_id>/', views_carrito.eliminar_del_carrito, name='eliminar_del_carrito'),
  path('carrito/eliminar/', views_carrito.eliminar_carrito, name='eliminar_carrito'),
  path('carrito/aumentar/<int:detalle_id>/', views_carrito.aumentar_cantidad, name='aumentar_cantidad'),
  path('carrito/disminuir/<int:detalle_id>/', views_carrito.disminuir_cantidad, name='disminuir_cantidad'),
  path('obtener-numero-productos-en-carrito/', views_carrito.obtener_numero_productos_en_carrito, name='obtener_numero_productos_en_carrito'),
  path('buscar/', views_carrito.buscar_productos, name='buscar_productos'),
  path("registro", views.registro, name="registro"),
  path("loginn/", views.loginn, name="loginn"),
      path('logout', views.cerrar, name='logout'),
]  
from django.conf import settings
from django.urls import include, path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    path('carrito/', views.carrito, name='carrito'),
  path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
  path('eliminar_del_carrito/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
  path('carrito/eliminar/', views.eliminar_carrito, name='eliminar_carrito'),
  path('carrito/aumentar/<int:detalle_id>/', views.aumentar_cantidad, name='aumentar_cantidad'),
  path('carrito/disminuir/<int:detalle_id>/', views.disminuir_cantidad, name='disminuir_cantidad'),
]  
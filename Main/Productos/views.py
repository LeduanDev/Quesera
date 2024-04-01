from django.shortcuts import get_object_or_404, render, redirect
from .models import DetallePedido, Pedido, SliderImage
from .models import Producto, DetalleCarrito, Categoria
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import DetailView


def home(request):
    imagen = SliderImage.objects.all()
    productos_especiales = Producto.objects.filter(especial=True)[:10]
    categoria = Categoria.objects.all()
    return render(request, 'principal/home.html', {'imagen': imagen, 'productos': productos_especiales, 'categoria': categoria})


def shop(request):
    categorias = Categoria.objects.all()
    categoria_seleccionada = None
    productos = Producto.objects.all()

    if 'categoria_id' in request.GET:
        categoria_id = request.GET['categoria_id']
        if categoria_id:
            categoria_seleccionada = get_object_or_404(Categoria, id=categoria_id)
            productos = productos.filter(categoria=categoria_seleccionada)

    return render(request, 'principal/shop.html', {'categorias': categorias, 'productos': productos, 'categoria_seleccionada': categoria_seleccionada})


def detalles_producto(request, id):
    producto = get_object_or_404(Producto, pk =id)
    return render(request, 'principal/detalles.html', {'producto' : producto})


# Verificar si el usuario es administrador
def es_admin(user):
    return user.is_staff

@method_decorator(user_passes_test(es_admin), name='dispatch')
class ListaPedidos(ListView):
    model = Pedido
    template_name = 'principal/admin/Pedidos_hechos.html'  # Nombre del template donde mostrarás la lista de pedidos
    context_object_name = 'pedidos'  # Nombre del objeto que pasará a tu template, por ejemplo {{ pedidos }}

    def get_queryset(self):
        # Obtener los pedidos ordenados por fecha de pedido de forma descendente
        return Pedido.objects.all().order_by('-fecha_pedido')


@method_decorator(user_passes_test(es_admin), name='dispatch')
class DetallesPedidoView(DetailView):
    model = Pedido
    template_name = 'principal/admin/detallesP.html'  # Nombre del template donde mostrarás los detalles del pedido
    context_object_name = 'pedido'  # Nombre del objeto que pasará a tu template, por ejemplo {{ pedido }}


from django.shortcuts import get_object_or_404, render, redirect
from .models import DetallePedido, Pedido, SliderImage
from .models import Producto, DetalleCarrito, Categoria
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from Productos.forms import PedidoForm
from .models import Carrito, DetallePedido, Pedido, Producto, DetalleCarrito
from django.template.defaultfilters import floatformat


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



def crear_pedido(request):
    try:
        carrito = Carrito.objects.get(user=request.user)
    except Carrito.DoesNotExist:
        return JsonResponse(
            {
                "mensaje": "Tu carrito está vacío. Por favor, agrega productos antes de proceder al pedido."
            }
        )

    if carrito.productos.count() == 0:
        return JsonResponse(
            {
                "mensaje": "Tu carrito está vacío. Por favor, agrega productos antes de proceder al pedido."
            }
        )

    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.user = request.user  # Asignar el usuario al pedido
            pedido.save()
            for detalle_carrito in carrito.detallecarrito_set.all():
                DetallePedido.objects.create(
                    pedido=pedido,
                    producto=detalle_carrito.producto,
                    cantidad=detalle_carrito.cantidad,
                    precio_unitario=detalle_carrito.producto.precio,
                    precio_total=detalle_carrito.precio_total(),
                )

            carrito.productos.clear()
            carrito.total = 0
            carrito.save()
            return redirect("vista_pedido", pedido_id=pedido.id)
    else:
        form = PedidoForm()

    return render(request, "principal/pedido.html", {"form": form})

def detalles_producto(request, id):
    producto = get_object_or_404(Producto, pk =id)
    return render(request, 'principal/detalles.html', {'producto' : producto})


# Verificar si el usuario es administrador
def es_admin(user):
    return user.is_staff

@login_required
def vista_pedido(request, pedido_id):
    # Verificar si el usuario es administrador
    if request.user.is_staff:
        pedido = get_object_or_404(Pedido, id=pedido_id)
    else:
        pedido = get_object_or_404(Pedido, id=pedido_id, user=request.user)
    
    detalles = DetallePedido.objects.filter(pedido=pedido)
    total_pedido = sum(detalle.precio_total for detalle in detalles)
    return render(
        request,
        "principal/correcto.html",
        {"pedido": pedido, "detalles": detalles, "total_pedido": total_pedido},
    )


@method_decorator(user_passes_test(es_admin), name='dispatch')
class ListaPedidos(ListView):
    model = Pedido
    template_name = 'principal/admin/Pedidos_hechos.html'  # Nombre del template donde mostrarás la lista de pedidos
    context_object_name = 'pedidos'  # Nombre del objeto que pasará a tu template, por ejemplo {{ pedidos }}

    def get_queryset(self):
        # Obtener los pedidos ordenados por fecha de pedido de forma descendente
        return Pedido.objects.all().order_by('-fecha_pedido')


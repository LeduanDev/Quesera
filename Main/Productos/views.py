from django.shortcuts import get_object_or_404, render, redirect
from .models import DetallePedido, Pedido, SliderImage, informacion
from .models import Producto, DetalleCarrito, Categoria
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from Productos.forms import PedidoForm
from .models import Carrito, DetallePedido, Pedido, Producto, DetalleCarrito
from django.template.defaultfilters import floatformat
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Pedido

def home(request):
    imagen = SliderImage.objects.all()
    productos_especiales = Producto.objects.filter(especial=True)[:10]
    categoria = Categoria.objects.all()
    return render(request, 'principal/home.html', {'imagen': imagen, 'productos': productos_especiales, 'categoria': categoria})



def shop(request):
    categorias = Categoria.objects.all()
    categoria_seleccionada = None

    # Obtener productos de la caché o realizar la consulta si no está en caché
    productos_cache_key = 'productos_tienda'
    productos = cache.get(productos_cache_key)
    if not productos:
        productos = Producto.objects.all()
        cache.set(productos_cache_key, productos)

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
    producto = get_object_or_404(Producto, pk=id)

    # Obtener productos relacionados de la caché o realizar la consulta si no está en caché
    productos_relacionados_cache_key = f'productos_relacionados_{producto.categoria.id}'
    productos_relacionados = cache.get(productos_relacionados_cache_key)
    if not productos_relacionados:
        productos_relacionados = Producto.objects.filter(categoria=producto.categoria).exclude(id=producto.id).order_by('?')[:8]
        cache.set(productos_relacionados_cache_key, productos_relacionados)

    return render(request, 'principal/detalles.html', {'producto': producto, 'productos_relacionados': productos_relacionados})



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




class ListaPedidos(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'principal/admin/Pedidos_hechos.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        # Si el usuario es un administrador, mostrar todos los pedidos
        if self.request.user.is_staff:
            return Pedido.objects.all().order_by('-fecha_pedido')
        # Si el usuario no es un administrador, mostrar solo sus propios pedidos
        else:
            return Pedido.objects.filter(user=self.request.user).order_by('-fecha_pedido')



def base_view(request):
    # Consulta el modelo informacion
    info = informacion.objects.first()  # Suponiendo que solo hay un registro
    return render(request, 'base.html', {'info': info})
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from Productos.forms import PedidoForm
from Productos.templatetags.my_filters import formato_moneda
from .models import Carrito, Categoria, DetallePedido, Pedido, Producto, DetalleCarrito
from django.db import transaction
from django.template.defaultfilters import floatformat
from django.db.models import Q


@login_required
def carrito(request):
    # Obtenemos el carrito asociado con el usuario actual
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    if created:
        request.session["carrito_id"] = carrito.id
    return render(request, "principal/carrito.html", {"carrito": carrito})

@transaction.atomic
def agregar_al_carrito(request, producto_id):
    if not request.user.is_authenticated:
        return JsonResponse(
            {"mensaje": "Debes iniciar sesión para agregar productos al carrito."},
            status=401,
        )

    producto = get_object_or_404(Producto, pk=producto_id)
    
    # Verificar disponibilidad del producto
    if not producto.disponible:
        return JsonResponse(
            {"mensaje": "El producto no está disponible para agregar al carrito."},
            status=400,
        )

    carrito, created = Carrito.objects.get_or_create(user=request.user)
    detalle_carrito, created = DetalleCarrito.objects.get_or_create(
        carrito=carrito, producto=producto
    )

    # Obtener la cantidad del formulario
    cantidad = int(request.POST.get('cantidad', 1))

    # Actualizar la cantidad del detalle del carrito
    detalle_carrito.cantidad = cantidad
    detalle_carrito.save()

    # Calcular el total del carrito
    carrito.calcular_total()

    # Devolver una respuesta JSON
    return JsonResponse(
        {
            "mensaje": "El producto se ha agregado al carrito.",
            "cantidad": cantidad,  # Devolver la cantidad actualizada
            "total_carrito": carrito.total,  # Devolver el total del carrito
        }
    )


from django.template.defaultfilters import floatformat

def aumentar_cantidad(request, detalle_id):
    detalle = get_object_or_404(DetalleCarrito, pk=detalle_id)
    detalle.cantidad += 1
    detalle.save()  

    # Calcular el precio total del detalle multiplicando la cantidad por el precio unitario
    precio_total = detalle.producto.precio * detalle.cantidad

    detalle.carrito.calcular_total()
    total_carrito = detalle.carrito.total
    numero_productos = detalle.carrito.detallecarrito_set.count()

    return JsonResponse(
        {
            "cantidad": detalle.cantidad,
            "numero_productos": numero_productos,
            "total": total_carrito,
            "precio_total": formato_moneda(precio_total),
        }
    )

def disminuir_cantidad(request, detalle_id):
    detalle = get_object_or_404(DetalleCarrito, pk=detalle_id)
    if detalle.cantidad > 1:
        detalle.cantidad -= 1
        detalle.save()
        eliminado_completamente = False
    else:
        detalle.delete()
        eliminado_completamente = True

    # Calcular el precio total del detalle multiplicando la cantidad por el precio unitario
    precio_total = detalle.producto.precio * detalle.cantidad

    detalle.carrito.calcular_total()
    total_carrito = detalle.carrito.total
    numero_productos = detalle.carrito.detallecarrito_set.count()

    return JsonResponse(
        {
            "cantidad": detalle.cantidad,
            "numero_productos": numero_productos,
            "total": total_carrito,
            "precio_total": formato_moneda(precio_total),
            "eliminado_completamente": eliminado_completamente,
        }
    )


def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Obtenemos el carrito asociado con el usuario actual
    carrito = Carrito.objects.get(user=request.user)

    try:
        detalle_carrito = DetalleCarrito.objects.get(carrito=carrito, producto=producto)
        detalle_carrito.delete()
        carrito.calcular_total()
    except DetalleCarrito.DoesNotExist:
        pass

    return redirect("carrito")


def eliminar_carrito(request):
    # Obtenemos el carrito asociado con el usuario actual
    carrito = Carrito.objects.get(user=request.user)

    # Eliminamos el carrito
    carrito.delete()

    return redirect("carrito")


def obtener_numero_productos_en_carrito(request):
    if request.user.is_authenticated:
        try:
            carrito = Carrito.objects.get(user=request.user)
            numero_productos = carrito.detallecarrito_set.count()
        except Carrito.DoesNotExist:
            numero_productos = 0
    else:
        numero_productos = 0

    return JsonResponse({"numero_productos": numero_productos})


def buscar_productos(request):
    query = request.GET.get("q")
    palabras_clave = query.split() if query else []
    categorias = Categoria.objects.all()
    # Inicializar una consulta vacía
    consulta = Q()

    # Agregar condiciones de búsqueda para cada palabra clave
    for palabra in palabras_clave:
        consulta |= (
            Q(nombre__icontains=palabra)
            | Q(categoria__nombre__icontains=palabra)
            # Asegúrate de que "descripcion" sea un campo en tu modelo Producto
        )

    # Ejecutar la consulta
    productos = Producto.objects.filter(consulta)

    return render(
        request, "principal/busqueda.html", {"productos": productos, "query": query, "categorias": categorias}
    )

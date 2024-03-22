from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from Productos.forms import PedidoForm
from .models import Carrito, DetallePedido, Pedido, Producto, DetalleCarrito
from django.db import transaction
from django.template.defaultfilters import floatformat
from django.db.models import Q



def carrito(request):
    # Obtenemos el ID del carrito de la sesión del usuario
    carrito_id = request.session.get("carrito_id")

    # Si no hay un ID de carrito en la sesión, creamos uno nuevo
    if not carrito_id:
        carrito = Carrito.objects.create()
        request.session["carrito_id"] = carrito.id
    else:
        # Si hay un ID de carrito, obtenemos el carrito asociado
        carrito = Carrito.objects.get(id=carrito_id)

    return render(request, "principal/carrito.html", {"carrito": carrito})




def crear_pedido(request):
    carrito_id = request.session.get("carrito_id")
    carrito = Carrito.objects.get(id=carrito_id)

    if carrito.productos.count() == 0:
        return JsonResponse(
            {
                "mensaje": "Tu carrito está vacío. Por favor, agrega productos antes de proceder al pedido."
            }
        )
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            carrito_id = request.session.get("carrito_id")
            if carrito_id:
                carrito = Carrito.objects.get(id=carrito_id)
                for detalle_carrito in carrito.detallecarrito_set.all():  # Acceder a los detalles del carrito
                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=detalle_carrito.producto,
                        cantidad=detalle_carrito.cantidad,
                        precio_unitario=detalle_carrito.producto.precio,
                        precio_total=detalle_carrito.precio_total()
                    )

                carrito.productos.clear()
                carrito.total = 0
                carrito.save()
            return redirect('vista_pedido', pedido_id=pedido.id)
    else:
        form = PedidoForm()
    return render(request, 'principal/pedido.html', {'form': form})



def vista_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    total_pedido = sum(detalle.precio_total for detalle in detalles)
    return render(request, 'principal/correcto.html', {'pedido': pedido, 'detalles': detalles, 'total_pedido': total_pedido})




def vista_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    total_pedido = sum(detalle.precio_total for detalle in detalles)
    return render(request, 'principal/correcto.html', {'pedido': pedido, 'detalles': detalles, 'total_pedido': total_pedido})


@transaction.atomic
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito_id = request.session.get("carrito_id")
    if not carrito_id:
        carrito = Carrito.objects.create()
        request.session["carrito_id"] = carrito.id
    else:
        carrito = Carrito.objects.get(id=carrito_id)

    # Ahora que carrito ha sido asignado correctamente, podemos obtener el número de productos en el carrito
    numero_productos = carrito.detallecarrito_set.count()

    detalle_carrito, created = DetalleCarrito.objects.get_or_create(
        carrito=carrito, producto=producto
    )

    # Actualizamos el número de productos después de agregar el nuevo detalle de carrito
    numero_productos = carrito.detallecarrito_set.count()

    if not created:
        return JsonResponse(
            {"mensaje": "El producto ya está en el carrito."}, status=400
        )

    else:
        detalle_carrito.cantidad = 1
        detalle_carrito.save()
        carrito.calcular_total()
        return JsonResponse(
            {
                "mensaje": "El producto se ha agregado al carrito.",
                "numero_productos": numero_productos,
            }
        )


def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Obtenemos el ID del carrito de la sesión del usuario
    carrito_id = request.session.get("carrito_id")

    # Si no hay un ID de carrito en la sesión, no hay nada que eliminar
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        try:
            detalle_carrito = DetalleCarrito.objects.get(
                carrito=carrito, producto=producto
            )
            detalle_carrito.delete()
            carrito.calcular_total()
        except DetalleCarrito.DoesNotExist:
            pass

    return redirect("carrito")


def eliminar_carrito(request):
    # Obtenemos el ID del carrito de la sesión del usuario
    carrito_id = request.session.get("carrito_id")

    # Si hay un ID de carrito en la sesión, lo eliminamos
    if carrito_id:
        Carrito.objects.filter(id=carrito_id).delete()
        # Eliminamos también el ID del carrito de la sesión
        del request.session["carrito_id"]

    return redirect("carrito")


def aumentar_cantidad(request, detalle_id):
    detalle = get_object_or_404(DetalleCarrito, pk=detalle_id)
    detalle.cantidad += 1
    detalle.save()

    # Calcular el precio total del detalle multiplicando la cantidad por el precio unitario
    precio_total = detalle.producto.precio * detalle.cantidad

    detalle.carrito.calcular_total()
    total_carrito = detalle.carrito.total
    numero_productos = detalle.carrito.detallecarrito_set.count()

    return JsonResponse({
        "cantidad": detalle.cantidad,
        "numero_productos": numero_productos,
        "total": total_carrito,
        "precio_total": floatformat(precio_total, 2),  # Formatear el precio total con dos decimales
    })

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

    return JsonResponse({
        "cantidad": detalle.cantidad,
        "numero_productos": numero_productos,
        "total": total_carrito,
        "precio_total": floatformat(precio_total, 2),  # Formatear el precio total con dos decimales
        "eliminado_completamente": eliminado_completamente,
    })



def obtener_numero_productos_en_carrito(request):
    carrito_id = request.session.get("carrito_id")
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        numero_productos = carrito.detallecarrito_set.count()
    else:
        numero_productos = 0
    return JsonResponse({"numero_productos": numero_productos})




def buscar_productos(request):
    query = request.GET.get('q')
    palabras_clave = query.split() if query else []

    # Inicializar una consulta vacía
    consulta = Q()

    # Agregar condiciones de búsqueda para cada palabra clave
    for palabra in palabras_clave:
        consulta |= (
            Q(nombre__icontains=palabra) |
            Q(categoria__nombre__icontains=palabra) 
          # Asegúrate de que "descripcion" sea un campo en tu modelo Producto
        )

    # Ejecutar la consulta
    productos = Producto.objects.filter(consulta)

    return render(request, 'principal/shop.html', {'productos': productos, 'query': query})

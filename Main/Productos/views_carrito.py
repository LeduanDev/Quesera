from django.shortcuts import get_object_or_404, render, redirect
from .models import SliderImage
from .models import Carrito, Producto, DetalleCarrito, Categoria


def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    # Obtenemos el ID del carrito de la sesión del usuario
    carrito_id = request.session.get('carrito_id')
    
    # Si no hay un ID de carrito en la sesión, creamos uno nuevo
    if not carrito_id:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
    else:
        # Si hay un ID de carrito, obtenemos el carrito asociado
        carrito = Carrito.objects.get(id=carrito_id)

    # Verificar si el producto ya está en el carrito
    detalle_carrito, created = DetalleCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        # Si el producto ya está en el carrito, no lo agregamos de nuevo
        # Puedes manejar esto de la manera que desees, aquí simplemente redireccionamos de nuevo a la página del carrito
        return redirect('carrito')
    
    detalle_carrito.cantidad += 0
    detalle_carrito.save()
    carrito.calcular_total()
    return redirect('carrito')



def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    # Obtenemos el ID del carrito de la sesión del usuario
    carrito_id = request.session.get('carrito_id')
    
    # Si no hay un ID de carrito en la sesión, no hay nada que eliminar
    if carrito_id:
        carrito = Carrito.objects.get(id=carrito_id)
        try:
            detalle_carrito = DetalleCarrito.objects.get(carrito=carrito, producto=producto)
            detalle_carrito.delete()
            carrito.calcular_total()
        except DetalleCarrito.DoesNotExist:
            pass

    return redirect('carrito')



def eliminar_carrito(request):
    # Obtenemos el ID del carrito de la sesión del usuario
    carrito_id = request.session.get('carrito_id')
    
    # Si hay un ID de carrito en la sesión, lo eliminamos
    if carrito_id:
        Carrito.objects.filter(id=carrito_id).delete()
        # Eliminamos también el ID del carrito de la sesión
        del request.session['carrito_id']

    return redirect('carrito')


def carrito(request):
    # Obtenemos el ID del carrito de la sesión del usuario
    carrito_id = request.session.get('carrito_id')
    
    # Si no hay un ID de carrito en la sesión, creamos uno nuevo
    if not carrito_id:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
    else:
        # Si hay un ID de carrito, obtenemos el carrito asociado
        carrito = Carrito.objects.get(id=carrito_id)
    
    return render(request, 'principal/carrito.html', {'carrito': carrito})


def aumentar_cantidad(request, detalle_id):
    detalle = get_object_or_404(DetalleCarrito, pk=detalle_id)
    detalle.cantidad += 1
    detalle.save()
    detalle.carrito.calcular_total()
    return redirect('carrito')

def disminuir_cantidad(request, detalle_id):
    detalle = get_object_or_404(DetalleCarrito, pk=detalle_id)
    if detalle.cantidad > 1:
        detalle.cantidad -= 1
        detalle.save()
    else:
        detalle.delete()
    detalle.carrito.calcular_total()
    return redirect('carrito')
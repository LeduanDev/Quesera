from django.shortcuts import get_object_or_404, render, redirect
from .models import SliderImage
from .models import Carrito, Producto, DetalleCarrito, Categoria




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






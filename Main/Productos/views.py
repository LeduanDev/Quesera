from django.shortcuts import get_object_or_404, render, redirect
from .models import SliderImage
from .models import Carrito, Producto, DetalleCarrito, Categoria

# def home(request):
#     imagen = SliderImage.objects.all()
#     producto =  Producto.objects.all()
#     categoria = Categoria.objects.all()
    
#     return render(request, 'principal/home.html', {'imagen': imagen, 'producto': producto, 'categoria' : categoria})

def home(request):
    imagen = SliderImage.objects.all()
    # Esto solo carga los productos que esten marcados como especiales, en este caso carga al menos 10 como maximo
    productos_especiales = Producto.objects.filter(especial=True)[:10]
    categoria = Categoria.objects.all()
    
    return render(request, 'principal/home.html', {'imagen': imagen, 'productos': productos_especiales, 'categoria': categoria})


def shop(request):
    imagen = SliderImage.objects.all()
    producto =  Producto.objects.all()
    categoria = Categoria.objects.all()

    return render(request, 'principal/shop.html')




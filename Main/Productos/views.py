from django.shortcuts import get_object_or_404, render, redirect
from .models import SliderImage
from .models import Carrito, Producto, DetalleCarrito, Categoria



def home(request):
    imagen = SliderImage.objects.all()
    # Esto solo carga los productos que esten marcados como especiales, en este caso carga al menos 10 como maximo
    productos_especiales = Producto.objects.filter(especial=True)[:10]
    categoria = Categoria.objects.all()
  
    
    return render(request, 'principal/home.html', {'imagen': imagen, 'productos': productos_especiales, 'categoria': categoria})



def shop(request):
    imagen = SliderImage.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    return render(request, 'principal/shop.html', {'imagen': imagen, 'categorias': categorias, 'productos': productos})





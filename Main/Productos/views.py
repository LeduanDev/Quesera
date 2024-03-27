from django.shortcuts import get_object_or_404, render, redirect

from Productos.forms import SignupForm
from .models import SliderImage
from .models import Carrito, Producto, DetalleCarrito, Categoria
from django.http import HttpResponse
from django.urls import reverse

from django.http import JsonResponse
from MySQLdb import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache


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
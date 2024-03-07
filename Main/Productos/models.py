from django.db import models


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images', null=False)
    title = models.CharField(max_length=100, null= True)
    description = models.TextField()

    def __str__(self):
        return self.title
   
class Categoria(models.Model):
    id =  models.AutoField(primary_key=True)
    nombre =  models.CharField(max_length=40, verbose_name = "Nombre de la categoria")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre del Producto")
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField( upload_to='imagenes/', verbose_name="Imagen", null=True, blank=True)
    especial = models.BooleanField(default=False, verbose_name="Producto especial")

    def __str__(self):
      return self.nombre
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete(using=using, keep_parents=keep_parents)


class Carrito(models.Model):
    productos = models.ManyToManyField('Producto', through='DetalleCarrito')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_total(self):
        self.total = sum(detalle.precio_total() for detalle in self.detallecarrito_set.all())
        self.save()


class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def precio_total(self):
        return self.producto.precio * self.cantidad
    
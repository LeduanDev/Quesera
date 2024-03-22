# forms.py
from django import forms

from Productos.models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre',  'direccion', 'telefono']

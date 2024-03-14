# forms.py
from django import forms

class PedidoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    numero = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)

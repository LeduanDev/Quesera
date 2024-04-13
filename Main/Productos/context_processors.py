from .models import informacion

def informacion_global(request):
    # Obtener la información del modelo 'informacion'
    info = informacion.objects.first()  # O consulta que obtiene la información que necesitas

    # Retornar el contexto
    return {'info': info}

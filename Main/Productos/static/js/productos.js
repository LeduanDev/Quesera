
// Función para manejar la petición AJAX de agregar al carrito
function agregarAlCarrito(producto_id, cantidad) {
    $.ajax({
        type: "POST",
        url: agregarAlCarritoURL.replace('0', producto_id),
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            producto_id: producto_id,
            cantidad: cantidad 
        },
        dataType: "json"
    })
    .then(response => {
        // Llama a la función para actualizar el número de productos en el carrito
        actualizarContadorProductos();
        
        // Muestra el mensaje de éxito en una alerta
        mostrarMensajeExito(response.mensaje);
    })
    .catch(error => {
        console.error('Error:', error);
        if (error.status === 401) {
            // Usuario no autenticado
            mostrarMensajeError(error.responseJSON.mensaje);
        } else if (error.status === 400) {
            // Producto ya en el carrito
            mostrarMensajeError(error.responseJSON.mensaje);
        } else {
            // Otro tipo de error
            mostrarMensajeError('Hubo un error al procesar su solicitud.');
        }
    });
}

// Función para mostrar un mensaje de éxito
function mostrarMensajeExito(mensaje) {
    Swal.fire({
        icon: 'success',
        title: 'Éxito',
        text: mensaje,
        timer: 2000, // Auto-cerrar después de 2 segundos
        timerProgressBar: true,
        showConfirmButton: false
    });
}

// Función para mostrar un mensaje de error
function mostrarMensajeError(mensaje) {
    Swal.fire({
        icon: 'error',
        title: 'Error',
        text: mensaje,
        timer: 2000,
        timerProgressBar: true,
        showConfirmButton: false
    });
}

// Manejador de eventos para el botón "Agregar al carrito"
document.querySelectorAll('.agregar-al-carrito').forEach(boton => {
    boton.addEventListener('click', function() {
        const producto_id = $(this).closest('form').data('producto-id'); // Obtener el ID del producto
        const cantidad = $(this).closest('form').find('.cantidad').val(); // Obtener la cantidad seleccionada
        agregarAlCarrito(producto_id, cantidad); // Llamar a la función agregarAlCarrito con el ID del producto y la cantidad
    });
});




function actualizarContadorProductos() {
    $.ajax({
        type: "GET",
        url: obtenerNumeroProductosURL,
        dataType: "json",
        success: function(response) {
            $("#numero-productos-carrito").text(response.numero_productos);
        },
        error: function(xhr, errmsg, err) {
            console.error("Error al obtener el número de productos en el carrito.");
        }
    });
 }
 
 
 $(document).ready(function() {
    actualizarContadorProductos();
 });
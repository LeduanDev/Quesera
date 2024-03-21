function agregarProductoAlCarrito(productoId) {
    fetch(`/carrito/agregar/${productoId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': obtenerCSRFToken(),
            'Content-Type': 'application/json'
        },
        credentials: 'same-origin'
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.json().then(data => {
                // Muestra el mensaje de error en una alerta
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: data.mensaje,
                    timer: 2000, // Auto-cerrar después de 2 segundos
                    timerProgressBar: true,
                    showConfirmButton: false
                });
                throw new Error(data.mensaje); // Lanza un error para capturarlo en el catch
            });
        }
    })
    .then(data => {
        // Llamar a la función para actualizar el número de productos en el carrito
        actualizarNumeroProductosCarrito();
        
        // Muestra el mensaje de éxito en una alerta
        Swal.fire({
            icon: 'success',
            title: 'Éxito',
            text: data.mensaje,
            timer: 2000, // Auto-cerrar después de 2 segundos
            timerProgressBar: true,
            showConfirmButton: false
        });
    })
    .catch(error => {
        console.error('Error:', error);
        // Muestra el mensaje de error en una alerta
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: error.message, // Accede al mensaje de error a través de error.message
            timer: 2000, // Auto-cerrar después de 2 segundos
            timerProgressBar: true,
            showConfirmButton: false
        });
    });
}

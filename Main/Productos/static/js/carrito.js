document.addEventListener('DOMContentLoaded', function() {
    // Agregar eventos click a los botones de aumentar y disminuir cantidad
    document.querySelectorAll('.cantidad-form').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Evitar que el formulario se envíe de forma tradicional
            
            const detalleId = form.dataset.detalleId;
            const action = form.action;
            
            fetch(action, {
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
                    throw new Error('Error al aumentar/disminuir la cantidad');
                }
            })
            .then(data => {
                // Actualizar la cantidad mostrada en el detalle del carrito
                const detalleElement = document.querySelector(`.detalle-carrito[data-detalle-id="${detalleId}"]`);
                detalleElement.querySelector('.cantidad').textContent = data.cantidad;
            
                // Actualizar el precio total por unidad del producto
                detalleElement.querySelector('.precio-total').textContent = data.precio_total;
            
                // Actualizar el contador de productos en el carrito
                actualizarNumeroProductosCarrito();
            
                // Verificar si el campo 'total' está presente en la respuesta JSON
                if ('total' in data) {
                    // Formatear el precio total del carrito con el símbolo de la moneda correspondiente
                    const formattedTotal = new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP' }).format(data.total);
                    // Actualizar el total neto del carrito
                    document.getElementById('total-neto').textContent = formattedTotal;
                } else {
                    console.error('El campo "total" no está presente en la respuesta JSON');
                }
                
                // Verificar si el detalle se ha eliminado completamente
                if (data.eliminado_completamente) {
                    detalleElement.remove(); // Eliminar visualmente el detalle del carrito
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});


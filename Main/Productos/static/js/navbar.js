document.addEventListener('DOMContentLoaded', function() {
    const botonesAgregarCarrito = document.querySelectorAll('.agregar-al-carrito');
    botonesAgregarCarrito.forEach(boton => {
    boton.addEventListener('click', function() {
        const productoId = boton.dataset.productoId;
        agregarProductoAlCarrito(productoId);
    });
    });
    });
    
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
                text: data.mensaje,
                timer: 2000, // Auto-cerrar después de 2 segundos
                timerProgressBar: true,
                showConfirmButton: false
            });
        });
    }
    
    
    function obtenerCSRFToken() {
    const cookieValue = document.cookie.match(/csrftoken=([^ ;]+)/)[1];
    return cookieValue;
    }
    

/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/* Menu show */
navToggle.addEventListener('click', () =>{
   navMenu.classList.add('show-menu')
})

/* Menu hidden */
navClose.addEventListener('click', () =>{
   navMenu.classList.remove('show-menu')
})

/*=============== SEARCH ===============*/
const search = document.getElementById('search'),
      searchBtn = document.getElementById('search-btn'),
      searchClose = document.getElementById('search-close')

/* Search show */
searchBtn.addEventListener('click', () =>{
   search.classList.add('show-search')
})

/* Search hidden */
searchClose.addEventListener('click', () =>{
   search.classList.remove('show-search')
})


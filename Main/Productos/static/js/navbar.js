/*=============== SHOW MENU ===============*/
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
          nav = document.getElementById(navId)
 
    toggle.addEventListener('click', () =>{
     
        nav.classList.toggle('show-menu')
       
        toggle.classList.toggle('show-icon')
    })
 }
 
 showMenu('nav-toggle','nav-menu')
 
 /*=============== SHOW DROPDOWN MENU ===============*/
 const dropdownItems = document.querySelectorAll('.dropdown__item')
 

 dropdownItems.forEach((item) =>{
     const dropdownButton = item.querySelector('.dropdown__button') 
 
  
     dropdownButton.addEventListener('click', () =>{
         const showDropdown = document.querySelector('.show-dropdown')
         toggleItem(item)
 
         if(showDropdown && showDropdown!== item){
             toggleItem(showDropdown)
         }
     })
 })
 

 const toggleItem = (item) =>{
     // 3.1. Select each dropdown content
     const dropdownContainer = item.querySelector('.dropdown__container')
 
  
     if(item.classList.contains('show-dropdown')){
         dropdownContainer.removeAttribute('style')
         item.classList.remove('show-dropdown')
     } else{
        
         dropdownContainer.style.height = dropdownContainer.scrollHeight + 'px'
         item.classList.add('show-dropdown')
     }
 }

 const mediaQuery = matchMedia('(min-width: 1118px)'),
       dropdownContainer = document.querySelectorAll('.dropdown__container')

 const removeStyle = () =>{

     if(mediaQuery.matches){
       
         dropdownContainer.forEach((e) =>{
             e.removeAttribute('style')
         })
 
         //
         dropdownItems.forEach((e) =>{
             e.classList.remove('show-dropdown')
         })
     }
 }
 



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
    
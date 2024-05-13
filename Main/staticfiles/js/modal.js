  // Obtener el botón de abrir modal
  const openModalButton = document.getElementById('openModalButton');
  // Obtener el modal
  const modal = document.querySelector('.modal');
  // Obtener el botón de cerrar el modal
  const closeModal = document.getElementById('closeModal');

  // Función para mostrar el modal
  function showModal() {
    modal.style.display = 'block';
  }

  // Función para ocultar el modal
  function hideModal() {
    modal.style.display = 'none';
  }

  // Evento clic en el botón de abrir modal
  openModalButton.addEventListener('click', showModal);

  // Evento clic en el botón de cerrar modal
  closeModal.addEventListener('click', hideModal);

  // Evento clic fuera del modal para cerrarlo
  window.addEventListener('click', function(event) {
    if (event.target === modal) {
      hideModal();
    }
  });



  
  const togglePassword = document.getElementById('togglePassword');
  const password = document.getElementById('password');
  const lockIcon = document.getElementById('lockIcon');

  let isPasswordVisible = false;

  togglePassword.addEventListener('click', function() {
      isPasswordVisible = !isPasswordVisible;
      const type = isPasswordVisible ? 'text' : 'password';
      password.setAttribute('type', type);
      lockIcon.innerHTML = isPasswordVisible ?
          `<svg id="lockOpenIcon" class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 2c-1.1 0-2 .9-2 2v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-2V4c0-1.1-.9-2-2-2zM8 8h4v2H8V8zm2 10a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
          </svg>` :
          `<svg id="lockIcon" class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path d="M3 8V6a5 5 0 0110 0v2h2V6a7 7 0 00-14 0v2h2zm2 4v3a1 1 0 001 1h8a1 1 0 001-1v-3H5zm7-4h2v2h-2V8zm-4 0h2v2H8V8zm-2 0H4v2h2V8zm4 0h2v2h-2V8z" />
          </svg>`;
  });
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
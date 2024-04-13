// Obtener el modal y el botón de cierre
var modal = document.getElementById("myModal");
var btn = document.getElementById("openModal");
var span = document.getElementsByClassName("close")[0];

// Cuando se presiona el botón, abrir el modal
btn.onclick = function() {
  modal.style.display = "block";
}

// Cuando se presiona en la X, cerrar el modal
span.onclick = function() {
  modal.style.display = "none";
}

// Cuando el usuario hace clic fuera del modal, cerrar el modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

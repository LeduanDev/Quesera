
// Función para manejar el envío del formulario de inicio de sesión
$(document).ready(function() {
    $("#login-form").submit(function(e) {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: $(this).attr("action"),
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    window.location.href = homeURL;
                } else {
                    $("#error-message").text("Usuario o contraseña incorrectos").show();
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log(xhr.responseText);
            }
        });
    });
});
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

/*=============== LOGIN ===============*/
const login = document.getElementById('login'),
      loginBtn = document.getElementById('login-btn'),
      loginClose = document.getElementById('login-close')

/* Login show */
loginBtn.addEventListener('click', () =>{
   login.classList.add('show-login')
})

/* Login hidden */
loginClose.addEventListener('click', () =>{
   login.classList.remove('show-login')
})


// contador de productos en el carrito

$(document).ready(function () {
   $("#login-form").submit(function (e) {
       e.preventDefault();

       $.ajax({
           type: "POST",
           url: loginFormActionURL,
           data: $(this).serialize(),
           success: function (response) {
               if (response.success) {
                   window.location.href = "{% url 'home' %}";
               } else {
                   $("#error-message").text("Usuario o contraseña incorrectos ").show();
               }
           },
           error: function (xhr, textStatus, errorThrown) {
               console.log(xhr.responseText);
           }
       });
   });
});
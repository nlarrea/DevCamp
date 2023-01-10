# HEAD

El apartado *head* está estructurado de la siguiente manera:

* `<meta charset="UTF-8">`: información para la página, indicando el tipo de codificación.

* `<title>`: contiene el título de la página, en este caso, **CodePen**.

* `<script>`: un script importado para poder utilizar los iconos de la página [FontAwesome](https://fontawesome.com/).

* `<link>`: importación de los tipos de fuentes utilizadas en CSS para dar estilo a los textos, así como la importación de las páginas CSS para estilar la web en general.

<br><hr><br>

# BODY

El *body* está estructurado de la siguiente manera:

* `<header>` con clase **navigation-wrapper**: contiene el logo, los links de navegación y botones para crear contenido, buscarlo, e iniciar sesión y registrarse.

  * `<div>` con clase **logo-links-wrapper**: contiene el logo y los links de navegación.

    * `<div>` con clase **logo-column**: contiene la imagen del logo de la página.

	* `<div>` con clase **links-column**: contiene el texto *EXPLORE* junto con los links de navegación.

	  * `<div>` con clase **explore**: un texto que explica que debajo se encuentran los elementos de exploración.

	  * `<nav>` con clase **links-wrapper**: en su interior se encuentran los `<div>` con clases **nav-link** y **spark-chevron**, es decir, los links con los que navegar.

  * `<div>` con clase **create-login-signup**: divisor que contiene los elementos referidos a crear y buscar contenido, así como el de inicio de sesión y regustrarse.

    * `<div>` con clase **create-wrapper**, el cual contiene un botón con clase **grey-btn**, que tiene un `span` con el texto del botón y un icono.

	* `<div>` con clase **search-icon**: contiene un link que encierra a un icono con forma de lupa.

	* `<button>` con clase **grey-btn**: es el botón encargado del inicio de sesión.

	* `<button>` con clase **grey-btn**: es el botón encargado de registrar al usuario en la web.

<br>

* `<section>` con clase **features-section**: se encarga de contener todas las características o resumen de la web de esta página de inidio.

  * `<div>` con clase **descritpion-section**: contiene texto, una imagen (emoji) y botones en su interior.

    * `<div>` con clase **text-content**: contiene dos divisiones:

	  * **top-header**: contiene el texto superior y la imagen de un emoji.

	  * **bottom-header**: contiene el texto inferior.

	* `<div>` con clase **buttons-wrapper**: contiene dos botones, el primero con clase **green-btn**, y el segundo con clase **black-btn**.

  * `<div>` con clase **projects-section**: utilizado para encerrar el texto y la imagen de la sección derecha de la página.

    * `<span>` con clase **img-header**: contiene el texto situado en la parte superior de la imagen, el cuál también está formado por un link.

	* `<img>` que contiene la imagen mostrada.

<br>

* `<nav>` con clase **codepen-for-wrapper**: contiene cuatro links, `<a>` con clase **codepen-for-item**.

<br>

* `<div>` con clase **page-end**, un elemento usado para añadir ese fondo gris al final de la página.

<br><hr><br>

* [Volver a la página README principal.](../README.md)
* [Ir al archivo README-css](../css/README-css.md)
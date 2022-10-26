# HEAD

El apartado *head* está estructurado de la siguiente manera:

* `<meta charset="UTF-8">`: información para la página, indicando el tipo de codificación.

* `<title>`: contiene el título de la página, **CodePen**.

* `<script>`: un kit importado para poder utilizar los iconos de la página [FontAwesome](https://fontawesome.com/).

* `<link>`: importación de los tipos de fuentes utilizadas en CSS para dar estilo a los textos, así como la importación de las páginas CSS creadas para estilar la web en general.

<br><hr><br>

# BODY

El *body* está estructurado de la siguiente manera:

* `<header>` con clase **navigation-wrapper**: contiene el logo, los links de navegación y botones para crear contenido, buscarlo, e iniciar sesión y registrarse.

  * `<div>` con clase **logo-links-wrapper**: contiene el logo y los links de navegación.

    * `<div>` con clase **logo-column**: contiene la imagen del logo de la página.

	* `<nav>` con clase **links-column**: contiene el texto *EXPLORE* junto con los links de navegación.

	  * `<div>` con clase **explore**: un span que explica que debajo se encuentran los elementos de exploración.

	  * `<div>` con clase **links-wrapper**: en su interior se encuentran los `<div>` con clases **nav-link** y **spark-chevron**, es decir, los links con los que navegar.

  * `<div>` con clase **create-login-signup**: divisor que contiene los elementos referidos a crear y buscar contenido, así como el de inicio de sesión y regustrarse.

    * `<div>` con clase **create-wrapper**, el cual contiene un botón con clase **grey-btn**, que tiene un `span` con el texto del botón y un icono.

	* `<div>` con clase **search-wrapper**: contiene un link que encierra a un icono con forma de lupa.

	* `<div>` con clase **login-wrapper**: bontiene un botón con clase **grey-btn** encargado del inicio de sesión.

	* `<div>` con clase **signup-wrapper**: contiene un botón con clase **grey-btn**, encargado de registrar al usuario en la web.

<br>

* `<section>` con clase **features-section**: se encarga de contener todas las características o resumen de la web en esta página de inidio.

  * `<div>` con clase **descritpion-section**: contiene texto, una imagen (emoji) y botones en su interior.

    * `<div>` con clase **text-content**: contiene dos divisiones:

	  * **top-header**: contiene el párrafo superior y la imagen de un emoji.

	  * **bottom-header**: contiene el párrafo inferior.

	* `<div>` con clase **buttons-wrapper**: contiene dos botones, el primero con clase **green-btn**, y el segundo con clase **black-btn**.

  * `<div>` con clase **projects-section**: contiene un `<div>` con un encabezado sobre una imagen, y la propia imagen como `<img>`.

    * `<div>` con clase **img-header**: contiene el texto situado en la parte superior de la imagen, el cuál también está formado por un link.

	* `<img>` que contiene la imagen mostrada.

<br>

* `<section>` con clase **codepen-for-wrapper**: contiene cuatro links, `<a>` con clase **codepen-for-item**.

<br>

* `<div>` con clase **page-end**, un elemento usado para añadir ese fondo gris al final de la página.

<br><hr><br>

[Volver a la página README principal.](../README.md)
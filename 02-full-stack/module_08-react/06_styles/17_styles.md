# Crear estilos en React

Existen muchas formas diferentes de crear estilos en React. En este módulo se va a seguir una de esas muchas.

Este *método* consiste en usar un archivo `.scss` llamado `main.scss` que no tendrá ningún estilo en sí mismo, pero que importará todos los demás archivos `.scss` que sí tendrán estilos.

Para ello, dentro de la carpeta `style`, que está situada dentro de `src`, se creará un archivo llamado `main.scss` con el siguiente contenido:

```scss
// main.scss
@use "./base";
```

<br/>

Ahora, vamos a crear el archivo `_base.scss` en el mismo directorio en el que se encuentra `main.scss`, y vamos a crear un estilo básico para el `body`.

```scss
// _base.scss

body {
    background-color: #f5f5f5;
}
```

<br/>

Si vemos que el estilo se aplica correctamente, significa que todo funciona bien.


<br/><hr/>
<hr/><br/>


## Modificar la fuente de texto

Para modificar la fuente de texto (`font-family`), vamos a acceder a la página [Google Fonts](https://fonts.google.com/), y vamos a seleccionar la fuente que queramos.

En este caso, vamos a seleccionar la fuente `Titillium Web` (se puede seleccionar cualquiera).

Una vez seleccionada la fuente, vamos a hacer click en el botón `+` que aparece en la parte inferior derecha de la pantalla. Esto añadirá la fuente a una lista de fuentes que vamos a usar.

Ahora, copiaremos el código HTML que se nos da, y lo pegaremos en el archivo `index.html` que se encuentra en la carpeta `static`.

Finalmente, vamos a copiar el código CSS que se nos da, y lo pegaremos en el archivo `_base.scss` que se encuentra en la carpeta `style`:

```scss
// _base.scss

body {
    font-family: 'Titillium Web', sans-serif;
}
```
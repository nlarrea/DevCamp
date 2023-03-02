# Forma de trabajo

Ahora que hemos creado todo lo necesario para poder realizar un proyecto, vamos a ver cuáles son las mejores pautas y prácticas a la hora de trabajar con proyectos en JavaScript.

<br>

En primer lugar, si quisiéramos utilizar librerías externas, tendríamos que importarlas al proyecto. En este apartado vamos a hablar sobre dividir el código en diferentes archivos y cómo importarlos en el proyecto.

Vamos a utilizar el archivo `boostrap.js` del que ya hemos hablado anteriormente. En este archivo, vamos a importar todos los archivos necesarios para trabajar en el proyecto.


<br><hr>
<hr><br>


## Exportar e importar una variable

1. Creamos el archivo `helper.js` en la carpeta `src`.

2. En ese archivo vamos a crear una variable constante `greeting` y le asignamos el valor `Hi there`.

3. Indicamos que queremos exportar esa variable con la palabra reservada `export`.

4. En el archivo `bootstrap.js` importamos la variable `greeting` con la palabra reservada `import` e indicando el nombre del archivo que queremos importar, añadiendo también el directorio y sin añadir el tipo de archivo: `./helper`.

El resultado sería el siguiente:

```js
// helper.js
export const greeting = "Hi there";

// bootstrap.js
import { greeting } from "./helper";
```


<br><hr>
<hr><br>


## Exportar e importar una función

En este caso, vamos a exportar una función. Se van a seguir los pasos mencionados anteriormente, pero en este caso, se creará una función en el archivo `helper.js` y se importará en el archivo `bootstrap.js`.

```js
// helper.js
export function multiply(numOne, numTwo) {
    return numOne * numTwo;
}

// bootstrap.js
import { multiply } from "./helper";
```
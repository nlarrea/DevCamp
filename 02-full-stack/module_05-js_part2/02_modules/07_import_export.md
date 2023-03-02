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


<br><hr>
<hr><br>


## Exportar e importar varios elementos a la vez

Para poder importar varios elementos a la vez, se utiliza el siguiente código:

```js
// bootstrap.js
import { multiply, greeting } from "./helper";

// acceder a los elementos importados:
console.log(greeting);          // Hi there
console.log(multiply(2, 3));    // 6
```


<br><hr>
<hr><br>


## Exportar e importar TODOS los elementos

En este caso, la sintaxis varía un poco, se haría de la siguiente manera:

```js
// bootstrap.js
import * as helper from "./helper";

// acceder a los elementos importados:
console.log(helper.greeting);           // Hi there
console.log(helper.multiply(2, 3));     // 6
```


<br><hr>
<hr><br>


## Exportar e importar por defecto

Vamos a crear un nuevo archivo llamado `navigation.js` en la carpeta `src`.

En este archivo vamos a escribir el siguiente código:

```js
// navigation.js
export default function() {
    return "<div>Logo</div>;
}

// bootstrap.js
import navigation from "./navigation";
console.log(navigation());      // <div>Logo</div>
```

<br>

Puede parecer que no tiene sentido exportar más elementos del archivo `navigation` puesto que los elementos tomarán el nombre del archivo. Sin embargo, en un archivo con elementos exportados por defecto, podemos seguir exportando otros elementos de la misma forma que la descrita en apartados anteriores.

De esta forma, tendríamos algo así:

```js
// navigation.js
export default function() {
    return "<div>Logo</div>;
}

export const greeting = "Hi there";

export function multiply(numOne, numTwo) {
    return numOne * numTwo;
}


// bootstrap.js
import navigation, { greeting, multiply } from "./navigation";
console.log(navigation());          // <div>Logo</div>
console.log(greeting);              // Hi there
console.log(multiply(3, 3));        // 9
```

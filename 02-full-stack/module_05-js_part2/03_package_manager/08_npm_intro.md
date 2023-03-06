# npm

<div id="indice"></div>

* [Introducción](#introducción)
* [package.json](#packagejson)
* [MomentJS](#momentjs)
  * [Instalación](#instalación)
  * [Funciones más populares](#funciones-más-populares)


<br><hr>
<hr><br>


## Introducción

<sub>[Volver al índice](#indice) | [package.json >>](#packagejson)</sub>

`npm` es el gestor de paquetes de Node.js. Es un programa que se instala en tu computadora y que te permite tanto instalar paquetes de Node.js, como otros paquetes de terceros.

Ya hemos hablado de él en la sección anterior, pero vamos a profundizar un poco más en él.

Para ver qué paquetes tenemos instalados ya, debemos ejecutar el siguiente comando:

```bash
npm list -g
```


<br><hr>
<hr><br>


## Package.json

<sub>[<< Introducción](#introducción) | [Volver al índice](#indice) | [MomentJS >>](#momentjs)</sub>

El archivo `package.json` es un archivo de texto que contiene información sobre el proyecto. Es un archivo que se crea automáticamente cuando ejecutamos el comando `npm init` y que nos permite configurar el proyecto.

Tiene una sección llamada `dependencies` que contiene la lista de paquetes que nuestro proyecto necesita para funcionar. Por otro lado, también tiene una sección llamada `devDependencies` que contiene la lista de paquetes que nuestro proyecto necesita para funcionar en el entorno de desarrollo (de forma local). Es decir, al momento de hacer el deploy de la aplicación, los paquetes que figuren en `devDependencies` no se instalarán, pero sí los que figuren en `dependencies`.


<br><hr>
<hr><br>


## MomentJS

Moment.js es una librería que nos permite trabajar con fechas y horas de una forma muy sencilla.

[Moment.js cheatsheet](https://devhints.io/moment)


<br><hr><br>


### Instalación

<sub>[<< Package.json](#packagejson) | [Volver al índice](#indice) | [Funciones populares >>](#funciones-más-populares)</sub>

Vamos a abrir la terminal y acceder al directorio de trabajo en el que queramos trabajar. Una vez ahí, vamos a ejecutar el siguiente comando:

```bash
js-generate
```

<br>

Se nos preguntará el tipo de proyecto (`es6-starter`), y el nombre que deseemos darle (`PackageProject`). Después entraremos dentro del directorio que se acaba de crear, el cual tendrá el mismo nombre que el que hemos puesto en el paso anterior.

<br>

Ahora, abriremos el archivo `package.json`. Veremos que el archivo no contiene el paquete `moment` en la sección `dependencies`. Esto es porque no lo hemos instalado aún.

Para ello, lo primero que haremos, desde el directorio `PackageProject` en la terminal, será ejecutar el siguiente comando:

```bash
npm install
```

<br>

Esto instalará todo lo que contenga el archivo `package.json` en las secciones `dependencies` y `devDependencies`.

Se instalará todo dentro del directorio `node_modules`. **Si alguna vez nos da algún error alguno de los paquetes**, ya sea por compatibilidad, o el problema que sea, se deberá eliminar la carpeta `node_modules` y volver a ejecutar el comando `npm install`.

Esto se debe a que se trata de una carpeta que se genera automáticamente, y que contiene todos los paquetes que se instalan. Si se elimina, se vuelve a generar, y se instalan todos los paquetes que se encuentran en el archivo `package.json`.

<br>

Veremos que seguimos sin obtener el paquete `moment.js` en la sección `dependencies` del archivo `package.json`.

Para ello, ejecutaremos el siguiente comando:

```bash
npm install --save moment
```

<br>

Lo que hará esa línea de código es, en lugar de instalar de forma local el paquete y listo, lo instalará en la sección `dependencies` del archivo `package.json`, lo que añadirá también el paquete en la carpeta `node_modules`.

> Si vamos al archivo `package.json` y miramos en la sección `dependencies`, y vamos a la carpeta `node_modules`, veremos que el paquete `moment` se encuentra ahí en ambos casos. [^1]


<br><hr><br>


### Funciones más populares

<sub>[<< Instalación](#instalación) | [Volver al índice](#indice)</sub>

Ahora que tenemos instalado el paquete `moment`, vamos a ver algunas de las funciones más populares que nos ofrece.

Para ello, en primer lugar, vamos a iniciar el servidor desde el directorio `PackageProject`:

```bash
npm start
```

<br>

Ahora, iremos al archivo `src/bootstrap.js` y añadiremos el siguiente código:

```javascript
import moment from 'moment';

console.log(moment.now());      // 1678110801606
```

<br>

Para utilizar el paquete `moment`, lo primero que tenemos que hacer es importarlo. Para ello, utilizamos la palabra reservada `import` y le indicamos el nombre del paquete que queremos importar, en este caso `moment`.

No debemos usar `./moment`, como habíamos visto en apartados anteriores, ya que no es un archivo que nosotros hayamos creado, sino que es un paquete que se encuentra en la carpeta `node_modules`.

<br>

Ese código imprime la cantidad de segundos desde el 1 de enero de 1970. Como vemos que funciona, significa que el paquete `moment` se ha instalado correctamente.

<br>

Vamos a comenzar a usar el paquete y ver sus funciones más populares:

```javascript
import moment from 'moment';

// date object
const rightNow = moment();
console.log(rightNow);


// custom date object
const birthday = moment('1998-06-29', 'YYYY-MM-DD');
console.log(birthday.format('dddd'));           // Monday
console.log(birthday.fromNow());                // 25 years ago
console.log(birthday.format('MMM Do YYYY'));    // Jun 29th 1998

const randomDate = moment('2023-02-26');
console.log(randomDate.fromNow());              // 9 days ago


// calculations
const twoWeeksFromNow = moment().add(14, 'days');
// const twoWeeksFromNow = moment().add(2, 'weeks'); -> sería lo mismo
console.log(twoWeeksFromNow.toString());    // Mon Mar 20 2023 15:12:52 GMT+0100

const sixMonthAgo = moment().subtract(6, 'months');
console.log(sixMonthAgo.toString());        // Tue Sep 06 2022 15:12:52 GMT+0100
```


<br><hr>

[^1]: Si no se encuentra el paquete en la carpeta `node_modules` al mirar desde Visual Studio Code, primero asegurarse de actualizar el árbol de archivos. Para ello, se debe hacer click en la opción `Refresh Explorer`, situada al lado de la opción de crear una nueva carpeta.
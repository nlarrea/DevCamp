# Crear un módulo npm

<div id="indice"></div>

* [Primeros pasos](#primeros-pasos)
* [Crear el módulo](#crear-el-módulo)
    * [Código - index.js](#código---indexjs)
    * [Documentación - README.md](#documentación---readmemd)
* [Publicar el módulo](#publicar-el-módulo)
* [Testear el módulo](#testear-el-módulo)


<br><hr>
<hr><br>


## Primeros pasos

<sub>[Volver al índice](#indice) | [Crear módulo >>](#crear-el-módulo)</sub>

Elementos necesarios para crear un módulo npm:

* **Herramientas:**
    * Editor de código ([Visual Studio Code](https://code.visualstudio.com/) por ejemplo)
    * [Node.js](https://nodejs.org/es/)
* **Cuentas en:**
    * [GitHub](https://github.com/)
    * [npm](https://www.npmjs.com/)

<br>

A continuación, iniciaremos el proceso de creación de un módulo npm. Para ello, comenzaremos **iniciando sesión en npm** desde la terminal:

```bash
npm set init-author-name "tu nombre"
npm set init-author-email "tu@email.com"
npm set init-author-url "http://www.tu-url.com"
```

<br>

Una vez hecho esto, iniciaremos la sesión en npm:

```bash
npm login
```

<br>

Se nos pedirá que introduzcamos el usuario, el password y el email. Una vez hecho esto, ya podemos comenzar a crear el módulo.


<br><hr>
<hr><br>


## Crear el módulo

<sub>[<< Primeros pasos](#primeros-pasos) | [Volver al índice](#indice) | [Código >>](#código---indexjs)</sub>

En primer lugar, accederemos a GitHub y crearemos un nuevo repositorio para el módulo. En este caso, creareos un repositorio llamado `copr-msg-footer`.

<br>

A continuación, desde la terminal, accederemos al directorio donde crearemos el módulo. En este caso, crearemos uno nuevo en el escritorio, y accederemos a él:

```bash
mkdir ~/Desktop/copr-msg-footer
cd ~/Desktop/copr-msg-footer
```

<br>

Una vez dentro del directorio, iniciaremos el proceso de creación del módulo. Para ello, ejecutaremos el siguiente comando:

```bash
npm init
```

<br>

Una vez ejecutado, se nos realizarán una serie de preguntas que deberemos responder:

```bash
package name: (copr-msg-footer)     # pulsar ENTER
version: (1.0.0) 0.1.0
description: This module allows for a dynamic footer to be generated for JS applications with an updated year and name.
entry point: (index.js) index.js    # pulsar ENTER
test command:                       # pulsar ENTER
git repository: https://github.com/nlarrea/copr-msg-footer
keywords: footer
license: (ISC) MIT
```

<br>

Una vez respondidas todas las preguntas, se nos creará el archivo `package.json` con la información que hemos introducido.


<br><hr><br>


### Código - index.js

<sub>[<< Crear módulo](#crear-el-módulo) | [Volver al índice](#indice) | [Documentación >>](#documentación---readmemd)</sub>

Vamos a crear un archivo llamado `index.js` en el directorio raíz del módulo. Este archivo será el archivo principal del módulo, y será el que se ejecutará cuando se importe el módulo en otro proyecto.

<br>

Dentro de este archivo, escribiremos el siguiente código:

```js
// que todo el código debe seguir la norma convencional de JS
'use strict';


// importamos de la forma antigua el módulo moment
var moment = require('moment');


// documentación -> indica qué hará la función
/**
 * Returns a string element with a footer and updating year.
 * @param {string} name
 * @return {string}
 */
exports.footer = function (name) {
    return "Copyright " + moment().format('YYYY') + " " + name + "All rights reserved.";
};
```

<br>

Como se puede observar, en el código se importa el módulo `moment` de la forma que se hacía en la versión anterior de JS.

Sin emargo, a pesar de indicar que se requiere dicho módulo, no ha sido instalado. Para ello, ejecutaremos el siguiente comando:

```bash
npm install --save moment
```

<br>

Esto creará la sección `dependencies` en el archivo `package.json`, y añadirá el módulo `moment` al mismo.

<br>

En las últimas líneas de código, usamos el objeto `exports` y le añadimos el atributo `footer` como una función. Esta función recibe un parámetro `name`, y devuelve un string, tal y como se indica en la documentación.

Cada vez que se use el módulo, al usar `moment`, se actualizará el año automáticamente, mostrando un string como el siguiente:

`Copyright 2023 All rights reserved.`


<br><hr><br>


### Documentación - README.md

<sub>[<< Código](#código---indexjs) | [Volver al índice](#indice) | [Publicar módulo >>](#publicar-el-módulo)</sub>

Ahora, lo que debemos hacer es crear un archivo README:

```bash
touch README.md
```

<br>

En este archivo README escribiremos la documentación del módulo. En este caso, escribiremos lo siguiente:

```md
# Devcamp JS Footer

> This should be used in the following manner:

Install with the command:

    ```bash
    npm install --save copr-msg-footer
    ```

Add to a JavaScript Project with the following code:

    ```javascript
    import { footer } from "copr-msg-footer";

    footer('Some name');
    ```
```


<br><hr>
<hr><br>


## Publicar el módulo

<sub>[<< Documentación](#documentación---readmemd) | [Volver al índice](#indice) | [Testear módulo >>](#testear-el-módulo)</sub>

Para poder publicar el paquete que acabamos de crear, ejecutaremos el siguiente comando:

```bash
npm publish
```

<br>

Es necesario que el paquete que queremos subir tenga un nombre único. Si no lo tiene, dará error, pero podremos modificar el nombre del paquete en el archivo `package.json` y volver a ejecutar el comando.

<br>

Una vez publicado, podremos verlo en la página de npm: [https://www.npmjs.com/package/copr-msg-footer](https://www.npmjs.com/package/copr-msg-footer)


<br><hr>
<hr><br>


## Testear el módulo

<sub>[<< Publicar módulo](#publicar-el-módulo) | [Volver al índice](#indice)</sub>

Vamos a crear un nuevo archivo en otro directorio para comprobar que el módulo funciona correctamente.

Para ello, crearemos un nuevo directorio en el escritorio, y realizaremos los siguientes pasos:

```bash
cd ..   # salir del directorio del módulo

# crear nuevo proyecto de react
js-generate
? What project template would you like to generate?
  es6-starter
? Project name: TestingFooterApp

# acceder al directorio
cd TestingFooterApp

# instalar dependencias
npm install
```

<br>

Ahora que tenemos el proyecto creado, vamos a instalar el módulo que acabamos de publicar. Para ello, podemos copiar el comando desde la página oficial creada, desde GitHub, o simplemente escribiendo el siguiente comando:

```bash
npm install --save copr-msg-footer
```

<br>

Veremos que ahora aparece en el archivo `package.json` la dependencia del módulo que acabamos de instalar.

<br>

Ahora, modificamos el código del archivo `src/bootstrap.js`, y añadimos el siguiente código:

```js
import { footer } from "copr-msg-footer";

console.log(footer('DevCamp'));
```

<br>

Iniciamos el servidor de desarrollo:

```bash
npm start
```

<br>

Y abriendo el navegador en la dirección `http://localhost:3000`, veremos el siguiente mensaje en la consola:

```
Copyright 2023 DevCamp All rights reserved.
```

<br>

Como se puede observar, **el módulo funciona correctamente**.
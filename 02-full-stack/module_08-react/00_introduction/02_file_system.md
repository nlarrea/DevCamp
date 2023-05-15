# React File System

En esta sección, vamos a repetir los pasos mostrados anteriormente para generar un proyecto de React haciendo uso de la herramienta `devcamp-js-builder`.

<br>

Para instalar esta herramienta, ejecutamos el siguiente comando en la terminal:

```bash
npm install devcamp-js-builder -g
```

<br>

A continuación, vamos a generar un proyecto de React. Para ello, ejecutamos el siguiente comando en la terminal:

```bash
js-generate
```

<br>

Este comando nos va a mostrar un menú con diferentes opciones. En este caso, vamos a seleccionar la opción `react-redux-router`. Después, vamos a darle un nombre al archivo. En mi caso, lo llamaré `nlarrea-react-portfolio`.

<br>

Una vez hecho esto, accedemos a dicho directorio recién creado desde la terminal, y ejecutamos lo siguiente:

```bash
# cd nlarrea-react-portfolio

npm install
```

<br>

> Si se genera algún problema debido a la instalación de `node-sass`, debemos seguir los siguientes pasos:
>
> 1. Eliminar la dependencia `node-sass` del archivo `package.json`.
> 2. Ejecutar el comando `npm install` para asegurarnos de que ya no hay errores.
> 3. Ejecutar el comando `npm i sass` para instalar la dependencia `sass`.

<br>

Una vez instaladas las dependencias, vamos a ejecutar el comando `npm start` para comprobar que todo funciona correctamente.


<br><hr>
<hr><br>


## node_modules

### Añadir dependencias

En esta sección, vamos a ver cómo está estructurado el proyecto de React que acabamos de generar.

<br>

En primer lugar, tras haber ejecutado el comando `npm install`, se nos habrá creado una carpeta llamada `node_modules`. Esta carpeta contiene todas las dependencias que hemos instalado en nuestro proyecto.

Si quisiéramos añadir nuevas dependencias, deberíamos añadirlas al archivo `package.json`, dentro del apartado `dependencies` y siguiendo el orden alfabético (*para usar buenas prácticas*), indicando el nombre de la dependencia y la versión que queremos instalar.

Después, con el sistema parado, ejecutaríamos el comando `npm install` para instalar dicha dependencia.

<br>

En nuestro caso, vamos a instalar la dependencia `moment` a modo de ejemplo. Para ello, vamos a escribir lo siguiente en el archivo `package.json`:

```json
"dependencies": {
    # otras dependencias
    "moment": "^2.29.1",
    # otras dependencias
}
```

<br>

A continuación, vamos a ejecutar el comando `npm install` para instalar dicha dependencia.

<br>

Para poder utilizarla, vamos al siguiente directorio:

```bash
src > components > app.js
```

<br>

Vamos a tener que importar la dependencia `moment` en este archivo. Para ello, escribimos lo siguiente:

```js
import moment from 'moment';
```

<br>

Ahora podremos utilizar la dependencia `moment` en este archivo. Por ejemplo, vamos a escribir lo siguiente:

```js
import React, { Component } from 'react';
import moment from 'moment';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                <h1>nlarrea</h1>
                <div>
                    {moment().format('MMMM Do YYYY, hh:mm:ss a')}
                </div>
            </div>
        );
    }
}
```


<br><hr><br>


### Eliminar dependencias

Para eliminar dependencias, lo único que se debe hacer es eliminarla de la lista de dependencias del archivo `package.json`, y después ejecutar el comando `npm install` para que se elimine de la carpeta `node_modules`.

<br>

El comando `npm install` se encarga de revisar la lista de dependencias. Si encuentra una dependencia en la lista y no está en la carpeta `node_modules`, la instala. Si encuentra una dependencia en la carpeta `node_modules` y no está en la lista, la elimina.

<br>

La carpeta `node_modules` debe verse como una carpeta temporal. Puede ser eliminada en cualquier momento, y si se va a subir la aplicación a un repositorio, no se debe subir esta carpeta.

Además, si se desea modificar algo de la carpeta `node_modules`, se debe hacer a través de la lista de dependencias del archivo `package.json`, y nunca de forma directa desde la propia carpeta.


<br><hr><br>


### Otra forma de añadir dependencias

Hemos visto como añadir y eliminar dependencias a través del archivo `package.json`. Sin embargo, existe otra forma de hacerlo.

<br>

Vamos a realizar la explicación a través de un ejemplo, volviendo a instalar la dependencia `moment`. Para ello, si accedemos a la página oficial de `moment`, veremos que nos indican que para instalar la dependencia, debemos ejecutar el siguiente comando:

```bash
npm i moment
```

<br>

Existen algunas ventajas de instalar las dependencias de esta forma, y es que se instalan directamente, se añaden tanto al archivo `package.json` como a la carpeta `node_modules`, y se añade la versión más reciente de la dependencia.

Se considera la forma estándar de instalar dependencias, y es la que más se suele utilizar.


<br><hr>
<hr><br>


## El directorio src

Las letras `src` hacen referencia a la palabra `source`. En este directorio encontraremos todos los elementos que correspondan a la lógica de nuestra aplicación.

Todos los demás archivos serán dependencias y archivos de configuración.


<br><hr><br>


### src > actions & src > reducers

Dentro de este directorio encontramos el archivo `index.js`. Este archivo nos permitirá interactuar con el store de Redux.

<br>

Redux nos permite almacenar toda la información en un único lugar.

<br>

Lo mismo ocurre con el directorio `reducers`. Ambos están creados específicamente para trabajar con Redux.

> Se explicará en secciones posteriores con mayor profundidad.


<br><hr><br>


### src > components

Este es un directorio clave para nuestras aplicaciones. Aquí es donde se almacenan todos los componentes de nuestra aplicación, y, por recordar, React se basa en componentes.

<br>

En este directorio encontraremos el archivo `app.js`, que es el componente principal de nuestra aplicación. Todos los demás componentes van a estar anidados dentro de este *App compoent*.

Este va a ser el *parent component* de todos los demás componentes que tengamos en nuestra aplicación.


<br><hr><br>


### src > style

Dentro de este directorio se encontrarán aquellos archivos que contengan los estilos de nuestra aplicación (archivos `.css` o `.scss`).


<br><hr><br>


### src > bootstrap.js

Este archivo es el encargado de arrancar nuestra aplicación. Es el primer archivo que se ejecuta cuando se inicia la aplicación.

En él se importan todos los componentes que se van a utilizar en la aplicación, así como el archivo `./style/main.scss`, de tal forma que los estilos queden cargados en la aplicación.

<br>

A continuación, se crea la función `main()`, por lo que aquí es donde comienza la aplicación de React.

Se especifica que se quiere usar el DOM de React, lo que significa que se va a utilizar el *browser* para renderizar la aplicación. Si fuera una aplicación móvil, se especificaría que se quiere usar React Native en lugar de DOM.

<br>

Por tanto, dentro de este archivo, se usan las siguientes líneas de código:

```js
// importar los componentes
import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import { BrowserRouter } from "react-router-dom";
import App from "./components/app";
import reducers from "./reducers";

// redux, se explica en secciones posteriores
const createStoreWithMiddleware = applyMiddleware()(createStore);

// importar los estilos
import "./style/main.scss";

// función main
function main() {
    ReactDOM.render(    // DOM de React
        // store de Redux
        <Provider store={createSoreWithMiddleware(reducers)}>
            <!-- para crear routes personalizados -->
            <BrowserRoute>
                <App />    <!-- componente principal -->
            </BrowserRoute>
        </Provider>,
        document.querySelector('.app-wrapper')
    );
}

document.addEventListener("DOMContentLoaded", main);
```

<br>

La línea de código `document.querySelector('.app-wrapper')` indica que quiere coger todas las líneas de código (*ReactDOM.render()*) y las va a renderizar en el elemento que tenga la clase `.app-wrapper`.

Pero, ¿dónde está ese elemento? Si nos fijamos en el archivo `static/index.html`, veremos que existe un elemento con la clase `.app-wrapper`:

```html
<body>
    <div class="app-wrapper"></div>
</body>
```

<br>

Esto es lo que hace que la aplicación tenga una única página. Ocurre porque se está renderizando la aplicación en el elemento `<div class="app-wrapper"></div>`. A medida que se necesite renderizar algo, se va a renderizar en ese elemento de forma dinámica, mostrándose únicamente lo que se necesite en cada momento.

<br>

Finalmente, la línea de código `document.addEventListener("DOMContentLoaded", main);` indica que cuando el DOM esté cargado, se ejecute la función `main()`.


<br><hr><br>


### src > vendor.js

Este archivo contiene únicamente un par de líneas de código.

Lo que hace es cargar `polyfill`, que es un archivo que se encarga de cargar todas las funcionalidades de ES6 que no son soportadas por los navegadores.

<br>

Lo que hace `babel-polyfill` es mirar el buscador y cargar en él todas las funcionalidades de ES6 que no soporta.


<br><hr>
<hr><br>


## El directorio static

Este directorio contiene todos los archivos estáticos de nuestra aplicación, como pueden ser imágenes, archivos de texto, etc.

<br>

En primer lugar, encontraremos un directorio llamado `assets`, que contiene un archivo `README.md` indicando qué tipo de archivos debemos guardar en él.

<br>

Después, encontraremos el *favicon* de nuestra aplicación, que es la imagen que aparece en la pestaña del navegador.

<br>

Finalmente, encontraremos el archivo `index.html`, que es el archivo principal de nuestra aplicación.


<br><hr>
<hr><br>


## El directorio webpack

Webpack es una tecnología que se usa para empaquetar y utilizar varias librerías dentro de nuestras aplicaciones de JavaScript. No está ligado a React concretamente, pero se utiliza mucho con él.

Se usa para crear ciertas reglas para las librerías que se van a utilizar en la aplicación.

<br>

Dentro de este directorio encontraremos los siguientes archivos:

* `common.config.js`: contiene la configuración común que debe seguir la aplicación en cualquier entorno.
* `dev.config.js`: contiene la configuración que debe seguir la aplicación en el entorno de desarrollo (o de manera local, en nuestra máquina).
* `prod.config.js`: contiene la configuración que debe seguir la aplicación en el entorno de producción (o en el servidor).
* `postcss.config.js`: contiene la configuración de PostCSS, que es una herramienta que se utiliza para transformar el código CSS con JavaScript.

<br>

Dentro de `common.config.js` encontraremos lo siguiente:
    
```js
// webpack plugins
const SplitChunksPlugin = require('webpack/lib/optimize/SplitChunksPlugin');

module.exports = {
    entry: {
        // que queremos que la aplicación comience aquí
        app: ['./src/bootstrap.js'],
        // para que use el polyfill
        vendor: './src/vendor.js',
    },

    resolve: {
        // lista de extensiones que se van a utilizar
        extensions: ['.js', '.scss'],
        // directorios donde se van a buscar los módulos
        modules: ['node_modules'],
    },

    module: {
        rules: [
            {
                /* que use babel en los archivos .js, en todos
                los que no estén dentro de node_modules */
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },

            {
                /* permite a la aplicación trabajar con archivos
                de multimedia */
                type: 'javascript/auto',
                test: /\.(jpg|png|gif|eot|svg|ttf|woff|woff2)$/,
                loader: 'file-loader',
                options: {
                    name: '[path][name].[ext]',
                    publicPath: '/',
                },
            },

            {
                test: /\.(mp4|webm)$/,
                loader: 'url?limit=10000',
            },
        ],
    },

    plugins: [
        /* en lugar de cargar toda la app, se divide en 'chunks'
        que se van cargando a medida que se necesitan */
        new SplitChunksPlugin({
            name: ['app', 'vendor'],
            minChunks: Infinity,
        }),
    ],
};
```
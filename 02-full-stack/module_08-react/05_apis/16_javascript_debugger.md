# JavaScript Debugger

<div id="index"></div>

* [Introducción al depurador de JS](#introducción-al-depurador-de-javascript)
* [Introducción al React Developers Tools](#introducción-al-react-developers-tools)
* [Extraer API Key Names con el depurador](#extraer-api-key-names-con-el-depurador)

<br/>

[<< KEY PROP](./15_key_prop.md#key-prop) | [HOME](../../../README.md#devcamp)


## Introducción al depurador de JavaScript

En este apartado vamos a ver cómo trabajar con el depurador de JavaScript. Este depurador nos permite ejecutar el código ***paso a paso***, puesto que se detiene cada vez que se encuentra con la palabra clave `debugger`.

En esta ocasión, vamos a introducir dicha palabra clave en el archivo `portfolio-container.js`, de la siguiente forma:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    // ...

    portfolioItems() {
        return this.state.data.map(item => {
            debugger;
            return <PortfolioItem key={item.id} title={item.name} url={item.url} slug={item.id} />;
        });
    }
    
    // ...
}
```

<br/>

Con este código, si ejecutamos la aplicación y abrimos la consola del navegador, podemos ver que se detiene la ejecución del código en el momento en el que se encuentra con la palabra clave `debugger`.

Ahora, si escribimos `item` en la consola, se nos mostrarán los datos del elemento actual de la lista. Dichos datos, serán aquellos que se introducieron en el servidor y a los que hemos llamado, es decir, los datos de la API.

Si clicamos en el botón de continuar, la ejecución del código continuará hasta que se encuentre con la siguiente palabra clave `debugger`. En este caso, solo hemos introducido esa palabra, por lo que si volvemos a escribir `item` en la consola, se nos mostrarán los datos del siguiente elemento de la lista.

Si escribimos `this.state.data` en la consola, se lanzará un error, puesto que el estado no puede ser modificado de esta manera. `debugger` solo nos permite ver los datos.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Introducción al React Developers Tools

En el apartado anterior hemos visto cómo utilizar `debugger` para ver los datos que se están utilizando en la aplicación. Sin embargo, esta no es una herramienta propia de React, sino que es una herramienta de JavaScript. Esto significa que puede ser utilizada en cualquier programa `.js`, independientemente de si se está utilizando React o no.

Para acceder a herramientas propias de React, se puede utilizar la extensión de React Developer Tools para Chrome. Accediendo [a esta página](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) se puede descargar la extensión.

Esta herramienta permite seleccionar y visualizar los componentes de React que se están utilizando en la aplicación. Además, también permite ver el estado de los componentes, así como los props que se están pasando a cada uno de ellos.



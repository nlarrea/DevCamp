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



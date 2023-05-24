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


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Extraer los nombres de los datos del API con el depurador

En este apartado vamos a ver cómo extraer los nombres de los datos recibidos a través del API. Para ello, vamos a utilizar el depurador de JavaScript.

Al igual que en el [primer apartado](#introducción-al-depurador-de-javascript), vamos a utilizar la palabra clave `debugger` para detener la ejecución del código en el momento en el que se genera cada `PortfolioItem`.

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

Ahora, en la consola y tras arrancar la app, escribiremos lo siguiente:

```js
Object.keys(item)
```

<br/>

Como ya mencionamos, `item` hace referencia a cada dato obtenido. Por ello, haciendo uso de `Object.keys()` podemos obtener las claves de cada uno de los datos, que en este caso son las mismas para todos:

1. `id`
2. `name`
3. `description`
4. `url`
5. `category`
6. `position`
7. `thumb_image_url`
8. `banner_image_url`
9. `logo_url`
10. `column_names_merged_with_images`

<br/>

Ahora, vamos a hacer una lista de lo que queremos enseñar en cada `PortfolioItem`, y vamos a relacionar cada elemento de la lista con las claves de los datos:

| Elemento a enseñar | Clave del dato |
| ------------------ | -------------- |
| Imagen de fondo    | `thumb_image_url` |
| Logo               | `logo_url` |
| Descripción        | `description` |
| ID                 | `id` |

<br/>

Ahora que sabemos cómo se llama cada dato de los elementos que queremos enseñar, vamos a poder mostrar dichos datos en cada `PortfolioItem`.


<br/><hr/><br/>


### Refactorizar el código de PortfolioItem

Ahora que sabemos qué datos queremos mostrar en cada `PortfolioItem`, vamos a refactorizar el código de dicho componente para que muestre dichos datos.

Comenzaremos modificando la forma en la que se envían los props al componente `PortfolioItem`:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    // ...

    portfolioItems() {
        return this.state.data.map(item => {
            return <PortfolioItem
                key={item.id}
                item={item}
            />;
        });
    }
    
    // ...
}
```

<br/>

Lo que queremos hacer con esto, es utilizar la opción de JavaScript de desestructurar objetos. De esta forma, mandamos todos los datos de cada ítem al componente `PortfolioItem`, y en dicho componente, tendremos acceso a cada uno de los datos.

Para ello, vamos a descomponer el objeto obteniendo únicamente los datos que queramos:

```js
// portfolio-item.js

// ...

export default function(props) {
    /** REMEMBER
     * Data that we'll need:
     * - bg image: thumb_image_url
     * - logo: logo_url
     * - description: description
     * - id: id
     */

    // destructuring the object
    const { id, description, thumb_image_url, logo } = props.item;

    return (
        <div>
            <div>{description}</div>
            <Link to={`/portfolio/${id}`}>Link</Link>
        </div>
    )
}
```

<br/>

Como se puede observar, hemos extraído los datos que queremos mostrar en cada `PortfolioItem` y los hemos almacenado en variables para facilitar su acceso.

Además, dado que ahora no obtenemos un prop llamado `slug`, sino que obtenemos directamente el `id`, debemos modificar dicha línea de código para que funcione correctamente.
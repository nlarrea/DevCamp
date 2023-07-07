# Scroll infinito

<div id='index'></div>

* [Crear la función para detectar el scroll](#crear-la-función-para-detectar-el-scroll)
* [Saber si se ha llegado al final de la página](#saber-si-se-ha-llegado-al-final-de-la-página)
* [Obtener el total de posts](#obtener-el-total-de-posts)
* [Spinner de carga](#spinner-de-carga)
* [Refactorizar el evento de scroll](#refactorizar-el-evento-de-scroll)

<br/>


[<< CREAR EL BLOG](./34_crear_el_blog.md#crear-el-blog) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


En esta sección vamos a ver cómo realizar un *scroll infinito*. Se conoce con este nombre al hecho de mostrar una cantidad determinada de elementos y, al llegar al final de la página, cargar y mostrar más elementos.

Esto se hace para evitar que la página se cargue con una cantidad excesiva de elementos, lo que podría ralentizar la carga de la misma.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Crear la función para detectar el scroll

En primer lugar, comenzaremos por crear la función encargada detectar el scroll:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...
        this.activateInfiniteScroll();
    }

    activateInfiniteScroll() {
        window.onscroll = () => {
            console.log('onscroll');
        }
    }

    // ...
}
```

<br/>

Si accedemos a la sección de blogs en la aplicación y hacemos scroll en ella, por consola veremos que se imprime el mensaje `onscroll` cada vez que se detecta un scroll.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Saber si se ha llegado al final de la página

Existen tres atributos clave para saber si se ha llegado al final de la página:

* `window.innerHeight`: Altura de la ventana actual del navegador.
* `document.documentElement.scrollTop`: Altura del scroll (*posición vertical*) actual.
* `document.documentElement.offsetHeight`: Altura total de la página.

<br/>

Para saber si se ha llegado al final de la página, debemos comprobar si la altura del scroll actual más la altura de la ventana actual es igual a la altura total de la página. Para ello, añadiremos el siguiente código a la función `activateInfiniteScroll()`:

```js
// blog.js

// ...

export default class Blog extends Component {
    // ...

    activateInfiniteScroll() {
        window.onscroll = () => {
            if (
                window.innerHeight + document.documentElement.scrollTop ===
                document.documentElement.offsetHeight
            ) {
                console.log('get more posts');
            }
        }
    }

    // ...
}
```

<br/>

Veremos que si hacemos scroll hasta el final de la página, se imprime el mensaje `get more posts` por consola.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Obtener el total de posts

Para saber si se deberán hacer más cargas y evitar mostrar todo el contenido de golpe, vamos a obtener el total de posts que hay en la API. Para ello, vamos a añadir nuevos atributos al estado y añadiremos el siguiente código a la función `getBlogItems()`:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...

        this.state = {
            // ...
            totalCount: 0,
            currentPage: 0
        };

        // ...
    }

    // ...

    getBlogItems() {
        this.setState({
            currentPage: ++this.state.currentPage
        });

        axios.get(/* ... */)
        .then(response => {
            debugger;
            // ...
        }).catch(error => {
            // ...
        });
    }

    // ...
}
```

<br/>

En primer lugar, añadimos al estado los atributos `totalCount` y `currentPage` para guardar el total de posts y la página actual en la que nos encontramos.

En el método `getBlogItems()` incrementamos en uno el valor de `currentPage` en uno, para que cada vez que se haga una petición a la API, se sume uno a la página actual.

Al acceder a la aplicación, como hemos usado `debugger`, abrimos la terminal y escribimos `response` en ella. Veremos los datos que se obtienen de la API, entre ellos, si accedemos a `data.meta` veremos que hay un atributo llamado `total_records` que nos indica el total de posts que hay en la API. Por lo que guardaremos dicho valor en el estado de la aplicación:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...

        this.state = {
            // ...
            totalCount: 0,
            currentPage: 0
        };

        // ...
    }

    // ...

    getBlogItems() {
        this.setState({
            currentPage: ++this.state.currentPage
        });

        axios.get(/* ... */)
        .then(response => {
            this.setState({
                // ...
                totalCount: response.data.meta.total_records
            });
        }).catch(error => {
            // ...
        });
    }

    // ...
}
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Spinner de carga

Para saber si se están cargando los posts, vamos a añadir un nuevo atributo al estado llamado `isLoading` y lo modificaremos en la función `getBlogItems()`:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...

        this.state = {
            // ...
            isLoading: true
        };

        // ...
    }

    // ...

    getBlogItems() {
        // ...

        axios.get(/* ... */)
        .then(response => {
            this.setState({
                // ...
                isLoading: false
            });
        }).catch(error => {
            // ...
        });
    }

    // ...
}
```

<br/>

Ahora, añadiremos un icono de FontAwesome con forma de spinner para hacer este efecto de carga.

Primero, importaremos el icono en el archivo `app.js`:

```js
// app.js

// ...
import {
    // ...,
    faSpinner
} from '@fortawesome/free-solid-svg-icons';
// ...

library.add(
    // ...,
    faSpinner
);

// ...
```

<br/>

Después, añadiremos el icono en el componente `Blog` y haremos uso de un operador ternario para mostrarlo únicamente cuando se estén cargando los posts:

```js
// blog.js

// ...
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

// ...

export default class Blog extends Component {
    // ...

    render() {
        // ...

        return (
            <div className='blog-container'>
                /* ... */

                {this.state.isLoading ? (
                    <div className='content-loader'>
                        <FontAwesomeIcon icon='spinner' spin />
                    </div>
                ) : (null)}
            </div>
        );
    }
}
```

<br/>

Finalmente, crearemos el archivo `_loaders.scss` y añadiremos el siguiente código al mismo:

> Recordar que para que el archivo sea leído por la aplicación, debemos importarlo en el archivo `main.scss`.

```scss
// _loaders.scss

@use './variables' as var;

.content-loader {
    font-size: 2em;
    color: var.$teal;
}
```

<br/>

Si accedemos a la aplicación, veremos que se muestra el icono de carga cuando se están cargando los posts.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Mostrar más posts

Para mostrar más posts, lo que haremos será modificar el método `activateInfiniteScroll()` para que, cuando se llegue al final de la página, se llame a la API para obtener más posts:

```js
// blog.js

// ...

export default class Blog extends Component {
    // ...

    activateInfiniteScroll() {
        window.onscroll = () => {
            if (
                window.innerHeight + document.documentElement.scrollTop ===
                document.documentElement.offsetHeight
            ) {
                this.getBlogItems();
            }
        }
    }
}
```

<br/>

Haciendo esto, veremos que cada vez que se llega al final se llama a la API para obtener más posts. Sin embargo, éstos eliminan los anteriores, aunque no se nota dado que estamos llamando a todos los datos desde el inicio.

Para llamar a los datos *por partes*, vamos a modificar el link de la API, indicando el parámetro de la página que se desea cargar:

```js
// blog.js

// ...

export default class Blog extends Component {
    // ...

    getBlogItems() {
        axios.get(
            `https://nlarrea.devcamp.space/portfolio/portfolio_blogs?page=${this.state.currentPage}`,
            // ...
        )
        // ...
    }

    // ...
}
```

<br/>

Si accedemos a la aplicación, veremos que esta vez se cargan los posts en cantidades correctas, sin embargo, los nuevos posts sobreescriben a los anteriores.

Para evitar esto, realizaremos la siguiente modificación:

```js
// blog.js

// ...

export default class Blog extends Component {
    // ...

    getBlogItems() {
        // ...

        axios.get(/* ... */)
        .then(response => {
            this.setState({
                blogItems: this.state.blogItems.concat(
                    response.data.portfolio_blogs
                ),
                // ...
            });
        }).catch(error => {
            // ...
        });
    }

    // ...
}
```

<br/>

Aparentemente, la funcionalidad completa del *scroll infinito* ya funciona, sin embargo, si accedemos a la consola del navegador, veremos que se siguen haciendo peticiones a la API aunque no haya más posts que mostrar.

Para solucionar esto, vamos a añadir una condición en la función `activateInfiniteScroll()`:

```js
// blog.js

// ...

export default class Blog extends Component {
    // ...

    activateInfiniteScroll() {
        window.onscroll = () => {
            /**
             * if the blogs are loading or all the blog items are
             * loaded, get out of this function
             */
            if (
                this.state.isLoading ||
                this.state.blogItems.length === this.state.totalCount
            ) {
                return;
            }

            // ...
        }
    }

    // ...
}
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Refactorizar el evento de scroll

Ahora mismo, nuestro código funciona correctamente, excepto por un pequeño bug:

* Si entramos en la página del blog, vamos a otra diferente (*por ejemplo, la página de inicio*) y hacemos scroll hasta abajo, se intentarán cargar más posts, lo que dará un error en la consola.

<br/>

Para solucionar esto y hacer que sólo se haga caso a ese evento cuando estemos en la página de los blogs, vamos a modificar el código de la siguiente forma:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...
        this.onScroll = this.onScroll.bind(this);
        window.addEventListener('scroll', this.onScroll, false);
    }

    onScroll() {
        if (
            this.state.isLoading ||
            this.state.blogItems.length === this.state.totalCount
        ) {
            return;
        }

        if (
            window.innerHeight + document.documentElement.scrollTop ===
            document.documentElement.offsetHeight
        ) {
            this.getBlogItems();
        }
    }

    // ...

    componentWillUnmount() {
        window.removeEventListener('scroll', this.onScroll, false);
    }

    // ...
}
```

<br/>

Lo que hemos hecho ha sido crear un nuevo método llamado `onScroll()` que se ejecutará cada vez que se haga scroll en la página. Dentro de él, hemos añadido el código que teníamos en la función `activateInfiniteScroll()` (*función que ha sido eliminada*) sin añadir el evento de scroll, que ahora está en el constructor de la clase.

Finalmente, para evitar que se sigan ejecutando eventos de scroll cuando no estamos en la página de los blogs, hemos añadido el método `componentWillUnmount()` para eliminar dicho evento.


<br/><hr/>
<hr/><br/>


[<< CREAR EL BLOG](./34_crear_el_blog.md#crear-el-blog) | [HOME](../../../README.md#devcamp)
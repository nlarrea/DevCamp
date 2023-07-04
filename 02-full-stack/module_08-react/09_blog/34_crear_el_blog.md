# Crear el Blog

<div id="index"></div>

* [Cambiar el componente funcional a uno basado en clase](#cambiar-el-componente-funcional-a-uno-basado-en-clase)
* [Crear y obtener datos de la API](#crear-y-obtener-datos-de-la-api)
    * [Mostrar los datos de los blogs](#mostrar-los-datos-de-los-blogs)
* [Crear el componente BlogDetail](#crear-el-componente-blogdetail)
* [Obtener los datos de cada blog](#obtener-los-datos-de-cada-blog)

<br/>


[<< EDITAR PORTFOLIO ITEMS](../08_portfolio_manager/33_editar_portfolio_items.md#editar-portfolioitems) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Cambiar el componente funcional a uno basado en clase

Al comienzo del proyecto ya fue creado el componente funcional `blog.js`. Lo que haremos a continuación, será convertirlo en un componente basado en clase. Para ello, accederemos a la ruta `src/components/pages/blog.js` y cambiaremos el código por el siguiente:

```js
// blog.js

import React, { Component } from 'react';
// ...

export default class Blog extends Component {
    construsctor() {
        super();
    }

    render() {
        return (
            /* ... */
        );
    }
}
```

<br/>

Mantendremos el código que teníamos dentro de `return()`, pero modificaremos el resto de líneas para conseguir modificar el componente de forma correcta.

Si arrancamos la aplicación, veremos que nada debería haberse visto modificado (*puesto que no hemos añadido ni modificado elementos dentro del componente*).


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Crear y obtener datos de la API

Para crear datos en la API, accederemos al link de [devcamp.space](https://www.devcamp.space/) y nos loguearemos con nuestro usuario. Una vez dentro, accederemos a la sección de `Portfolio`, después a `Blogs` y crearemos tantas entradas como queramos.

Ahora, añadiremos el código necesario para obtener la información de los blogs que acabamos de crear:

```js
// blog.js

// ...
import axios from 'axios';

export default class Blog extends Component {
    costructor() {
        // ...

        this.state = {
            blogItems: []
        };

        this.getBlogItems = this.getBlogItems.bind(this);
    }

    getBlogItems() {
        axios.get(
            'https://nlarrea.devcamp.space/portfolio/porftolio_blogs',
            { withCredentials: true}
        ).then(response => {
            console.log('response', response);
        }).catch(error => {
            console.log('getBlogItems error', error);
        });
    }

    componentDidMount() {
        this.getBlogItems();
    }

    // ...
}
```

<br/>

Si abrimos la consola del navegador podremos ver cómo hemos realizado la petición a la API correctamente y hemos recibido los datos de los blogs que hemos creado.

Ahora, vamos a modificar el estado de nuestro componente para que guarde los datos que acabamos de recibir:

```js
// blog.js

// ...

export default class Blog extends Component {
    // ...

    getBlogItems() {
        axios(/* ... */)
        .then(response => {
            this.setState({
                blogItems: response.data.portfolio_blogs
            });
        }).catch(error => {
            // ...
        });
    }

    // ...
}
```

<br/>

Para comprobar si se ha modificado o no el estado de la app, podemos hacer uso de la extensión de Chrome `React Developer Tools`. Si abrimos la pestaña de `Components` y buscamos nuestro componente, podremos ver que el estado ha sido modificado correctamente.


<br/><hr/><br/>


### Mostrar los datos de los blogs

Ahora que sabemos que recibimos los datos de los blogs creados, vamos a mostrarlos en la aplicación. En primer lugar, vamos a crear una nueva constante dentro de la función `render()` que contenga una lista de los blogs formateados para mostrar lo que queramos de ellos.

Comenzaremos mostrando el título y comprobando que el código es correcto:

```js
// blog.js

// ...

export default class Blog extends Component {
    // ...

    render() {
        const blogRecords = this.state.blogItems.map(blogItem => {
            return <h1>{blogItem.title}</h1>;
        });

        return (
            <div>
                {blogRecords}
            </div>
        );
    }
}
```

<br/>

Si abrimos la aplicación, veremos que se muestran los títulos de los blogs que hemos creado.

A continuación, dado que se va a alargar bastante el contenido de dicha constante, lo que haremos será reorganizar el código, creando así un nuevo componente llamado `blog-item.js`.

Así es como quedaría el código de `blog.js`:

```js
// blog.js

// ...

import BlogItem from '../blog/blog-item';

export default class Blog extends Component {
    // ...

    render() {
        const blogRecords = this.state.blogItems.map(blogItem => {
            return <BlogItem key={blogItem.id} blogItem={blogItem} />;
        });

        return (
            <div>
                {blogRecords}
            </div>
        );
    }
}
```

<br/>

Y en el nuevo componente, en primer lugar mostraremos únicamente el título y el contenido de cada blog:

```js
// blog-item.js

import React from 'react';

const BlogItem = props => {
    const {
        id,
        title,
        content,
        blog_status,
        featured_image_url
    } = props.blogItem;

    return (
        <div>
            <h1>{title}</h1>

            <div>{content}</div>
        </div>
    )
}
```

<br/>

Accediendo a la app, veremos que debería mostrarse el título y el contenido de cada blog.


<br/><hr/>
<hr/><br/>


<div>
    <a href='#index'>Volver arriba</a>
</div>


## Crear el componente BlogDetail

Vamos a crear un nuevo componente llamado `BlogDetail` para que podamos clicar en el título de cada `BlogItem` y nos muestre el contenido completo de dicho blog.

Para esto, primero deberemos crear la ruta a dicho componente en el archivo `app.js`:

```js
// app.js

// ...

// import Blog from ...;
import BlogDetail from './pages/blog-detail';
// ...

export default class App extends Component {
    // ...

    render() {
        return (
            <div className="container">
                <Router>
                    <div>
                        /* ... */

                        <Switch>
                            /* ... */
                            /* <Route path="/blog" ... /> */
                            <Route path="/b/:slug" component={BlogDetail}/>

                            /* ... */
                        </Switch>
                    </div>
                </Router>
            </div>
        );
    }
}
```

<br/>

Lo que hace el código anterior es crear una ruta que contenga la palabra `b` seguida de un `slug` que será el identificador de cada blog. El `slug` es un identificador único que se crea automáticamente para cada blog, donde aprovecharemos el ID que se genera en la API al crear cada uno de los blogs.

Una vez creada la ruta, vamos a crear el componente `BlogDetail`, de tal forma que simplemente muestre un texto para que podamos comprobar que funciona:

```js
// blog-detail.js

import React, { Component } from 'react';

export default class BlogDetail extends Component {
    render() {
        return (
            <div>
                <h1>Blog detail</h1>
            </div>
        );
    }
}
```

<br/>

Finalmente, volveremos al archivo `blog-item.js` y editaremos el código para añadir el enlace que nos permita acceder al detalle de cada blog:

```js
// blog-item.js

// ...
import { Link } from 'react-router-dom';

const BlogItem = props => {
    // ...

    return (
        <div>
            <Link to={`/b/${id}`}>
                <h1>{title}</h1>
            </Link>

            /* ... */
        </div>
    );
};

// ...
```

<br/>

En este código se puede ver perfectamente cómo la palabra `slug` utilizada al crear la ruta, se sustituye por el ID de cada blog.


<br/><hr/>
<hr/><br/>


<div>
    <a href='#index'>Volver arriba</a>
</div>


## Obtener los datos de cada blog

Ahora que ya tenemos la ruta creada y el componente `BlogDetail` creado, vamos a obtener los datos de cada blog para mostrarlos en el componente.

Para ello, vamos a crear el constructor de la clase `BlogDetail` para obtener el ID del blog actual usando los `props` pasados directamente gracias al uso de `react-router-dom`, y los datos de dicho blog.

Para ello, vamos a añadir las siguientes líneas de código:

```js
// blog-detail.js

// ...
import axios from 'axios';

export default class BlogDetail extends Component {
    constructor(props) {
        super(props);

        this.state = {
            currentId: this.props.match.params.slug,
            blogItem: {}
        };
    }

    getBlogItem() {
        axios.get(
            'https://nlarrea.devcamp.space/portfolio/portfolio_blogs/${this.state.currentId}'
        ).then(response => {
            console.log('response', response);
        }).catch(error => {
            console.log('getBlogItem error', error);
        });
    }

    componentDidMount() {
        this.getBlogItem();
    }

    // ...
}
```

<br/>

En primer lugar, hemos obtenido el ID del blog actual. Con él, hacemos uso de `axios` para obtener los datos del blog con ese ID.

Por ahora, solo hacemos un `console.log` para comprobar que se obtienen los datos correctamente. Si abrimos la consola del navegador, veremos que se muestran los datos del blog actual.

Viendo que los datos se han obtenido correctamente, para poder mostrarlos por pantalla, vamos a realizar las siguientes modificaciones:

```js
// blog-detail.js

// ...

export default class BlogDetail extends Component {
    // ...

    getBlogItem() {
        axios.get(/* ... */)
        .then(response => {
            this.setState({
                blogItem: response.data.portfolio_blog
            });
        }).catch(error => {
            // ...
        });
    }

    // ...

    render() {
        const {
            title,
            content,
            blog_status
            featured_image_url,
        } = this.state.blogItem;

        return (
            <div>
                <h1>{title}</h1>
                <img src={featured_image_url} alt='featured-image' />
                
                <div>
                    {content}
                </div>
            </div>
        );
    }
}
```

<br/>

Si accedemos a la aplicación, veremos que se muestran los datos del blog actual.
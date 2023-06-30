# Crear el Blog

<div id="index"></div>

* [Cambiar el componente funcional a uno basado en clase](#cambiar-el-componente-funcional-a-uno-basado-en-clase)
* [Crear y obtener datos de la API](#crear-y-obtener-datos-de-la-api)

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
# Crear el Portfolio-Manager

<div id="index"></div>

* [Crear el componente](#crear-el-componente)
    * [Crear la ruta](#crear-la-ruta)
* [Estilar el layout del componente](#estilar-el-layout-del-componente)
* [Portfolio Sidebar](#portfolio-sidebar)
    * [Añadir los datos de la API al estado de PortfolioManager](#añadir-los-datos-de-la-api-al-estado-de-portfoliomanager)
    * [Mostrar los datos en el Sidebar](#mostrar-los-datos-en-el-sidebar)
    * [Estilar el Sidebar](#estilar-el-sidebar)

<br/>

[<< LOGOUT HANDLER](../07_authentication/24_logout_handler.md#cerrar-la-sesión) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


## Crear el componente

En esta sección vamos a crear el componente que se encargará de gestionar el portfolio del usuario. Desde aquí, el usuario podrá crear, editar y eliminar sus *portfolio items*.

En primer lugar, comenzaremos creando un nuevo archivo en la carpeta `src/components/pages` llamado `portfolio-manager.js`. Una vez creado, escribimos el siguiente código:

```js
// portfolio-manager.js

import React, { Component } from 'react';

export default class PortfolioManager extends Component {
    render() {
        return (
            <div className="portfolio-manager-wrapper">
                <h1>PortfolioManager</h1>
                <h1>PortfolioManager</h1>
            </div>
        );
    }
}
```

<br/>

El código del componente por ahora sirve únicamente para comprobar que se renderiza correctamente.


<br/><hr/><br/>


### Crear la ruta

Ahora, vamos a crear una nueva ruta en nuestro archivo `app.js` que nos permita acceder a este componente. Por tanto, abrimos el archivo y escribimos el siguiente código:

```js
// app.js

// ...

// ...
import PortfolioManager from './pages/portfolio-manager';
// ...

export default class App extends Component {
    // ...

    authorizedPages() {
        return [
            <Route path="/portfolio-manager" component={PortfolioManager} />
        ]
    }

    render() {
        return (
            <div className="container">
                <Router>
                    <div>
                        /* ... */

                        <Switch>
                            /* ... */
                            <Route path="/blog" component={Blog}/>

                            {this.state.loggedInStatus === 'LOGGED_IN' ? this.authorizedPages() : null}

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

Como se puede observar, hemos eliminado el componente `Blog` de la función `authorizedPages()` y lo hemos añadido dentro del `Switch` con las demás rutas que son accesibles para todos los usuarios (*como recordatorio, esto se hizo para comprobar que funcionaba el ocultar links en base al usuario que accedía a la aplicación*).

A continuación, hemos añadido la ruta `/portfolio-manager` dentro de la función `authorizedPages()` para mostrar este componente únicamente a los usuarios que hayan iniciado sesión.

<br/>

Hasta ahora, la aplicación debería funcionar correctamente (ésto se puede comprobar accediendo a las diferentes rutas a través de la barra de navegación). Sin embargo, aún nos queda modificar el componente `NavigationComponent` del archivo `navigation-container.js` para que muestre los links correctamente:

```js
// navigation-container.js

// ...

const NavigationComponent = (props) => {
    // ...

    return (
        <div className="nav-wrapper">
            <div className="left-side">
                /* ... */
                
                <div className="nav-link-wrapper">
                    <NavLink to='/blog' activeClassName='nav-link-active'>Blog</NavLink>
                </div>

                {props.loggedInStatus === 'LOGGED_IN' ? dynamicLink('/portfolio-manager', 'Portfolio Manager') : null}
            </div>

            /* ... */
        </div>
    );
}
```

<br/>

Ahora deberían mostrarse los siguientes links para todos los usuarios:

* Home
* About
* Contact
* Blog

<br/>

Y el link `Portfolio Manager` únicamente para los usuarios que hayan iniciado sesión.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Estilar el layout del componente

Ahora que hemos creado el componente, vamos a generar ya el estilo del layout, el cual consistirá en dos columnas:

* El formulario para añadir un nuevo *portfolio item*.
* Una lista que contenga los *portfolio items*.

<br/>

Para ello, abrimos el archivo `portfolio-manager.js` y escribimos el siguiente código:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    render() {
        return (
            <div className='portfolio-manager-wrapper'>
                <div className='left-column'>
                    <h1>Portfolio form...</h1>
                </div>

                <div className='right-column'>
                    <h1>Portfolio sidebar...</h1>
                </div>
            </div>
        );
    }
}
```

<br/>

Una vez hecho esto, debemos estilar el layout. Para conseguirlo, crearemos un nuevo archivo dentro del directorio `src/style` llamado `_portfolio-manager.scss` (y lo añadiremos en el `main.scss`).

Dentro del nuevo archivo, escribiremos lo siguiente:

```scss
// _portfolio-manager.scss

@use './variables';

.portfolio-manager-wrapper {
    display: grid;
    grid-template-columns: 3fr 1fr;

    .left-column {
        background-color: variables.$offwhite;
    }
    
    .right-column {
        background-color: variables.$charcoal;
    }
}
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Portfolio Sidebar

### Añadir los datos de la API al estado de PortfolioManager

Vamos a comenzar llamando a la API para obtener y guardar los datos de los *portfolio items* en el estado del componente. Para ello, abrimos el archivo `portfolio-manager.js` y escribimos el siguiente código:

```js
// portfolio-manager.js

// ...
import axios from 'axios';

export default class PortfolioManager extends Component {
    constructor(props) {
        super(props);

        this.state = {
            portfolioItems: []
        };
    }

    getPortfolioItems() {
        axios.get('https://nlarrea.devcamp.space/portfolio/portfolio_items', { withCredentials: true })
        .then(response => {
            this.setState({
                portfolioItems: [...response.data.portfolio_items]
            });
        })
        .catch(error => {
            console.log('error in getPortfolioItems', error);
        });
    }

    componentDidMount() {
        this.getPortfolioItems();
    }

    // ...
}
```

<br/>

Comenzamos indicando en el estado un valor `[]` para la propiedad `portfolioItems` (que será un array que contendrá los *portfolio items*).

A continuación, llamamos a la API a través de la función `getPortfolioItems()` y guardamos los datos en el estado. Desde la API se obtiene un array de arrays, por lo que no es necesario usar el *spread operator*, ya que eso es lo que queremos guardar en el estado. Sin embargo, se ha añadido para que quede más claro que se está guardando un array de arrays.


<br/><hr/><br/>


### Mostrar los datos en el Sidebar

Ahora que tenemos los datos, vamos a crear un nuevo componente dentro del directorio `src/components/portfolio` llamado `portfolio-sidebar-list.js`. En este componente, el cual es una lista, se renderizaran los *portfolio items* obtenidos en el componente `PortfolioManager`.

Este es el código necesario en el componente `portfolio-sidebar-list.js`:

```js
// portfolio-sidebar-list.js

import React from 'react';

const PortfolioSidebarList = (props) => {
    const portfolioItem = props.data.map(portfolioItem => {
        return (
            <div>
                <div>
                    <img src={portfolioItem.thumb_image_url} />
                </div>
                <h1>{portfolioItem.name}</h1>
                <h2>{portfolioItem.id}</h2>
            </div>
        );
    });

    return (
        <div>
            {portfolioItem}
        </div>
    );
}

export default PortfolioSidebarList;
```

<br/>

Como se puede observar, el componente recibe los datos a través de las props y los renderiza en el return. Para ello, primero utilizamos la función `map()` para recorrer cada uno de los *portfolio items* y, a continuación, renderizamos los datos que queremos mostrar. Todo esto lo guardamos en una constante llamada `portfolioItem`.

Después, usamos el `return()` para renderizar la lista guardada en la constante `portfolioItem`.

<br/>

Como los datos se han pasado mediante `props`, debemos modificar el código del componente `portfolio-manajer.js` para que envíe dichos datos:

```js
// portfolio-manager.js

// ...

import PortfolioSidebarList from '../portfolio/portfolio-sidebar-list';

export default class PortfolioManager extends Component {
    // ...

    render() {
        return (
            <div className='portfolio-manager-wrapper'>
                /* ... */

                <div className='right-column'>
                    <PortfolioSidebarList data={this.state.portfolioItems} />
                </div>
            </div>
        );
    }
}
```


<br/><hr/><br/>


### Estilar el Sidebar

Una vez creado el sidebar, vamos a darle ciertos estilos para que las imágnes y los nombres se muestren como queremos.

En primer lugar, comenzaremos dando nobres a las clases de los elementos:

```js
// portfolio-sidebar-list.js

// ...

const PortfolioSidebarList = (props) => {
    const portfolioList = props.data.map(portfolioItem => {
        return (
            <div className='portfolio-item-thumb'>
                <div className='portfolio-thumb-img'>
                    <img src={portfolioItem.thumb_image_url} />
                </div>
                <h1 className='title'>{portfolioItem.name}</h1>
                <h2>{portfolioItem.id}</h2>
            </div>
        )
    });

    return (
        <div className='portfolio-sidebar-list-wrapper'>
            {portfolioList}
        </div>
    );
}

// ...
```

<br/>

Habiendo dado ya los nombres de clases deseados, creamos un nuevo archivo (`src/style/_portfolio-sidebar-list.scss`), lo añadimos en el `main.scss` y escribimos el siguiente código:

```scss
// _portfolio-sidebar-list.scss

@use './variables';

.portfolio-sidebar-list-wrapper {
    .portfolio-item-thumb {
        padding: 21px;

        .portfolio-thumb-img img {
            width: 100%;
        }

        .title {
            color: variables.$offwhite;
        }
    }
}
```
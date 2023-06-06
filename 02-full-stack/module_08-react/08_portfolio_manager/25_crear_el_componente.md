# Crear el Portfolio-Manager

<div id="index"></div>

* [Crear el componente](#crear-el-componente)
    * [Crear la ruta](#crear-la-ruta)

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
# Route Setup

En esta sección se va a hablar de cómo configurar las rutas en React.

En primer lugar, vamos a crear dos nuevos archivos dentro del directorio `components/pages`:

* `home.js`
* `about.js`

<br/>

Dentro de estos archivos vamos a insertar las siguientes líneas de código:

```jsx
// home.js

import React from 'react';

export default function() {
    return (
        <h1>Home</h1>
    )
}
```

```jsx
// about.js

import React from 'react';

export default function() {
    return (
        <h1>About</h1>
    )
}
```

<br/>

Una vez hecho esto, vamos a volver al archivo `app.js` y vamos a importar los componentes que acabamos de crear, así como aquellos que necesitamos para crear las rutas:

```jsx
// app.js

import React, { Component } from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom';

import Home from './pages/home';
import About from './pages/about';
```

<br/>

Ahora vamos a crear las rutas:

```jsx
// app.js

export default class App extends Component {
    render() {
        return(
            <div className='app'>
                <Router>
                    <div>
                        <NavigationContainer />

                        <Switch>
                            <Route exact path='/' component={Home} />
                            <Route path='/about-me' component={About} />
                        </Switch>
                    </div>
                </Router>

                <!-- ... -->
            </div>
        )
    }
}
```

<br/>

Aún, dichas rutas no están ligadas a ningún botón o link para poder navegar a ellas. Sin embargo, dentro de nuestro servidor, podemos navegar a ellas escribiendo la ruta en la barra de direcciones del navegador:

* Al encontrarnos ya dentro de la durección `localhost:3000`, veremos que nos aparece directamente el componente `Home`.
* Si escribimos `localhost:3000/about-me`, veremos que nos aparece el componente `About`.

<br/>

El *prop* `exact` que hemos añadido a la ruta `/` es necesario para que el componente `Home` se muestre únicamente cuando la ruta sea exactamente `/`. Si no lo añadiéramos, el componente `Home` se mostraría en todas las rutas que empiecen por `/` (`/about-me`, por ejemplo).

<br/>

Esto es posible gracias a que hemos importado el componente `Switch` de `react-router-dom`, el cual funciona como una especie de *if-else*.
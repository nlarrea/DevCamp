# Auth Component

<div id="index"></div>

* [Crear la ruta y el componente](#crear-la-ruta-y-el-componente)
* [Dar estilos al componente](#dar-estilos-al-componente)
    * [Importar una imagen estática](#importar-una-imagen-estática)
    * []

<br/>

[<< MIXINS](../06_styles/20_mixins.md#mixins) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


## Crear la ruta y el componente

Vamos a crear un sistema de autenticación para nuestro portfolio.

No vamos a añadir de forma visual a la página un link para ir a la ruta de *inicio de sesión*, ya que al tratarse de nuestro portfolio, seremos los únicos que podremos acceder a la zona de administración.

Aún así, sí que deberemos crear el componente y la ruta para poder acceder a él:

```jsx
// app.js

// ...

// ...
// import PortfolioDetail ...
import Auth from './pages/auth';
// import NoMatch ...

export default class App extends Component {
    render() {
        return (
            <div className="container">
                <Router>
                    <div>
                        <NavigationContainer />
                        
                        <Switch>
                            <Route exact path="/" component={Home}/>
                            <Route path="/auth" component={Auth}/>
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

Una vez creada la ruta, vamos a crear el componente:

```jsx
// auth.js

import React, { Component } from 'react';

export default class Auth extends Component {
    render() {
        return (
            <div>
                <h1>Auth...</h1>
            </div>
        )
    }
}
```

<br/>

Escribimos cualquier cosa en él y comprobamos que funciona correctamente.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Dar estilos al componente

### Importar una imagen estática

Vamos a comenzar importando una imagen que va a ser utilizada posteriormente.

Para ello, vamos a guardar la imagen `login.jpg` en la carpeta `static/assets/images/auth`.

Una vez hecho esto, vamos a importarla en el componente, y a crear la estructura básica que tendrá el mismo:

```jsx
// auth.js

// ...

import loginImg from '../../../static/assets/images/auth/login.jpg'

export default class Auth extends Component {
    render() {
        return (
            <div className='auth-page-wrapper'>
                <div className="left-column"
                    style={{
                        backgroundImage: `url(${loginImg})`
                    }}
                />

                <div className="right-column">
                    <h1>Login component goes here...</h1>
                </div>
            </div>
        );
    }
}
```


<br/><hr/><br/>


### Dispocisión de los elementos

Vamos a darle estilos a los elementos que hemos creado.

Queremos que la imagen importada ocupe la mitad izquierda de la pantalla, y que la mitad derecha esté formada por el formulario de inicio de sesión.

Vamos a crear el archivo `_auth.scss` y a importarlo en `main.scss`. Después, vamos a darle estilos a los elementos:

```scss
// _auth.scss

@use "./variables";

.auth-page-wrapper {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    height: calc(100vh - 84px); // 84px = navbar height

    .left-column {
        background-size: cover;
    }

    .right-column {
        display: flex;
        justify-content: center;
        align-items: center;

        background-color: variables.$offwhite;
    }
}
```


<br/><hr/>
<hr/><br/>



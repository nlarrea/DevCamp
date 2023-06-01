# Render props

<div id="index"></div>

* [Objetivo](#objetivo)
* [Modificar el componente padre](#modificar-el-componente-padre)
    * [Crear un estado](#crear-un-estado)
    * [Manejar el login](#manejar-el-login)
* [Modificar los componentes hijos](#modificar-los-componentes-hijos)
    * [Modificar Auth](#modificar-auth)
    * [Modificar Login](#modificar-login)
* [Comprobar el estado de autenticación](#comprobar-el-estado-de-autenticación)
* [Convertir un componente de clase en uno de función](#convertir-un-componente-de-clase-en-uno-de-función)

<br/>


[<< DEEP DIVE: AUTHENTICATION](./22_deepDive_authentication.md#deep-dive-authentication) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


## Objetivo

Ahora que sabemos que nuestro proceso de autenticación funciona correctamente, vamos a comenzar a crear el proceso que nos permitirá mostrar cierta parte del contenido de la aplicación cuando el usuario esté autenticado.

Por ejemplo, si el usuario ha iniciado sesión correctamente, el usuario debe poder acceder a ciertas rutas, como aquella que permita crear nuevos *portfolio items*. En caso de que no lo esté, no solo no debe ver los enlaces a dichas rutas, sino que si intenta acceder a ellas, debe ser redirigido a la página de `no-match`.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Modificar el componente padre

Para hacer esto, vamos a comenzar a modificar el código directamente en el componente padre: `app.js`, el componente que contiene toda la aplicación. Esto lo hacemos para poder manejar la lógica de autenticación en todas las páginas de la app.

No podemos eliminar código, pero lo que sí podemos hacer es crear y usar condicionales que se encarguen de ejecutar diferentes partes de código en función de si el usuario está autenticado o no.


<br/><hr/><br/>


### Crear un estado

Lo primero que haremos, será crear un estado en el componente padre, añadiendo el constructor, al que pasaremos unos `props`:

```js
// app.js

// ...

export default class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            loggedInStatus: 'NOT_LOGGED_IN'
        };
    }

    render() {/* ... */}
}
```

<br/>

Comenzamos con un estado que tiene una propiedad `loggedInStatus` que tiene un valor inicial de `NOT_LOGGED_IN`.

El motivo por el que no usamos valores booleanos, es porque ésto suele llevar a problemas a la hora de interpretar un condicional por diferentes personas. Por lo que vamos a usar dos cadenas de texto con un valor que sea fácil de entender, los cuales son valores muy usados por convención.


<br/><hr/><br/>


### Manejar el login

Una vez creado el estado, vamos a crear dos métodos capaces de manejar si el usuario ha iniciado sesión correctamente (`handleSuccessfulLogin`) o no (`handleUnsuccessfulLogin`):

```js
// app.js

// ...

export default class App extends Component {
    constructor(props) {
        // ...
    }

    handleSuccessfulLogin() {
        this.setState({
            loggedInStatus: 'LOGGED_IN'
        });
    }

    handleUnsuccessfulLogin() {
        this.setState({
            loggedInStatus: 'NOT_LOGGED_IN'
        });
    }

    render() {/* ... */}
}
```

<br/>

Cada vez que estos métodos sean llamados, su función será actualizar el estado de la aplicación, cambiando el valor de la propiedad `loggedInStatus`.

<br/>

**¿Cómo vamos a ser capaces de llamar a estos métodos?**

Para poder llamarlos, vamos a hacer uso de los `render props`.

Hasta ahora, hemos trabajado con `render`, que es un método obligatorio para aquellos componentes de tipo clase en React. Y por otro lado, hemos trabajado con `props`, que son los datos que se pasan de un componente padre a un componente hijo.

Un `render prop` es un `prop` que se pasa a un componente, pero permitiendo el acceso a comunicar con el proceso de `render`.

Vamos a ver ésto con la ruta encargada de llevarnos al componente `Auth`:

```js
// app.js

// ...

export default class App extends Component {
    constructor(props) {
        // ...

        this.handleSuccessfulLogin = this.handleSuccessfulLogin.bind(this);
        this.handleUnsuccessfulLogin = this.handleUnsuccessfulLogin.bind(this);
    }

    handleSuccessfulLogin() {/* ... */}

    handleUnsuccessfulLogin() {/* ... */}

    render() {
        return (
            <div className='app'>
                <Router>
                    <div>
                        /* ... */

                        <Switch>
                            /* ... */

                            <Route
                                path='/auth'
                                render={props => (
                                    <Auth
                                        {...props}
                                        handleSuccessfulLogin={this.handleSuccessfulLogin}
                                        handleUnsuccessfulLogin={this.handleUnsuccessfulLogin}
                                    />
                                )}
                            />

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

En la ruta que lleva al componente `Auth`, hemos añadido un `render prop` que recibe unos `props` y que devuelve el componente `Auth` con los `props` que recibe, además de los métodos `handleSuccessfulLogin` y `handleUnsuccessfulLogin`.

Esto lo hacemos para permitir al componente `Auth` tener acceso a estos métodos, y así poder llamarlos cuando sea necesario.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Modificar los componentes hijos

### Modificar Auth

Ya hemos pasado los métodos `handleSuccessfulLogin` y `handleUnsuccessfulLogin` al componente `Auth`, por lo que ahora vamos a modificar el código de este componente para que haga uso de ellos.

En primer lugar, deberemos crear el constructor de este componente y pasarle los `props` que recibe:

```js
// auth.js

// ...

export default class Auth extends Component {
    constructor(props) {
        super(props);
    }

    render() {/* ... */}
}
```

<br/>

Si recordamos del [apartado anterior](#modificar-el-componente-padre), el componente `Auth` recibe los métodos `handleSuccessfulLogin` y `handleUnsuccessfulLogin` como `props`, por lo que ahora podremos usarlos en este componente.

Vamos a comenzar creando dos nuevos métodos que hagan uso de estos `props`:

```js
// auth.js

// ...

export default class Auth extends Component {
    constructor(props) {
        super(props);

        this.handleSuccessfulAuth = this.handleSuccessfulAuth.bind(this);
        this.handleUnsuccessfulAuth = this.handleUnsuccessfulAuth.bind(this);
    }

    handleSuccessfulAuth() {
        this.props.handleSuccessfulLogin();

        // redirect user to home page
        this.props.history.push('/');
    }

    handleUnsuccessfulAuth() {
        this.props.handleUnsuccessfulLogin();
    }

    render() {/* ... */}
}
```

<br/>

En el método `handleSuccessfulAuth` llamamos al método `handleSuccessfulLogin` que hemos pasado como `prop` y que se encarga de actualizar el estado de la aplicación, y después redirigimos al usuario a la página de inicio.

En el método `handleUnsuccessfulAuth` llamamos al método `handleUnsuccessfulLogin` que hemos pasado como `prop` y que se encarga de actualizar el estado de la aplicación.

Finalmente, solo nos queda modificar los `props` que recibe el componente `Login`:

```js
// auth.js

export default class Auth extends Component {
    // ...

    render() {
        return (
            <div className='auth-page-wrapper'>
                /* ... */

                <div className='right-column'>
                    <Login
                        handleSuccessfulAuth={this.handleSuccessfulAuth}
                        handleUnsuccessfulAuth={this.handleUnsuccessfulAuth}
                    />
                </div>
            </div>
        );
    }
}
```


<br/><hr/><br/>


### Modificar Login

Habiendo modificado los datos enviados al componente `Login`, ahora debemos modificar el código de este componente para que haga uso de ellos.

Todo el código a modificar se encuentra en el método `handleSubmit`:

```js
// login.js

// ...

export default class Login extends Component {
    // ...
    
    handleSuibmit(event) {
        axios.post(/* ... */)
        .then(response => {
            if (response.data.status === 'created') {
                this.props.handleSuccessfulAuth();
            } else {
                // ...
                this.props.handleUnsuccessfulAuth();
            }
        }).catch(error => {
            // ...
            this.props.handleUnsuccessfulAuth();
        });

        // ...
    }
}
```


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Comprobar el estado de autenticación

Con lo que hemos hecho hasta ahora, el hecho de recargar la página, hace que el estado de autenticación se pierda, y se muestre que el usuario no está autenticado.

Queremos conseguir que se mantenga el último estado, por lo que vamos a modificar el código de tal forma que compruebe si el usuario está autenticado o no llamando a la API.

Para ello, vamos a crear un nuevo método llamado `checkLoginStatus()` que se encargará de hacer la llamada a la API:

```js
// app.js

// ...

export default class App extends Component {
    // ...

    checkLoginStatus() {
        axios.get('https://api.devcamp.space/logged_in', { withCredentials: true })
        .then(response => {
            const loggedIn = response.data.logged_in;
            const loggedInStatus = this.state.loggedInStatus;

            // if loggedIn and status LOGGED_IN => return data
            // if loggedIn status NOT_LOGGED_IN => update state
            // if not loggedIn and status LOGGED_IN => update state
            
            if (loggedIn && loggedInStatus === 'LOGGED_IN') {
                return loggedIn;
            } else if (loggedIn && loggedInStatus === 'NOT_LOGGED_IN') {
                this.setState({
                    loggedInStatus: 'LOGGED_IN'
                });
            } else if (!loggedIn && loggedInStatus === 'LOGGED_IN') {
                this.setState({
                    loggedInStatus: 'NOT_LOGGED_IN'
                });
            }
        }).catch(error => {
            console.log('Error: ', error);
        });
    }

    componentDidMount() {
        this.checkLoginStatus();
    }

    render() {/* ... */}
}
```

<br/>

En este método, hacemos una llamada a la API, y en función de la respuesta, actualizamos el estado de la aplicación.

Se comprueba el estado en el método `componentDidMount()` para que se ejecute cada vez que se recargue la página.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Convertir un componente de clase en uno de función

En el componente `NavigationComponent` no vamos a necesitar hacer uso del estado ni de métodos de ciclo de vida, por lo que vamos a convertirlo en un componente de función:

```js
// navigation-container.js

import React from "react";
import { NavLink } from "react-router-dom";

const NavigationComponent = (props) => {
    return (
        <div className="nav-wrapper">
            <div className="left-side">
                <div className="nav-link-wrapper">
                    <NavLink exact to='/' activeClassName='nav-link-active'>Home</NavLink>
                </div>

                <div className="nav-link-wrapper">
                    <NavLink to='/about-me' activeClassName='nav-link-active'>About</NavLink>
                </div>

                <div className="nav-link-wrapper">
                    <NavLink to='/contact' activeClassName='nav-link-active'>Contact</NavLink>
                </div>

                <div className="nav-link-wrapper">
                    <NavLink to='/blog' activeClassName='nav-link-active'>Blog</NavLink>
                </div>
            </div>

            <div className="right-side">
                NAIA LARREA
            </div>
        </div>
    );
}

export default NavigationComponent;
```


<br/><hr/>
<hr/><br/>


[<< DEEP DIVE: AUTHENTICATION](./22_deepDive_authentication.md#deep-dive-authentication) | [HOME](../../../README.md#devcamp)
# Render props

<div id="index"></div>

* [Objetivo](#objetivo)
* [Modificar el componente padre](#modificar-el-componente-padre)
    * [Crear un estado](#crear-un-estado)
    * [Manejar el login](#manejar-el-login)

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


[<< DEEP DIVE: AUTHENTICATION](./22_deepDive_authentication.md#deep-dive-authentication) | [HOME](../../../README.md#devcamp)
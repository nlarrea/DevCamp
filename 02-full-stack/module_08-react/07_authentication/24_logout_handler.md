# Cerrar la sesión

<div id='index'></div>

* [Logout handler](#logout-handler)
* [Higher order component](#higher-order-component)
    * [Error de funcionamiento](#error-de-funcionamiento)

<br/>

[<< RENDER PROPS](./23_render_props.md#render-props) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


Hasta ahora, hemos visto cómo conseguir que el usuario pudiera iniciar sesión si estaba autorizado a ello. Ahora, vamos a ver cómo permitir que el usuario cierre la sesión.


## Logout handler

En primer lugar, vamos a crear el *handler* que se encargará de cerrar la sesión. Para ello, comenzamos abriendo nuestro archivo `app.js` y escribiendo el siguiente código:

```js
// app.js

// ...

export default class App extends Component {
    constructor(props) {
        // ...

        this.handleSuccessfulLogout = this.handleSuccessfulLogout.bind(this);
    }

    // ...

    handleSuccessfulLogout() {
        this.setState({
            loggedInStatus: 'NOT_LOGGED_IN'
        });
    }

    // ...

    render() {
        return (
            <div className="container">
                <Router>
                    <div>
                        <NavigationContainer
                            loggedInStatus={this.state.loggedInStatus}
                            handleSuccessfulLogout={this.handleSuccessfulLogout}
                        />

                        /* ... */
                    </div>
                </Router>
            </div>
        );
    }
}
```

<br/>

Con esto, lo que hacemos es pasar como `prop` la función encargada de modificar el estado de la sesión a `NavigationContainer`.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Higher order component

Ahora, debemos modificar el archivo `navigation-container.js` para que, cuando el usuario haga clic en el botón de cerrar sesión (*que aún debemos añadir*), se ejecute la función que hemos pasado como `prop`. Para ello, abrimos el archivo y escribimos el siguiente código:

```js
// navigation-container.js

// ...
import axios from 'axios';
import { withRouter } from 'react-router';
// ...

const NavigationComponent = (props) => {
    // ...

    const handleSignOut = () => {
        axios.delete('https://api.devcamp.space/logout', { withCredentials: true })
        .then(response => {
            if (response.status === 200) {
                props.history.push('/');
                props.handleSuccessfulLogout();
            }

            return response.data;
        })
        .catch(error => {
            console.log('Error signing out', error);
        });
    }

    return (
        <div className="nav-wrapper">
            /* ... */

            <div className="right-side">
                NAIA LARREA

                {props.loggedInStatus === 'LOGGED_IN' ? (
                    <a onClick={handleSignOut}>Sign Out</a>
                ) : null}
            </div>
        </div>
    );
}

export default withRouter(NavigationComponent);
```

<br/>

Hemos añadido una condición utilizando el *operador ternario* dentro de la sentencia `return` para que se muestre un enlace de ***cerrar sesión*** cuando el usuario esté *logueado*.

Si se hace clic en dicho enlace, se ejecutará la función `handleSignOut`, donde se cerrará la sesión del usuario gracias a esta línea de código:

```js
axios.delete('https://api.devcamp.space/logout', { withCredentials: true })
```

<br/>

El usuario será redirigido a la página *Home*:

```js
props.history.push('/');
```

<br/>

Y se modificará el estado de la sesión:

```js
props.handleSuccessfulLogout();
```


<br/><hr/><br/>


### Error de funcionamiento

A priori, estas líneas de código no serán capaces de hacer al usuario volver atrás a la página de inicio, puesto que se mostrará un error diciendo que se está tratando de hacer `push` sobre un elemento `undefined`.

Lo que se está indicando es que `history` no está definido, lo que significa que no podemos acceder al historial del navegador. Sin embargo, hemos usado este cósido anteriormente (*en el archivo `auth.js`*) y no hemos tenido ningún problema.

<br/>

**¿Por qué ocurre esto?**

En el archivo `app.js` hemos utilizado el componente `Route` para renderizar el componente `Auth` y, por tanto, `history` está disponible. Sin embargo, a la hora de renderizar el archivo `navigation-container.js`, no hemos utilizado `Route`, por lo que `history` no está disponible.

Por ello, en este caso, para que funcione correctamente, se debe utilizar el *Higher Order Component* `withRouter` de la siguiente manera:

```js
export default withRouter(NavigationComponent);
```

<br/>

Lo que esto hace, es *encapsular* el componente `NavigationComponent` dentro de `withRouter`, lo que le permite acceder a `history`.


<br/><hr/>
<hr/><br/>


[<< RENDER PROPS](./23_render_props.md#render-props) | [HOME](../../../README.md#devcamp)
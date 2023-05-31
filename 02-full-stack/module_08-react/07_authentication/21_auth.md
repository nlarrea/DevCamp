# Auth Component

<div id="index"></div>

* [Crear la ruta y el componente](#crear-la-ruta-y-el-componente)
* [Dar estilos al componente](#dar-estilos-al-componente)
    * [Importar una imagen estática](#importar-una-imagen-estática)
    * [Disposición de los elementos](#dispocisión-de-los-elementos)
* [Formulario de inicio de sesión](#formulario-de-inicio-de-sesión)
    * [Cambiar el estado con los datos del formulario](#cambiar-el-estado-con-los-datos-del-formulario)
    * [Manejo de errores](#manejo-de-errores)

<br/>

[<< MIXINS](../06_styles/20_mixins.md#mixins) | [HOME](../../../README.md#devcamp) | [DEEP DIVE: AUTHENTICATION >>](./22_deepDive_authentication.md#deep-dive-authentication)


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


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Formulario de inicio de sesión

Por ahora, vamos a crear la estructura necesaria para el inicio de sesión, posteriormente, veremos cómo hacer que funcione.

Vamos a crear un nuevo archivo, dentro del directorio `src/components/auth`, llamado `login.js`. Dentro de este archivo, vamos a crear un componente de tipo clase, que va a tener un título y un formulario:

```jsx
// login.js

import React, { Component } from 'react';

export default class Login extends Component {
    render() {
        return (
            <div>
                <h1>LOGIN TO ACCESS YOUR DASHBOARD</h1>
                <form>
                    <input type="text" />
                    <input type="password" />
                </form>
            </div>
        );
    }
}
```

<br/>

Una vez creado el componente, vamos a importarlo en `auth.js` y a renderizarlo:

```jsx
// auth.js

// ...
import Login from '../auth/login';

export default class Auth extends Component {
    render() {
        return (
            <div className='auth-page-wrapper'>
                /* ... */

                <div className="right-column">
                    <Login />
                </div>
            </div>
        );
    }
}
```

<br/>

Si arrancamos la aplicación, veremos que se muestra todo correctamente, aunque aún no tiene los estilos que queremos.


<br/><hr/><br/>


### Cambiar el estado con los datos del formulario

En primer lugar, vamos a crear un constructor para el componente y vamos a definir el estado inicial del mismo:

```jsx
// login.js

// ...

export default class Login extends Component {
    constructor(props) {
        super(props);

        this.state = {
            email: '',
            password: ''
        };
    }

    // ...
}
```

<br/>

Vamos a añadir un botón de tipo `submit` al formulario, y vamos a actualizar los `input` para que tengan lo siguiente:

* `type`: necesario para definir el elemento. En este caso, `email` y `password`.
* `name`: le daremos el mismo nombre que la propiedad del estado que queremos actualizar (`email` y `password`).
* `value`: tendrán el valor de la propiedad del estado (`this.state.email` y `this.state.password`).
* `onChange`: le pasaremos una función que se ejecutará cada vez que el usuario escriba algo en el `input`. Esta función actualizará el estado del componente.

<br/>

```jsx
// login.js

// ...

export default class Login extends Component {
    // ...

    render() {
        return (
            <div>
                /* ... */
                
                <form onSubmit={this.handleSubmit}>
                    <input type="email"
                        name='email'
                        placeholder='Your email'
                        value={this.state.email}
                        onChange={this.handleChange}
                    />

                    <input type="password"
                        name='password'
                        placeholder='Your password'
                        value={this.state.password}
                        onChange={this.handleChange}
                    />

                    <div>
                        <button type='submit'>Login</button>
                    </div>
                </form>
            </div>
        );
    }
}
```

<br/>

Ahora, vamos a comenzar por crear la clase `handleChange`, que se encargará de actualizar el estado del componente cada vez que el usuario escriba algo en los `input`:

```jsx
// login.js

import React, { Component } from 'react';

export default class Login extends Component {
    constructor(props) {
        super(props);

        this.state = {
            email: '',
            password: ''
        };

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    render() {
        // ...
    }
}
```

<br/>

Este método será accedido cada vez que se actualice el valor tanto del `input` de tipo `email` como del de tipo `password`. Necesitamos una forma de comprobar cuál de los dos `input` se está actualizando, para poder actualizar el estado correctamente.

Para eso, se realiza la comprobación de forma dinámica mediante el nombre del `input` (`event.target.name`), que es el mismo que el nombre de la propiedad del estado que queremos actualizar.

Lo metemos entre `[]` para que se evalúe como una expresión, y no como una cadena de texto.

> Es decir, si el usuario está escribiendo en el `input` de tipo `email`, `event.target.name` será igual a `email`, y actualizará el estado de la siguiente forma:
>
> ```jsx
> this.setState({ email: event.target.value })
> ```


<br/><hr/><br/>


### Enviar los datos del formulario

Ahora, vamos a crear el método `handleSubmit`, que será accedido cada vez que el usuario pulse el botón de tipo `submit` del formulario.

En primer lugar, si el usuario pulsa el botón, por defecto la página se va a actualizar, y va a mostrar los datos del formulario en la URL.

Desde luego, esto no es lo que queremos que ocurra, así que lo primero que vamos a hacer dentro de esta nueva función, es prevenir el comportamiento por defecto del botón:

```jsx
// login.js

import React, { Component } from 'react';

export default class Login extends Component {
    constructor(props) {
        // ...
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    // ...

    handleSubmit(event) {
        event.preventDefault();
    }

    render() {
        return (
            <div>
                /* ... */
                
                <form onSubmit={this.handleSubmit}>
                    /* ... */

                    <div>
                        <button type='submit'>Login</button>
                    </div>
                </form>
            </div>
        );
    }
}
```

<br/>

Hecho esto, debemos conectar con la API para poder *loguearnos* con nuestras credenciales de la misma. Para ello, vamos a importar `axios` en el componente, y vamos a añadir las siguientes líneas al método `handleSubmit`:

```jsx
// login.js

handleSubmit(event) {
    axios.post('https://api.devcamp.space/sessions',
        {
            client: {
                email: this.state.email,
                password: this.state.password
            }
        },
        { withCredentials: true }
    ).then(response => {
        console.log('response', response);
    })
    
    event.preventDefault();
}
```

<br/>

Con esto, lo único que hemos hecho es enviar una petición `POST` a la API, con los datos del formulario. Se necesitan 3 parámetros:

* La URL a la que se va a enviar la petición.
* Los datos que se van a enviar. En este caso, un objeto con las credenciales del usuario.
* Un objeto con la configuración de la petición. Esto es necesario para que la API pueda identificar al usuario que se está logueando.

<br/>

Si abrimos una ***ventana de incógnito*** (porque aún no hemos implementado una forma de cerrar sesión), e introducimos los datos de la cuenta que tenemos en [DevCamp Space](https://www.devcamp.space/), veremos que se muestra un objeto en la consola del navegador, con los datos del usuario que se ha logueado.

Esto significa que todo funciona correctamente hasta ahora.


<br/><hr/><br/>


### Manejo de errores

**¿Qué ocurre si se produce algún error?**

Cuando se produce algún tipo de error, la API devuelve un error, y la petición no se completa.

<br/>

**¿Qué ocurre si se introducen datos incorrectos?**

Cuando se introducen datos correctos, la API devuelve un objeto con los datos del usuario, e información sobre el estado de la petición. Si hacemos el `console.log()` de la respuesta, veremos que tiene una propiedad `data` que contiene un objeto donde pone `status: 'created'`.

Si el usuario introduce datos incorrectos, el objeto de la respuesta tendrá una propiedad `data` que contiene un objeto donde pone `status: 401`, lo que significa que no se tiene acceso a la API.

<br/>

En ambos casos, hay que hacer saber al usuario qué es lo que está ocurriendo. Para ello, vamos a realizar lo siguiente:

* Vamos a añadir una propiedad `errorText` al estado del componente, que contendrá el mensaje de error que se mostrará al usuario.
* Para poder mostrar este error, vamos a añadir un `<div>` sobre los `input` del formulario, que se mostrará cuando haya un error, y que contendrá el mensaje del mismo.
* Vamos a modificar el método `handleSubmit`, para que actualice el estado del componente con el mensaje de error, en caso de que se produzca algún error con la API.
* Vamos a comprobar si el usuario ha introducido datos correctos, si no lo hace, se actualizará el estado del componente con el mensaje de error de inicio de sesión debido a credenciales erróneas.

<br/>

He aquí el código:

```jsx
// login.js

// ...

export default class Login extends Component {
    constructor(props) {
        // ...

        this.state = {
            email: '',
            password: '',
            errorText: ''
        };

        // ...
    }

    handleSubmit(event) {
        axios.post(
            'https://api.devcamp.space/sessionsasd',
            {
                client: {
                    email: this.state.email,
                    password: this.state.password
                }
            },
            { withCredentials: true }
        )
        .then(response => {
            // comprobar si el usuario ha introducido datos correctos
            if (response.data.status === 'created') {
                console.log('You can come in...');
            } else {
                // datos incorrectos -> actualizar mensaje de error
                this.setState({
                    errorText: 'Wrong email or password.'
                })
            }
        }).catch(error => {
            this.setState({
                // error con la API -> actualizar mensaje de error
                errorText: 'An error ocurred.'
            })
        });
        event.preventDefault();
    }

    render() {
        return (
            <div>
                /* ... */

                <div>{this.state.errorText}</div>
                
                <form onSubmit={this.handleSubmit}>
                    /* ... */
                </form>
            </div>
        );
    }
}
```

<br/>

Haciendo esto, veremos que se muestran dos mensajes diferentes:

* Si el usuario introduce datos incorrectos, se mostrará el mensaje `Wrong email or password.`
* Si se produce algún error con la API, se mostrará el mensaje `An error ocurred.`

<br/>

De esta forma, el usuario puede saber si el problema es que ha introducido datos incorrectos, o si se ha producido algún error con la API.

Sin embargo, al introducir un dato incorrecto y corregirlo, vemos que se sigue mostrando dicho mensaje. Esto se debe a que no hemos modificado su valor para que vuelva al estado inicial (vacío, o sin errores).

Para ello, introduciremos la siguiente línea en el método `handleChange`, para que se elimine el mensaje de error en el momento en el que el usuario comience a reescribir las credenciales:

```jsx
// login.js

handleChange(event) {
    this.setState({
        // ...
        errorText: ''   // actualizar mensaje de error
    });
}
```
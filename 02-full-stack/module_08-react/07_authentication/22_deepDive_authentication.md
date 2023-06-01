# Deep Dive: Authentication


[<< AUTH](./21_auth.md#auth-component) | [HOME](../../../README.md#devcamp) | [RENDER PROPS >>](./23_render_props.md#render-props)


<br/><hr/>
<hr/><br/>


Antes de continuar con las explicaciones, vamos a realizar una pausa para profundizar en el tema de la autenticación. En esta lección vamos a ver cómo funciona el proceso de autenticación en esta aplicación, teniendo en cuenta cómo lo hemos implementado en el código.

Vamos a utilizar una herramienta como ***Postman***, o ***Thunder Client*** para realizar las peticiones a nuestra API.


<br/><hr/>
<hr/><br/>


## Realizar una petición de inicio de sesión

Suponiendo que ya hemos sido registrados y recordando las siguientes líneas de código:

```js
handleSubmit(event) {
    axios.post(
        'https://api.devcamp.space/sessions',
        {
            client: {
                email: this.state.email,
                password: this.state.password
            }
        },
        { withCredentials: true }
    )
    .then(response => {
        if (response.data.status === 'created') {
            console.log('You can come in...');
        } else {
            this.setState({
                errorText: 'Wrong email or password.'
            })
        }
    }).catch(error => {
        this.setState({
            errorText: 'An error ocurred.'
        })
    });
    event.preventDefault();
}
```

<br/>

Hemos visto al arrancar el server que al hacer una petición de inicio de sesión, se nos muestra un mensaje `You can come in...` cuando las credenciales son correctas, y un mensaje `Wrong email or password.` cuando las credenciales son incorrectas.

**Pero, ¿cómo funciona esto?**

Vamos a realizar la petición desde ***Postman***, para ver qué ocurre:

1. Indicamos el enlace de la API: `https://api.devcamp.space/sessions`
2. Indicamos el método de la petición: `POST`
3. Escribimos en el `Body` los datos de la petición a realizar (indtroduciendo datos reales de un usuario registrado en la aplicación):
    ```json
    {
        "client": {
            "email": "email_real@gmail.com",
            "password": "password_real"
        }
    }
    ```

<br/>

Si los datos son correctos, como respuesta recibiremos lo siguiente:

```json
{
    "status": "created"
}
```

<br/>

Además, si nos fijamos en la parte de `Cookies`, veremos que hay una `cookie` llamada `_devcamp_space_session` con un valor en concreto.

Esta `cookie` es la que nos permite acceder a la aplicación, y es la que se crea cuando se realiza una petición de inicio de sesión. Esta `cookie` se almacena de forma automática en el navegador.

Cuando indicamos en el código `withCredentials: true`, lo que estamos haciendo es indicar que se envíe la `cookie` en la petición.


<br/><hr/>
<hr/><br/>


[<< AUTH](./21_auth.md#auth-component) | [HOME](../../../README.md#devcamp) | [RENDER PROPS >>](./23_render_props.md#render-props)
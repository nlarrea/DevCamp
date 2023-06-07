# Crear PortfolioItems desde PortfolioForm

<div id='index'></div>

* [Enviar los datos a la API](#enviar-los-datos-a-la-api)

<br/>


[<< KEY PROP WARNINGS](./26_eliminar_key_prop_warnings.md#eliminar-key-prop-warnings) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


## Enviar los datos a la API

En el componente `PortfolioForm` tenemos un formulario que nos permite crear nuevos items para el portfolio. Habíamos dejado pendiente el envío de los datos a la API desde el método `handleSubmit()`.

Vamos a modificar el código para poder crear dichos items.

```js
// portfolio-form.js

// ...
import axios from 'axios';

export default class PortfolioForm extends Component {
    // ...

    handleSubmit(event) {
        /** axios.post() -> 3 arguments
         * 1. url
         * 2. data
         * 3. withCredentials
         */

        axios.post(
            'https://nlarrea.devcamp.space/portfolio/portfolio_items',
            this.buildForm(),
            { withCredentials: true }
        ).then(response => {
            console.log('response', response);
        }).catch(error => {
            console.log('portfolio form handleSubmit error', error);
        })

        event.preventDefault();
    }

    // ...
}
```

<br/>

Si rellenamos el formulario con datos y clicamos en el botón de enviar, veremos que en la consola del navegador se nos muestra un objeto con la respuesta de la API, donde se indican:

* `data`: los datos que hemos enviado
* `status`: el código de estado de la respuesta (`201`)
* `statusText`: el mensaje de estado de la respuesta (`Created`)

<br/>

Tras esto, aún no se visualiza el ítem en el Sidebar, ya que no hemos actualizado el estado del componente `PortfolioManager`. Sin embargo, sí se mostrará si recargamos la página.

Al acceder al `Home`, también debe mostrarse el espacio en blando (*porque aún no hay imágenes*) y el mensaje de la descripción del ítem tras hacer *hover* sobre el mismo.
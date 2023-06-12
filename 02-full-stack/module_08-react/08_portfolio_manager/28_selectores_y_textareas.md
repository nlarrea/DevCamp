# Selectores y Textareas

<div id="index"></div>

* [Objetivo](#objetivo)
* [Selectores](#selectores)
* [Textareas](#textareas)

<br/>


[CREAR ITEMS DESDE EL FORM >>](./27_crear_items_desde_form.md#crear-portfolioitems-desde-portfolioform) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


## Objetivo

En el componente `PortfolioForm` tenemos un formulario que nos permite crear nuevos items para el portfolio. Ya hemos comprobado que los ítems se crean correctamente, sin embargo, tenemos dos elementos en el formulario que debemos modificar:

* `Category`: es un campo de texto, pero vamos a modificarlo para que sea un selector (`select`) con las categorías disponibles.
* `Description`: es un campo de texto, pero vamos a modificarlo para que sea un `textarea`.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Selectores

Para crear un selector, debemos utilizar la etiqueta `<select>` y dentro de ella, una serie de etiquetas `<option>` con los valores que queremos que se muestren en el selector.

Para ello, vamos a acceder al archivo `portfolio-form.js` y vamos a modificar el código de la siguiente manera:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    render() {
        return (
            <div>
                /* ... */

                <form onSubmit={this.handleSubmit}>
                    /* ... */
                    
                    <div>
                        /* ... */
                        
                        <select
                            name='category'
                            value={this.state.category}
                            onChange={this.handleChange}
                        >
                            <option value="eCommerce">eCommerce</option>
                            <option value="Scheduling">Scheduling</option>
                            <option value="Enterprise">Enterprise</option>
                        </select>
                    </div>

                    /* ... */
                </form>
            </div>
        );
    }
}
```

<br/>

Mantenemos los atributos `name`, `value` y `onChange` que ya teníamos en el campo de texto, y añadimos las etiquetas `<option>` con los valores que queremos que se muestren en el selector.


<br/><hr/><br/>


### Arreglar un error

Aunque seleccionando los componentes del selector, parezca que todo funciona correctamente, en realidad existe un pequeño error en el código.

Y es que, si entramos a la página de *crear* un nuevo Portfolio Item, y no seleccionamos ninguna categoría (*porque queremos usar la que está ya seleccionada por defecto*), y pulsamos el botón de *Create*, el item se crea correctamente, pero el valor de la categoría es `null`.

Esto se debe a que al renderizar la página, el estado inicial del `PortfolioForm` es `''` para todos los campos, incluido el de `category`. Lo que significa que, aunque parezca que hay una categoría seleccionada, en realidad no lo está, porque hasta que no ocurra el evento `onChange`, no se modifica el valor del estado.

Para solucionar esto, la idea más simple es modificar el valor inicial del estado por el valor del primer `option` del selector:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    constructor(props) {
        super(props);

        this.state = {
            // ...
            category: 'eCommerce',
            // ...
        };
    }
}
```

<br/>

Si probamos a crear un nuevo Portfolio Item, veremos que ahora sí que se crea correctamente, con la categoría seleccionada por defecto.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Textareas

Los cambios a realizar en nuestro código para modificar el input de tipo texto a un *textarea* son realmente mínimos. Simplemente debemos cambiar la etiqueta `<input>` por la etiqueta `<textarea>`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    render() {
        return (
            <div>
                /* ... */

                <form onSubmit={this.handleSubmit}>
                    /* ... */

                    <div>
                        <textarea
                            type="text"
                            name='description'
                            placeholder='Description'
                            value={this.state.description}
                            onChange={this.handleChange}
                        />
                    </div>

                    /* ... */
                </form>
            </div>
        );
    }
}
```
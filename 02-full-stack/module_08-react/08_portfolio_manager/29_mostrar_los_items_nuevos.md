# Mostrar los PortfolioItems nuevos

<div id="index"></div>

* [PorftolioForm](#porftolioform)
* [PorftolioManager](#porftoliomanager)
* [Modificar el orden de los PortfolioItems](#modificar-el-orden-de-los-items)

<br/>


[<< SELECTORES Y TEXTAREAS](./28_selectores_y_textareas.md#selectores-y-textareas) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


En el componente `PortfolioForm` tenemos un formulario que nos permite crear nuevos items para el portfolio. Ya hemos comprobado que los ítems se crean correctamente, sin embargo, éstos no se muestran en la lista de items del portfolio a no ser que recarguemos la página.

Para solucionar esto, vamos a realizar un par de modificaciones en los componentes `PortfolioForm` y `PortfolioManager`.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href='#index'>Volver arriba</a>
</div>


## PorftolioForm

**RECORDATORIO**

En este componente habíamos creado un formulario para crear nuevos PortfolioItems y añadirlos a la base de datos de la API desde la aplicación.

Hasta ahora, teníamos un método llamado `handleSubmit()` que se encargaba de enviar los datos del formulario a la API. Sin embargo, este método no hacía nada con la respuesta de la API (*teníamos un simple `console.log()` para comprobar que se creaba el componente correctamente*), por lo que vamos a modificarlo para que, cuando la respuesta sea correcta, se añada el nuevo item a la lista de items del portfolio.

Por tanto, lo único que debemos hacer es modificar el `console.log()` por el código capaz de enviar los datos al componente padre, que en este caso es `PortfolioManager`. Desde este componente padre, habíamos mandado como `prop` una función llamada `handleSuccessfulFormSubmission()` que se encargaría de añadir el nuevo item a la lista de items del portfolio. Por ello:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    handleSubmit(event) {
        /** axios.post() -> 3 arguments
         * url
         * data
         * withCredentials
         */
        axios.post(/* ... */)
        .then(response => {
            this.props.handleSuccessfulFormSubmission(response.data.portfolio_item);
        }).catch(error => {
            // ...
        })

        // ...
    }

    // ...
}
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## PorftolioManager

Como ya hemos mencionado, en este componente teníamos un método llamado `handleSuccessfulFormSubmission()` que se encargaba de añadir el nuevo item a la lista de items del portfolio. Sin embargo, este método no hacía nada con el nuevo item, por lo que vamos a modificarlo para que, cuando la respuesta sea correcta, se añada el nuevo item a la lista de items del portfolio.

Esta función recibe un parámetro (`porfolioItem`), el cual ha sido enviado desde el componente hijo `PortfolioForm` y contiene los datos del nuevo item.

Por ello, lo único que debemos hacer es añadir el nuevo ítem a la lista de items del portfolio, es decir, al estado del componente:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    // ...

    handleSuccessfulFormSubmission(porfolioItem) {
        this.setState({
            portfolioItems: [porfolioItem].concat(this.state.portfolioItems)
        })
    }

    // ...
}
```

<br/>

**Con este código lo que hacemos es lo siguiente:**

En primer lugar, indicamos que vamos a modificar el estado del componente, por lo que usamos `this.setState()`.

El elemento a modificar en el estado es una lista de items del portfolio, por lo que podemos pensar en hacer algo como:

```js
this.setState({
    portfolioItems: this.state.portfolioItems.push(portfolioItem)
})
```

<br/>

Sin embargo, esto no hace nada, debido a cómo funciona React.

Para que funcione, debemos hacer lo siguiente:

* Añadir el ítem a una lista usando `[]`:

    ```js
    [portfolioItem]
    ```

* Usar el método `concat()` para indicar qué elementos queremos concatenar:

    ```js
    [portfolioItem].concat(this.state.portfolioItems)
    ```

* Modificar el estado con este código.

<br/>

El resultado de modificar el estado sería el siguiente:

```js
this.setState({
    portfolioItems: [porfolioItem].concat(this.state.portfolioItems)
})
```

<br/>

Si ahora añadimos un elemento nuevo en el formulario y clicamos en el botón de enviar, veremos que el nuevo elemento se añade a la lista de items del portfolio sin necesidad de recargar la página.

Al principio, el nuevo elemento aparecerá en la primera posición, sin embargo, tras recargar la página, aparecerá al final. Esto se debe a cómo funciona la API, ya que los elementos se ordenan por fecha de creación, y al recargar la página, la fecha de creación del nuevo elemento será la más reciente, por lo que se posicionará al final de la lista.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Modificar el orden de los items

Podemos modificar el orden en el que se renderizan los componentes cuando son llamados e importados desde la API.

Para ello, modificaremos el modo en el que obtenemos los datos. Si recordamos, los datos son importados desde la API usando `axios.get()` en el método `getPortfolioItems()` del componente `PortfolioManager`. El link utilizado para llamar a los datos es el siguiente:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    // ...

    getPortfolioItems() {
        axios.get(
            'https://nlarrea.devcamp.space/portfolio/portfolio_items',
            // ...
        )
        // ...
    }

    // ...
}
```

<br/>

Podemos modificar el link para hacer que los datos se ordenen de forma ascendente o descendente, basándonos en la fecha de creación de los elementos:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    // ...

    getPortfolioItems() {
        axios.get(
            'https://nlarrea.devcamp.space/portfolio/portfolio_items?order_by=created_at&direction=desc',
            // ...
        )
        // ...
    }

    // ...
}
```

<br/>

Ahora, veremos que los ítems mostrados en el lateral de la página están ordenados desde el más reciente al más antiguo.
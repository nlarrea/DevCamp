# Eliminar PortfolioItems

<div id='index'></div>

* [Crear el link para eliminar los PortfolioItems](#crear-el-link-para-eliminar-los-portfolioitems)
* [Eliminar de la API](#eliminar-de-la-api)
    * [Funcionalidad](#funcionalidad)
    * [Actualizar el estado](#actualizar-el-estado)

<br/>


[<< ESTILAR LOS FORMULARIOS](./30_estilar_los_formularios.md#dar-estilo-a-los-formularios) | [HOME](../../../README.md#devcamp) | [FONTAWESOME >>](./32_fontawesome.md#fontawesome)


<br/><hr/>
<hr/><br/>


Hemos creado un formulario para crear los `PortfolioItems`. Ahora, vamos añadir la opción de eliminar los que ya existen.


<br/><hr/>
<hr/><br/>


## Crear el link para eliminar los PortfolioItems

En el `sidebar` donde se muestran los `PortfolioItems`, vamos a añadir un link para eliminar cada uno de ellos. Por ahora, el link mostrará el texto `Delete`, el cual se modificará más adelante por un icono.

Vamos a acceder primero al archivo `portfolio-sidebar-list.js` y vamos a añadir dicho link para cada uno de los componentes:

```js
// portfolio-sidebar-list.js

// ...

const PortfolioSidebarList = (props) => {
    const portfolioList = props.data.map(portfolioItem => {
        return (
            <div /* ... */>
                /* ... */

                <a onClick={() => props.handleDeleteClick(portfolioItem)}>
                    Delete
                </a>
            </div>
        );
    });
}

// ...
```

<br/>

Con este código, añadimos el link `Delete` para cada uno de los `PortfolioItems` que se muestran en el `sidebar`, y indicamos que cada vez que se clique en dicho link, se ejecute la función `handleDeleteClick()` que hemos pasado como `props` desde el componente `portfolio-manager.js` (*aún no la hemos creado*), que recibe un `PortfolioItem` como argumento.

Ahora, vamos al archivo `portfolio-manager.js` y vamos a crear la función `handleDeleteClick()`:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    constructor(props) {
        // ...
        this.handleDeleteClick = this.handleDeleteClick.bind(this);
    }

    handleDeleteClick(portfolioItem) {
        console.log("handleDeleteClick", portfolioItem);
    }

    // ...

    render() {
        return (
            <div className='portfolio-manager-wrapper'>
                /* ... */

                <div className="right-column">
                    <PortfolioSidebarList
                        handleDeleteClick={this.handleDeleteClick}
                        /* ... */
                    />
                </div>
            </div>
        );
    }
}
```

<br/>

Hemos creado el método de tal forma que su único trabajo ahora sea mostrar a qué `PortfolioItem` se le ha hecho click. Para ello, mostramos por consola el `portfolioItem` que se ha pasado como argumento.

Además, hemos pasado como `prop` la función `handleDeleteClick()` al componente `PortfolioSidebarList`.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Eliminar de la API

### Funcionalidad

Vamos a terminar de crear el código necesario para llamar a la API y eliminar el componente de su base de datos.

Tenemos ya el *handler* creado, por lo que solo debemos añadir las siguientes líneas en el mismo:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    // ...

    handleDeleteClick(portfolioItem) {
        axios.delete(
            `https://api.devcamp.space/portfolio/portfolio_items/${portfolioItem.id}`,
            { withCredentials: true }
        ).then(response => {
            console.log('response from delete', response);
        }).catch(error => {
            console.log('handleDeleteClick', error);
        });
    }
}
```

<br/>

Con este código, haciendo uso de `axios`, enviamos el *link dinámico* de la API, debido a que tenemos que indicar en dicho link el ID del elemento que queremos eliminar.

Si clicamos en alguno de los botones `Delete`, veremos que se ejecuta el `console.log()` y que muestra que el `response` ha sido satisfactorio. Esto significa que hemos eliminado el `PortfolioItem` de la API.

En el `sidebar` no se aprecia, pero si se recarga la página, veremos que el `PortfolioItem` ha sido eliminado.


<br/><hr/>
<hr/><br/>


### Actualizar el estado

Ahora que sabemos que el link funciona correctamente, vamos a actualizar el estado para no tener que recargar la página para ver los cambios:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    // ...

    handleDeleteClick(portfolioItem) {
        axios.delete(/* ... */)
        .then(response => {
            this.setState({
                portfolioItems: this.state.portfolioItems.filter(item => item.id !== portfolioItem.id)
            });

            return response.data;
        }).catch(error => {
            // ...
        });
    }
}
```

<br/>

Con esto, indicamos que los `portfolioItems` del estado sean todos los que no tengan el ID del `portfolioItem` que hemos pasado como argumento, es decir, el que se acaba de eliminar. Esto se consigue haciendo uso del método `filter()`.

De esta forma, el `portfolioItem` que hemos eliminado no se mostrará en el `sidebar`.


<br/><hr/>
<hr/><br/>


[<< ESTILAR LOS FORMULARIOS](./30_estilar_los_formularios.md#dar-estilo-a-los-formularios) | [HOME](../../../README.md#devcamp) | [FONTAWESOME >>](./32_fontawesome.md#fontawesome)
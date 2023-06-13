# Eliminar PortfolioItems

<div id='index'></div>

* [Crear el link para eliminar](#crear-el-link-para-eliminar)

<br/>


[<< ESTILAR LOS FORMULARIOS](./30_estilar_los_formularios.md#dar-estilo-a-los-formularios)


<br/><hr/>
<hr/><br/>


Hemos creado un formulario para crear los `PortfolioItems`. Ahora, vamos añadir la opción de eliminar los que ya existen.


<br/><hr/>
<hr/><br/>


## Crear el link para eliminar

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
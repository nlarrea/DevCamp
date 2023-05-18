# Render data

## Modificar el estado de la aplicación con datos de la API

Tal y como indica el título, habiendo comprobado que los datos se muestran por consola, ahora vamos a modificar el estado de la aplicación con los datos de la API.

<br/>

Seguiremos trabajando con el componente `PortfolioContainer`, lo primero que haremos, será eliminar del estado inicial los datos que han sido *hardcodeados* anteriormente:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
  constructor() {
    super();
    this.state = {
      data: [],
      loading: true,
      error: null,
    };
  }

  // ...
}
```

<br/>

Esto lo hacemos porque queremos que los datos vengan desde el servidor a traves de la API, y no que estén *hardcodeados* en el estado inicial.

<br/>

Una vez hecho esto, vamos a utilizar un método del ciclo de vida de los componentes de React, llamado `componentDidMount()`, que se ejecuta justo después de que el componente se haya montado en el DOM.

Eliminaremos del `constructor()` el `bind()` que habíamos hecho al método `getPortfolioItems()`, y eliminaremos del método `render()` la llamada a dicha función para añadirla en el método `componentDidMount()`.

Además, dentro del método `getPortfolioItems()`, vamos a modificar el valor de la propiedad `data` del estado de la aplicación, para que sea igual a los datos que nos devuelve la API:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    constructor() {
        // ...

        this.state = {
            pageTitle: 'Welcome to my portfolio',
            data: [], // eliminamos los datos hardcodeados
            isLoading: false
        };

        // eliminamos el bind() del método getPortfolioItems()

        // ...
    }

    // ...

    getPortfolioItems() {
        axios
            .get('https://nlarrea.devcamp.space/portfolio/portfolio_items')
            .then(response => {
                // modificación de la propiedad 'data' del estado de la aplicación
                this.setState({
                    data: response.data.portfolio_items
                });
            })
            .catch(error => {
                console.error(error);
            });
    }

    // llamada a la función para obtener los datos de la API
    componentDidMount() {
        this.getPortfolioItems();
    }

    render() {
        // ...
    }
}
```

<br/>

Habiendo hecho esto, podemos comprobar que aún no tenemos los resultados deseados. Esto es debido a que, aunque hemos modificado el estado de la aplicación con los datos de la API, aún no hemos hecho las modificaciones necesarias en el componente `PortfolioItem`, o en la llamada del mismo.

La API nos devuelve un array de objetos, pero éstos no tienen los mismos `keys` que los que teníamos *hardcodeados* en el estado inicial de la aplicación. Por ello, ésto es lo que debemos modificar:

```js
// portfolio-container.js

// ...

export default class PortfolioContaienr extends Component {
    // ...

    portfolioItems() {
        return this.state.data.map(item => {
            return (
                <PortfolioItem title={item.name} url={item.url} slug={item.id}/>
            )
        });
    }
}
```

<br/>

Habiendo hecho esto, ya podemos comprobar que los datos se muestran correctamente en la aplicación.
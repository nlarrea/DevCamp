# Condicionales

En este apartado vamos a ver cómo usar condicionales en JSX.

Para ello, vamos a añadir un nuevo atributo en el estado de nuestro archivo `portfolio-container.js`:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    constructor() {
        super();

        this.state = {
            pageTitle: 'Welcome to my portfolio',
            data: [
                {title: 'Primer dato', category: 'eCommerce'},
                {title: 'Segundo dato', category: 'Scheduling'},
                {title: 'Tercer dato', category: 'Enterprise'},
                {title: 'Cuarto dato', category: 'eCommerce'}
            ],
            isLoading: false
        };
    }
}

// ...
```

<br/>

Ahora, vamos a añadir una condición:

```jsx
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    // ...

    render() {
        if (this.state.isLoading) {
            return <div>Loading...</div>
        }

        return(
            // ...
        )
    }
}
```

<br/>

Si el valor de `isLoading` es `true`, entonces se mostrará el texto `Loading...`, en caso contrario, se mostrará el contenido del componente.

<br/>

Esto es muy útil cuando se pretenden mostrar datos obtenidos de un API. En caso de no tener aún dichos datos, podemos mostrar un mensaje de carga, y cuando se obtengan, mostrar los datos.
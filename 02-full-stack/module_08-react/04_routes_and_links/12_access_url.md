# Acceder a los valores de una URL

En este apartado vamos a crear un nuevo archivo al que acceder para entrar en más detalle dentro de nuestros proyectos, lo llamaremos `portfolio-detail.js`. Aquí se accedería para poder visualizar una habilidad, un proyecto o una empresa en concreto, por ejemplo.

Cada vez que clicáramos en un item del porfolio, nos llevaría a una URL que perteneciera a dicho ítem en concreto.

<br/>

Para hacer esto, vamos a tener que crear nuevas rutas en el archivo `app.js`:

```js
// app.js

// ...

import PortfolioDetail from './portfolio/portfolio-detail';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                <!-- ... -->

                <Router>
                    <div>
                        <NavigationContainer />

                        <Switch>
                            <!-- ... -->

                            <Route path='/portfolio/:slug' component={PortfolioDetail} />
                        </Switch>
                    </div>
                </Router>
            </div>
        );
    }
}
```

<br/>

La palabra `slug` se usa como convenio para aquellas URLs que tienen partes customizadas, que podrían ser parámetros.

En este caso, el `slug` sería el nombre del proyecto, la habilidad o la empresa.

<br/>

A continuación, añadimos el componente creado en la ruta `portfolio/portfolio-detail.js`:

<br/>

Ahora, vamos a crear dicho componente:

```js
// portfolio-detail.js

import React from 'react';

export default function(props) {
    return (
        <div>
            <h2>Portfolio Detail for {props.match.params.slug}</h2>

        </div>
    );
}
```

<br/>

Dentro del `<h2>` estamos indicando el título de la página, que será `Portfolio Detail for` y el `slug` que se haya pasado por parámetro.

Es decir, si accedemos a la URL `http://localhost:3000/portfolio/React`, el título de la página será `Portfolio Detail for React`.

<br/>

Ahora, lo que necesitamos es que al hacer click en un item del portfolio, nos lleve a la URL que corresponda. Para ello, vamos a modificar el componente `portfolio-container.js`:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    constructor() {
        super();

        this.state = {
            pageTitle: 'Welcome to my portfolio',
            data: [
                {title: 'Primer dato', category: 'eCommerce', slug: 'primero'},
                {title: 'Segundo dato', category: 'Scheduling', slug: 'segundo'},
                {title: 'Tercer dato', category: 'Enterprise', slug: 'tercero'},
                {title: 'Cuarto dato', category: 'eCommerce', slug: 'cuarto'}
            ],
            isLoading: false
        };

        // ...
    }

    portfolioItems() {
        return this.state.data.map(item => {
            return <PortfolioItem title={item.title} url={'google.com'} slug={item.slug} />;
        });
    }

    // ...

    render() {
        // ...
    }
}
```

<br/>

Con esto, hemos añadido el atributo `slug` a cada uno de los datos que tenemos dentro de `data` en `state`. También, hemos usado ese atributo para pasarlo como parámetro a cada uno de los items del portfolio a través del componente PortfolioItem (`portfolio-item.js`):

```js
// portfolio-item.js

// ...

export default function(props) {
    return (
        <div>
            <!-- ... -->

            <Link to={`/portfolio/${props.slug}`}>Link</Link>
        </div>
    )
}
```

<br/>

Finalmente, hemos añadido un link que nos llevará a la URL que corresponda a cada item del portfolio.
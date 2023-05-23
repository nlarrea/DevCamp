# Trabajar con URLs

<div id="index"></div>

* [Acceder a los valores de una URL](#acceder-a-los-valores-de-una-url)
* [Sin coincidencias de URL](#sin-coincidencias-de-url)
* [URLs anidadas en Portfolio](#urls-anidadas-en-portfolio)

<br/>


[<< LINKS](./11_links.md#links) | [HOME](../../../README.md#devcamp) | [APIs >>](../05_apis/13_crear_y_llamar_datos.md#trabajar-con-apis)


<br/><hr/>
<hr/><br/>


## Acceder a los valores de una URL

En este apartado vamos a crear un nuevo archivo al que acceder para entrar en más detalle dentro de nuestros proyectos, lo llamaremos `portfolio-detail.js`. Aquí se accedería para poder visualizar una habilidad, un proyecto o una empresa en concreto, por ejemplo.

Cada vez que clicáramos en un item del porfolio, nos llevaría a una URL que perteneciera a dicho ítem en concreto.

Para hacer esto, vamos a tener que crear nuevas rutas en el archivo `app.js`:

```js
// app.js

// ...

import PortfolioDetail from './portfolio/portfolio-detail';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                /* ... */

                <Router>
                    <div>
                        <NavigationContainer />

                        <Switch>
                            /* ... */

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

A continuación, añadimos el componente creado en la ruta `portfolio/portfolio-detail.js`:

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
            /* ... */

            <Link to={`/portfolio/${props.slug}`}>Link</Link>
        </div>
    )
}
```

<br/>

Finalmente, hemos añadido un link que nos llevará a la URL que corresponda a cada item del portfolio.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Sin coincidencias de URL

En ocasiones, se trata de acceder a través de una URL a una dirección que no existe. En estos casos, es probable que se desee mostrar un mensaje o página de error.

En este apartado, se va a mostrar cómo hacer esto.

En primer lugar, crearemos un nuevo componente llamado `no-match.js`, y lo crearemos dentro del directorio `components/pages`:

```js
// no-match.js

import React from 'react';
import { Link } from 'react-router-dom';

export default function() {
    return (
        <div>
            <h2>We couldn't find that page</h2>
            <Link to='/'>Return to homepage</Link>
        </div>
    );
}
```

<br/>

Ahora, vamos a modificar el componente `app.js` para que, en caso de que no se encuentre la URL, se muestre el componente `no-match.js`:

```js
// app.js

// ...

import NoMatch from './pages/no-match';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                /* ... */

                <Router>
                    <div>
                        /* ... */

                        <Switch>
                            /* ... */
                            <Route component={NoMatch} />
                        </Switch>
                    </div>
                </Router>
            </div>
        );
    }
}
```

<br/>

Con esto, estamos indicando que, en caso de que no se encuentre la URL, se muestre el componente `no-match.js`.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## URLs anidadas en Portfolio

Si escribimos URLs como:

```
http://localhost:3000/portfolio/lo-que-sea
```

<br/>

Como tenemos la ruta:

```js
// app.js

<Route path='/portfolio/:slug' component={PortfolioDetail} />
```

<br/>

Se va a mostrar el componente `portfolio-detail.js` con el mensaje `Portfolio Detail for lo-que-sea` como título.

Sin embargo, si se trata acceder a una URL como:

```
http://localhost:3000/portfolio/lo-que-sea/otra-cosa
```

<br/>

Lo que ocurre es que se muestra el mismo componente que antes, incluyendo el mismo mensaje, debido a que la ruta coincide con la ruta que hemos indicado en `app.js`.

Si lo que queremos es que en caso de tratar acceder a esta segunda URL se muestre el componente de `no-match.js` que hemos creado antes, debemos añadir la propiedad `exact` a la ruta:

```js
// app.js

<Route exact path='/portfolio/:slug' component={PortfolioDetail} />
```


<br/><hr/>
<hr/><br/>


[<< LINKS](./11_links.md#links) | [HOME](../../../README.md#devcamp) | [APIs >>](../05_apis/13_crear_y_llamar_datos.md#trabajar-con-apis)
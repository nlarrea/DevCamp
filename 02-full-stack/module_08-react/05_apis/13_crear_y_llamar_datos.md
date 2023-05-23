# Trabajar con APIs

<div id="index"></div>

* [Crear información en el servidor](#crear-infromación-en-el-servidor)
* [Importar y usar Axios](#importar-y-usar-axios)
* [Reorganizar el código](#reorganizar-el-código)

<br/>


[<< ACCESS URL](../04_routes_and_links/12_access_url.md#trabajar-con-urls) | [HOME](../../../README.md#devcamp) | [RENDER DATA >>](./14_render_data.md#render-data)


<br/><hr/>
<hr/><br/>


Hasta ahora, hemos mostrado los datos que hemos *hardcodeado* por pantalla.

Ahora, vamos a trabjar con APIs para obtener datos reales. En este caso, dichos datos serán de un servidor proporcionado por Bottega, llamado [DevCamp Space](https://www.devcamp.space/).

En este servidor, tras crear una cuenta, podemos introducir diferentes datos, y de aquí obtendremos la información que mostraremos en nuestra aplicación.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Crear infromación en el servidor

Una vez entremos en el servidor, podremos acceder a una sección llamada 'Portfolio', donde podremos crear diferentes entradas de datos.

Una vez dentro, entraremos en la sección 'Portfolio Items', y crearemos un par de ítems nuevos para poder mostrarlos por pantalla.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Importar y usar Axios

Para poder trabajar con APIs, vamos a usar una librería llamada [Axios](https://www.npmjs.com/package/axios).

Para instalarla, ejecutaremos el siguiente comando:

```bash
npm i axios
```

<br/>

Ahora que se ha instalado, vamos a usarla en nuestro componente `app.js`:

```js
// app.js

// ...
import axios from 'axios';

export default class App extends Component {
    // añadimos el constructor para poder usar 'this.getPorfolioItems()'
    constructor() {
        super();

        this.getPorfolioItems = this.getPorfolioItems.bind(this);
    }

    // creamos una función para obtener los datos del servidor
    getPorfolioItems() {
        axios
            .get('https://nlarrea.devcamp.space/portfolio/portfolio_items')
            .then(response => {
                // IMPORTANTE: debe usarse arrow function para usar 'this' sin errores
                console.log('response data', response);
            })
            .catch(error => {
                console.log(error);
            });
    }

    render() {
        // llamada a la función para obtener los datos
        this.getPorfolioItems();

        //...
    }
}
```

<br/>

Si arrancamos el servidor, veremos que muestra los items que hayamos añadido previamente al servidor.

Podemos confirmar que se muestran los datos por consola correctamente, lo que significa que la API y la llamada de la misma están funcionando correctamente.


<br/><hr/>
<hr/><br/>


## Reorganizar el código

Ahora que hemos comprobado que los datos funcionan correctamente, vamos a reorganizar el código para situar dicha llamada en un lugar más adecuado.

Lo que queremos es que la información proporcionada por la API se muestre en la página *home*, por lo que es el lugar lógico donde situar la llamada.

Sin embargo, dentro de esta página se llama al componente `PortfolioContainer`, por lo que es en este componente donde situaremos la llamada a la API.

<br/>

Vamos a eliminar todo lo escrito en el apartado anterior del archivo `app.js`, y vamos a situar la llamada a la API en el componente `PortfolioContainer`, en el archivo `portfolio-container.js`.

Así es cómo quedaría el código de `app.js`:

```js
import React, { Component } from 'react';
import moment from 'moment';
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom';

import NavigationContainer from './navigation/navigation-container';
import Home from './pages/home';
import About from './pages/about';
import Contact from './pages/contact';
import Blog from './pages/blog';
import PortfolioDetail from './portfolio/portfolio-detail';
import NoMatch from './pages/no-match';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                <h1>nlarrea</h1>
                <div>
                    {moment().format('MMMM Do YYYY, hh:mm:ss a')}
                </div>

                <Router>
                    <div>
                        <NavigationContainer />

                        <Switch>
                            <Route exact path="/" component={Home}/>
                            <Route path="/about-me" component={About}/>
                            <Route path="/contact" component={Contact}/>
                            <Route path="/blog" component={Blog}/>

                            <Route exact path='/portfolio/:slug' component={PortfolioDetail} />
                            
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

A continuación, así es como debe verse el código de `portfolio-container.js`:

```js
// portfolio-container.js

// ...
import axios from 'axios';

// ...

export default class PortfolioContainer extends Component {
    constructor() {
        // ...

        this.getPorfolioItems = this.getPorfolioItems.bind(this);
    }

    getPortfolioItems() {
        axios
            .get('https://nlarrea.devcamp.space/portfolio/portfolio_items')
            .then(response => {
                this.setState({
                    data: response.data.portfolio_items
                });
            })
            .catch(error => {
                console.error(error);
            });
    }

    render() {
        this.getPortfolioItems();

        // ...
    }
}
```

<br/>

Tras hacer esto, comprobaremos que vuelven a mostrarse los datos de la misma manera que antes por consola.

Viendo que así es, podemos volver a confirmar que todo funciona correctamente.


<br/><hr/>
<hr/><br/>


[<< ACCESS URL](../04_routes_and_links/12_access_url.md#trabajar-con-urls) | [HOME](../../../README.md#devcamp) | [RENDER DATA >>](./14_render_data.md#render-data)
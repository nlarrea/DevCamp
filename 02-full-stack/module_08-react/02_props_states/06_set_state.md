# Modificar el estado en React

<div id="index"></div>

* [Función sin parámetros](#función-sin-parámetros)
* [Función con parámetros](#función-con-parámetros)

<br/>


[<< PROPS, STATE, THIS](./05_props_states_this.md#props-state--this) | [HOME](../../../README.md#devcamp) | [CONDICIONALES >>](../03_conditionals/07_conditionals.md#condicionales)


<br/><hr/>
<hr/><br/>


## Función sin parámetros

A pesar de haberlo visto en apartados anteriores de forma menos explícita, en este apartado vamos a ver cómo modificar el estado de un componente en React.

Para ello, vamos a volver al proyecto del portfolio, concretamente, vamos a crear una función que modifique el título de la página cuando el usuario pulse un botón.

Para ello, vamos a crear la siguiente función dentro de la clase `PortfolioContainer`:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    constructor() {
        super();


        this.state = {
            pageTitle: 'Welcome to my portfolio',
            data: [
                {title: 'Primer dato'},
                {title: 'Segundo dato'},
                {title: 'Tercer dato'}
            ]
        }
    }

    // ...

    handlePageTitleUpdate() {
        this.setState({
            pageTitle: 'Something Else'
        });
    }

    // ...
}
```

<br/>

Hemos creado la función. El nombre de la función es aquel que nosotros decidamos darle, y en su interior, lo que hacemos es llamar a la función `setState()`, función propia de React, que nos permite modificar el estado de un componente.

Dentro de `setState()`, debemos pasar un objeto, por ello, pasamos como `key` el valor que queremos modificar (*en este caso, el valor de `pageTitle`*), y como `value` el nuevo valor que queremos que tenga.

Ahora, debemos crear un botón para llamar a dicha función cuando éste sea pulsado:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    constructor() {
        super();

        super();


        this.state = {
            pageTitle: 'Welcome to my portfolio',
            data: [
                {title: 'Primer dato'},
                {title: 'Segundo dato'},
                {title: 'Tercer dato'}
            ]
        }
    }

    // ...

    handlePageTitleUpdate() {
        this.setState({
            pageTitle: 'Something Else'
        });
    }

    render() {
        return (
            <div>
                <h2>{this.state.pageTitle}</h2>

                <button onClick={this.handlePageTitleUpdate}>Change Title</button>

                {this.portfolioItems()}

                <hr/>

                <button onClick={this.handlePageTitleUpdate}>Change Title</button>
            </div>
        );
    }
}
```

<br/>

A priori, parece que este código debería funcionar. Sin embargo, no es así. Para poder funcionar, la función `handlePageTitleUpdate()` debe tener acceso al `this` de la clase `PortfolioContainer`.

Existen diferentes formas de hacerlo. La primera de ellas, es llamar a la función desde el `onClick` del botón de la siguiente forma:

```js
<button onClick={this.handlePageTitleUpdate.bind(this)}>Change Title</button>
```

<br/>

Esta forma es correcta, pero si debemos llamar a la función en repetidas ocasiones, puede resultar tedioso. Por ello, existe una segunda forma que consiste en añadir una línea de código en el constructor. He aquí el código completo:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    constructor() {
        super();


        this.state = {
            pageTitle: 'Welcome to my portfolio',
            data: [
                {title: 'Primer dato'},
                {title: 'Segundo dato'},
                {title: 'Tercer dato'}
            ]
        };

        // línea de código añadida
        this.handlePageTitleUpdate = this.handlePageTitleUpdate.bind(this);
    }

    // ...

    handlePageTitleUpdate() {
        this.setState({
            pageTitle: "Something Else"
        });
    }

    render() {
        return (
            <div>
                <h2>{this.state.pageTitle}</h2>

                {this.portfolioItems()}

                <hr/>

                <button onClick={this.handlePageTitleUpdate}>Change Title</button>
            </div>
        )
    }
}
```


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Función con parámetros

Vamos a ver este ejemplo con un selector de datos. Es decir, buscamos que al pulsar un botón, se filtren los resultados mostrando aquellos que coincidan con el dato que hemos seleccionado.

Para ello, vamos a crear una nueva función que se encargue de filtrar los datos del estado `data`:

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
            ]
        };
    }

    // ...

    handleFilter(filter) {
        this.setState({
            data: this.state.data.filter(obj => obj.category === filter)
        });
    }

    // ...
}
```

<br/>

Hemos creado la función encargada de filtrar los datos en función de un dato `filter` recibido.

Ahora, debemos crear los botones que llamen a dicha función:

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
            ]
        };

        this.handleFilter = this.handleFilter.bind(this);
    }

    // ...

    handleFilter(filter) {
        this.setState({
            data: this.state.data.filter(obj => obj.category === filter)
        });
    }

    render() {
        return (
            <div>
                <h2>{this.state.pageTitle}</h2>

                <button onClick={() => this.handleFilter('eCommerce')}>eCommerce</button>
                <button onClick={() => this.handleFilter('Scheduling')}>Scheduling</button>
                <button onClick={() => this.handleFilter('Enterprise')}>Enterprise</button>

                {this.portfolioItems()}
            </div>
        )
    }
}
```

Es importante recordar que debemos añadir la línea que permite a la función `handleFilter()` acceder al `this` de la clase `PortfolioContainer`.

Además, a la hora de llamar a las funciones con eventos, si se añaden paréntesis al llamar a la función, el programa trata de ejecutar dicha función en el momento en el que se carga la página. Lo que significa que tendríamos 3 funciones tratando de ejecutarse a la vez sin que el usuario haya hecho nada.

Para evitar esto, la forma de llamar a dichas funciones **con parámetros** es la siguiente:

```js
<button onClick={() => this.function(parameter)}>Button text</button>
```

<br/>

Se debe tener en cuenta, que si los datos están *hardcodeados*, se clica el botón para filtrar datos, y se vuelve a clicar el botón para mostrar otros datos, esto no funcionará. Esto se debe a que el estado `data` ya no contiene todos los datos, sino que contiene los datos filtrados. Por ello, al tratar de mostrar otros datos, no se verá nada en pantalla, ya que no existe ningún dato que coincida con el filtro.

Si se quisiera arreglar esto, habría que encontrar una manera de devolver los datos originales al estado `data` antes de realizar el filtro.


<br/><hr/>
<hr/><br/>


[<< PROPS, STATE, THIS](./05_props_states_this.md#props-state--this) | [HOME](../../../README.md#devcamp) | [CONDICIONALES >>](../03_conditionals/07_conditionals.md#condicionales)
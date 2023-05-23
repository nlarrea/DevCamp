# Componentes de React


<span id="index"></span>

* [Crear un componente de clase](#crear-un-componente-de-clase)
* [Componentes de clase vs funcionales](#componentes-de-clase-vs-funcionales)
    * [Cuándo usar cada tipo de componente](#cuándo-usar-cada-tipo-de-componente)
    * [Constructores en los componentes de clase](#constructores-en-los-componentes-de-clase)
* [Funciones customizadas](#funciones-customizadas)
    * [Pasar datos a los componentes (props)](#pasar-datos-a-los-componentes-props)

<br/>


[<< FILE SYSTEM](../00_introduction/02_file_system.md#react-file-system) | [HOME](../../../README.md#devcamp) | [STATE >>](../02_props_states/04_working_with_states.md#trabajar-con-estados)


<br/><hr/>
<hr/><br/>


Aunque parece muy evidente, el primer paso a seguir para poder utilizar los componentes de React, es importar React.

Si abrimos el archivo `app.js`, veremos que ya tenemos importado React, por lo que podemos empezar a crear nuestros componentes.

```js
import React, { Component } from 'react';
```


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Crear un componente de clase

A continuación, vamos a crear un nuevo archivo (`src/components/portfolio-container.js`) y vamos a crear un componente en él de la siguiente manera:
    
```js
// portfolio-container.js

// importamos React
import React, { Component } from 'react';

// creamos un componente basado en una clase
export default class PortfolioContainer extends Component {
    /* los componentes basados en clases deben tener un método
    llamado render */
    render() {
        // devolvemos el contenido del componente
        return (
            // aquí va el contenido
            <div>
                <h2>Portfolio items go here...</h2>
            </div>
        )
    }
}
```

<br/>

Ahora, dentro del archivo `app.js`, debemos importar el componente que acabamos de crear. Después lo usaremos para que se vea debajo del título de la página.

```js
// app.js

import React, { Component } from 'react';
import moment from 'moment';

import PortfolioContainer from './portfolio-container';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                <h1>nlarrea</h1>
                <PortfolioContainer />
                <div>
                    {moment().format('MMMM Do YYYY, hh:mm:ss a')}
                </div>
            </div>
        );
    }
}
```

<br/>

Ahora, si arrancamos la aplicación, veremos que se muestran las siguientes líneas de texto (con sus respectivos estilos):

```txt
nlarrea
Portfolio Items go here...
May 10th 2023, 12:01:18 pm
```


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Componentes de clase vs funcionales

Existen dos tipos de componentes en React:

* Class-based components
* Functional components (también llamados *presentational components*)

<br/>

Para ver este tipo de componentes, vamos a continuar creando un portfolio a modo de ejemplo.

Por ello, para continuar, vamos a comenzar creando un nuevo directorio dentro de la carpeta `src/components` llamado `portfolio`. En su interior, añadiremos el archivo `portfolio-container.js` creado anteriormente, modificando su importación para que apunte a la nueva ruta en el archivo `app.js`.

```js
// app.js

import PortfolioContainer from './portfolio/portfolio-container';
```

<br/>

Después, crearemos un nuevo archivo llamado `portfolio-item.js` dentro de la carpeta `portfolio`.

Hasta ahora, tendremos dos archivos *portfolio*, el primero de ellos, el `portfolio-container.js`, será el que contenga a todos los *portfolio items*. Es un archivo único que puede tener varios ítems en su interior.

Vamos a crear un componente funcional en el archivo `portfolio-item.js`:

```js
// portfolio-item.js

import React from 'react';

export default function() {
    return (
        <div>
            <h3>Portfolio Item</h3>
        </div>
    )
}
```

<br/>

En los componentes funcionales, no hay que importar `{ Component }` porque no vamos a crear una clase que se extienda de `Component`.

Crearemos una función que devuelva el contenido del componente. En este caso, un `div` con un título. Y después, exportaremos la función.

Ahora, debemos volver al archivo `portfolio-container.js` y añadir el componente que acabamos de crear.

```js
// portfolio-container.js

import React, { Component } from 'react';

// importamos el componente funcional
import PortfolioItem from './portfolio-item';

export default class PortfolioContainer extends Component {
    render() {
        return (
            <div>
                <h2>Portfolio Items go here...</h2>

                /* añadimos el componente funcional */
                <PortfolioItem />
            </div>
        )
    }
}
```

<br/>

Si arrancamos la aplicación, veremos que se muestra el título del componente funcional.

```txt
nlarrea
Portfolio Items go here...
Portfolio Item
May 10th 2023, 12:26:39 pm
```

<br/><hr/><br/>


### Cuándo usar cada tipo de componente

Los componentes de clase se utilizan cuando necesitamos tener un estado o cuando necesitamos utilizar el ciclo de vida de los componentes (*State y Lifecycle Hooks*).

Son componentes que se deben usar cuando hace falta usar más lógica en el componente.

Si simplemente se desea renderizar algo, mostrarlo por pantalla, etc. enconces, se utilizan los componentes funcionales.


<br/><hr/><br/>


### Constructores en los componentes de clase

Solo se pueden utilizar constructores en los componentes de clase.

El constructor es una palabra reservada en JavaScript. Es un método que se ejecuta cuando se crea una instancia de una clase. Dentro de él, tienen lugar las configuraciones o valores iniciales.

Se debe tener en cuenta que los componentes de clase se extienden de `Component`, por lo que, si se quiere utilizar un constructor, se debe llamar al constructor de la clase padre.

```js
// portfolio-container.js

import React, { Component } from 'react';

import PortfolioItem from './portfolio-item';

export default class PortfolioContainer extends Component {
    constructor() {
        super();    // llamada al constructor de la clase padre
        console.log('Portfolio container has rendered');
    }

    render() {
        return (
            <div>
                <h2>Portfolio Items go here...</h2>

                <PortfolioItem />
            </div>
        )
    }
}
```

<br/>

En este caso, el contructor no tiene prácticamente ninguna utilidad, sin embargo, aquí es donde normalmente se situan todos los estados iniciales, donde se definen todos los valores de partida, etc.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Funciones customizadas

Vamos a crear una función que, partiendo de una lista con datos, muestre los datos por pantalla creando un componente por cada uno de ellos.

En primer lugar, crearemos la clase. Para ello, abriremos el archivo `portfolio-container.js`, y crearemos una clase o método llamado `portfolioItems()`:

```js
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    // ...

    portfolioItems() {
        const data = ['primer dato', 'segundo dato', 'tercer dato'];

        return data.map(item => {
            // en un .map() siempre hay que devolver algo
            return <PortfolioItem />;
        });
    }

    render() {
        return (
            <div>
                <h2>Portfolio Items go here...</h2>

                /* dentro de 'render()' se usan {} para
                escribir JS */
                {this.portfolioItems()}
            </div>
        )
    }
}
```

<br/>

Si arrancamos la aplicación, veremos que se muestran tres componentes funcionales, uno por cada elemento del array, aunque no es exactamente lo que queremos (*veremos más adelante cómo solucionarlo*).

```txt
nlarrea
May 10th 2023, 12:53:22 pm
Portfolio Items go here...
Portfolio Item
Portfolio Item
Portfolio Item
```


<br/><hr/><br/>


### Pasar datos a los componentes (props)

Hemos visto cómo crear funciones personalizadas para crear tantos elementos como deseemos a partir de una lista de datos, pero ¿cómo podemos pasar datos a los componentes?

Para que esto sea posible, debemos pasar datos de un componente padre a un componente hijo. Para ello, utilizaremos las *props*.

En primer lugar, accederemos al archivo donde estamos llamando al componente funcional, en este caso, el archivo `portfolio-container.js`, y vamos a modificar el método `portfolioItems()` para que envíe datos al componente funcional.

```js
// portfolio-container.js

// ...

portfolioItems() {
    const data = ['primer dato', 'segundo dato', 'tercer dato'];

    return data.map(item => {
        return <PortfolioItem title={item} />;
    });
}

// ...
```

<br/>

Estamos enviando cada dato de la lista (cada `item`) como `title` al componente funcional. Ahora, desde el componente funcional (`portfolio-item.js`), podemos acceder a ese dato.

```js
// portfolio-item.js

// ...

export default function(props) {
    return (
        <div>
            <h3>{props.title}</h3>
        </div>
    )
}
```

<br/>

Indicamos a la función que tiene parámetros usando `props`, y después, podemos acceder a los datos que le estamos enviando desde el componente padre utilizando `props.title`.

`props` es un objeto que contiene todas las propiedades que se le están pasando al componente, por lo que para acceder al `title` enviado, debemos acceder a `props.title`.

Podemos crear tantas propiedades como queramos, y acceder a ellas desde el componente funcional de la misma forma.

Como queremos utilizar código JS dentro de JSX, debemos usar `{}` para llamar al atributo del objeto.

Si arrancamos la aplicación, veremos que se muestran los datos que estamos enviando desde el componente padre.

```txt
nlarrea
May 10th 2023, 1:05:39 pm
Portfolio Items go here...
primer dato
segundo dato
tercer dato
```


<br/><hr/>
<hr/><br/>


[<< FILE SYSTEM](../00_introduction/02_file_system.md#react-file-system) | [HOME](../../../README.md#devcamp) | [STATE >>](../02_props_states/04_working_with_states.md#trabajar-con-estados)
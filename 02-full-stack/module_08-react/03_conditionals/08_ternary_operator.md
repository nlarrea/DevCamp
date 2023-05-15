# Ternarios

De forma similar a la vista en el apartado anterior, podemos trabajar con condicionales en JSX usando el operador ternario.

Vamos a trabajar este concepto creando un nuevo componente, un `navbar`. Para ello, dentro del directorio `components` vamos a crear `navigation/navigation-container.js`.

Antes de crearlo siquiera, en el archivo `app.js` vamos a llamar a dicho componentes:

```jsx
// app.js

//...

//...
import NavigationContainer from './navigation/navigation-container';

export default class App extends Component {
    render() {
        return (
            <div className='app'>
                <NavigationContainer />
                <!-- ... -->
            </div>
        );
    }
}
```

<br/>

Ahora, volvemos al nuevo archivo creado y añadimos el siguiente código:

```jsx
import React, { Component } from "react";

export default class NavigationComponent extends Component {
    constructor() {
        super();
    }

    render() {
        return (
            <div>
                <button>Home</button>
                <button>About</button>
                <button>Contact</button>
                <button>Blog</button>
                <button>Add Blog</button>
            </div>
        );
    }
}
```

<br/>

Queremos conseguir que el botón `Add Blog` solo se muestre si el usuario es administrador. Aún no vamos a trabajar con usuarios, pero podemos simularlo con simples `true` y `false`.

Para ello, vamos a modificar la línea correspondiente para utilizar un operador ternario:

```jsx
// navigation-container.js

{true ? <button>Add Blog</button> : null}
```

<br/>

Con esa línea, no deben verse modificaciones en la página, puesto que se está indicando que se muestre el botón si el valor es `true`, y no se muestre si es `false`, y en este caso es `true`.

Si por el contrario, se modificara de la siguiente manera:

```jsx
// navigation-container.js

{false ? <button>Add Blog</button> : null}
```

<br/>

Debería desaparecer el botón.
# Props, State & This

Para poder entender React, es necesario entender el concepto de `props`, `state` y `this`. En este caso, vamos a explicar cómo trabajar con ellos a través de un ejemplo.

Para el ejemplo, vamos a volver a utilizar la herramienta vista anteriormente para crear un proyecto de React. Para ello, vamos a ejecutar el siguiente comando:

```bash
js-generate
```

<br>

Se selecciona un nombre y el tipo de proyecto que se desea crear.

A continuación, tras ponerle un nombre y desde dentro del directorio del proyecto, vamos a ejecutar el siguiente comando:

```bash
npm start
```

<br>

Ahora se deberían instalar las dependencias necesarias.

Una vez instaladas, ejecutaremos `npm start` para arrancar el servidor de desarrollo.

<br>

Vamos a crear un componente de clase que se llame `JournalList`, por lo que crearemos un nuevo directorio dentro de la carpeta `src` llamado `journals` y dentro de este, crearemos un archivo llamado `journal_list.js`.

Ahora, dentro de este archivo, lo primero que haremos será importar React, una clase que dependa de React y unos datos que por ahora serán *hardcoded*, pero esto ya se cambiará:

```jsx
// journal_list.js

import React, { Component } from 'react';

const rawJournalData = [
    { title: "Post One", content: "Post content", status: "draft" },
    { title: "Post Two", content: "Post content", status: "published" },
    { title: "Post Three", content: "Post content", status: "published" },
    { title: "Post Four", content: "Post content", status: "published" }
]

export default class JournalLList extends Component {
    constructor(props) {
        super();

        this.state = {
            journalData: rawJournalData,
            isOpen: true
        };
    }

    render() {
        return (
            <h2>Heyyy.</h2>
        )
    }
}
```

<br>

Si guardamos y accedemos al servidor, veremos que no ha cambiado absolutamente nada. Esto se debe a que tenemos que importar el componente en el archivo `app.js`:

```jsx
// app.js

import React from 'react';

import JournalList from './journals/journal_list';

function App() {
    return (
        <div className="App">
            <h1>React, Props, and State - Deep Drive</h1>
            <JournalList />
        </div>
    );
}
```

<br>

Ahora veremos cómo en la página se muestra el siguiente texto:

```txt
React, Props, and State - Deep Drive
Heyyy.
```

<br>

Eso significa que el componente se ha importado correctamente.

No tiene mucho sentido *hardcodear* todo lo que se muestre, por lo que vamos a ver cómo trabajar con `props`.

<br>

En el archivo `journal_list.js`, hemos creado un componente de clase y hemos añadido un constructor que tiene un parámetro llamado `props`. Este parámetro es un objeto que contiene todas las propiedades que se le pasan al componente.

Para ver cómo funciona, vamos a llamar al componente desde `app.js` y le vamos a pasar una propiedad llamada `heading` con el valor que queramos que se muestre:

```jsx
// app.js

// ...

return (
    <div className="App">
        <h1>React, Props, and State - Deep Drive</h1>
        <JournalList heading="List 1" />
    </div>
);

// ...
```

<br>

Ahora, en el archivo `journal_list.js`, vamos a añadir lo siguiente:

```jsx
// journal_list.js

// ...

render() {
    return (
        <div>
            <h1>{this.props.heading}</h1>
        </div>
    )
}

// ...
```

<br>

Si guardamos y accedemos al servidor, veremos que se muestra el siguiente texto:

```txt
React, Props, and State - Deep Drive
List 1
```

<br>

Esto significa que el valor pasado como propiedad a JournalList se ha mostrado correctamente.

Adicionalmente, podríamos añadir más componentes como el que acabamos de crear:

```jsx
// app.js

// ...

return (
    <div className="App">
        <h1>React, Props, and State - Deep Drive</h1>
        <JournalList heading="List 1" />
        <JournalList heading="List 2" />
    </div>
);
```

<br>

Haciendo esto, se verá en la página que hay dos componentes iguales, uno con el texto `List 1` y otro con el texto `List 2`.


<br><hr><br>


## Trabajando con props y datos

Ahora vamos a crear otro componente llamado `JournalEntry` que se encargará de mostrar cada una de las entradas del diario. Para ello, vamos a crear otro archivo en el mismo directorio que el anterior, y lo llamaremos `journal_entry.js`.

Dentro de este archivo, vamos a crear un componente que solo va a renderizar contenido, por lo que puede tratarse de un componente funcional:

```jsx
// journal_entry.js

import React from 'react';

export const JournalEntry = () => {
    return (
        <div>
            <h1>Hi there</h1>
            <p>Some amazing content</p>
        </div>
    );
};
```

<br>

Ahora, en el archivo `journal_list.js`, vamos a importar el componente y lo vamos a utilizar dentro del método `render`:

```jsx
// journal_list.js

// ...

import { JournalEntry } from './journal_entry';

// ...

render() {
    return (
        <div>
            <h1>{this.props.heading}</h1>
            <JournalEntry />
        </div>
    );
};

// ...
```

<br>

Si guardamos y accedemos al servidor, veremos que se muestra el siguiente texto:

```txt
React, Props, and State - Deep Drive
List 1
Hi there
Some amazing content
List 2
Hi there
Some amazing content
```

<br>

Se añaden dos componentes `JournalList` en el archivo `app.js`, por lo que se muestran dos componentes `JournalEntry` en la página, cada uno después o dentro de su correspondiente `JournalList`.

<br>

Vamos a eliminar los mensajes *hardcodeados* y vamos a pasarle directamente los mensajes a mostrar en cada componente `JournalEntry` desde el componente `JournalList`. Para ello, primero vamos a modificar el archivo `journal_entry.js` para que reciba las propiedades que le pasemos desde el componente `JournalList`:

```jsx
// journal_entry.js

import React from 'react';

const JournalEntry = props => {
    return (
        <div>
            <h1>{props.title}</h1>
            <p>{props.content}</p>
        </div>
    );
};
```

<br>

Ahora, en el archivo `journal_list.js`, vamos a modificar el método `render` para que pase las propiedades al componente `JournalEntry`:

```jsx
// journal_list.js

// ...

render() {
    return (
        <div>
            <h1>{this.props.heading}</h1>
            <JournalEntry title="Some Title" content="More Content" />
        </div>
    );
};

// ...
```

<br>

Si guardamos y accedemos al servidor, veremos que se muestra el siguiente texto:

```txt
React, Props, and State - Deep Drive
List 1
Some Title
More Content
List 2
Some Title
More Content
```

<br>

Vamos a eliminar de `app.js` el segundo componente `JournalList` y vamos a añadir componentes `JournalEntry` con diferentes títulos en el archivo `journal_list.js`:

```jsx
// journal_list.js

// ...

render() {
    return (
        <div>
            <h1>{this.props.heading}</h1>
            <JournalEntry title="Some Title" content="More Content" />
            <JournalEntry title="Some Other Title" content="Even More Content" />
        </div>
    );
};
```

<br>

Si guardamos y accedemos al servidor, veremos que se muestra el siguiente texto:

```txt
React, Props, and State - Deep Drive
List 1
Some Title
More Content
Some Other Title
Even More Content
```

<br>

Dentro del archivo, vamos a crear una variable que contenga todos los datos que queremos mostrar en la página:

```jsx
// journal_list.js

// ...

export default class JournalList extends Component {
    constructor() {
        // ...
    }

    render() {
        const journalEntries = this.state.journalData.map(journalEntry => {
            return (
                /* key es un atributo especial que se le pasa
                a cada elemento de una lista, como un ID */
                <div key={journalEntry.title}>
                    <JournalEntry
                        title={journalEntry.title}
                        content={journalEntry.content}
                    />
                </div>
            );
        });

        return (
            <div>
                <h2>{this.props.heading}</h2>
                {journalEntries}    {/* llamada a la variable */}
            </div>
        )
    }
}
```

<br>

Si guardamos y accedemos al servidor, veremos que se muestra el siguiente texto:

```txt
React, Props, and State - Deep Drive
List 1
Post One
Post Content
Post Two
Post Content
Post Three
Post Content
```

<br>

Hay que tener en cuenta que como hemos indicado `key={journalEntry.title}` en el componente `JournalEntry`, cada elemento de la lista debe tener un título diferente, ya que si no, React no sabrá a qué elemento de la lista nos referimos.


<br><hr><br>


## Modificar el estado

Vamos a crear un nuevo método dentro de la clase `JournalList`, lo usaremos para llamarlo cada vez que se pulse un botón, y su función será eliminar el contenido de la lista:

```jsx
// journal_list.js

// ...

export default class JournalList extends Component {
    constructor() {
        // ...
    }

    clearEntries() {
        this.setState({ journalData: [] });
    }

    render() {
        // ...

        return (
            <div>
                <h2>{this.props.heading}</h2>
                {journalEntries}

                <button onClick={this.clearEntries}>Clear Journal Entries</button>
            </div>
        )
    }
}
```

<br>

Si miramos ahora el servidor, veremos que se nos muestra el mismo texto que el mencionado la última vez, sin embargo, aparece un botón en la parte inferior.

Si pulsamos ese botón se borrará el contenido de la lista, pero no se actualizará la página. Esto es porque React no actualiza la página cada vez que se modifica el estado.

<br>

Vamos a crear otros dos métodos, el primero para mostrar el contenido de la lista y el segundo para hacer la función de *toggle*:

```jsx
// journal_list.js

// ...

export default class JournalList extends Component {
    constructor() {
        // ...
    }

    clearEntries = () => {
        this.setState({ journalData: [], isOpen: false });
    }

    showAllEntries = () => {
        this.setState({ journalData: journalData, isOpen: true });
    }

    toggleStatus = () => {
        if (this.state.isOpen) {
            this.setState({ journalData: [], isOpen: false });
        } else {
            this.setState({ journalData: journalData, isOpen: true });
        }
    }

    render() {
        // ...

        return (
            <div>
                <h2>{this.props.heading}</h2>
                {journalEntries}

                <button onClick={this.clearEntries}>Clear Journal Entries</button>
                <button onClick={this.showAllEntries}>Show All Journal Entries</button>
                <button onClick={this.toggleStatus}>Toggle Journal Entries</button>
            </div>
        )
    }
}
```
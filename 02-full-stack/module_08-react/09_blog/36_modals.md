# Modals

<div id='index'></div>

* [Instalar react-modal](#instalar-react-modal)
* [Crear un Modal](#crear-un-modal)
* [Abrir y cerrar Modals](#abrir-y-cerrar-un-modal)
    * [Abrir un Modal](#abrir-un-modal)
    * [Cerrar un Modal](#cerrar-un-modal)
* [Dar estilos al Modal](#dar-estilos-al-modal)

<br/>


[<< SCROLL INFINITO](./35_scroll_infinito.md#scroll-infinito) | [HOME](../../../README.md#devcamp) | [BLOG FORM >>](./37_blog_form.md#blog-form)


<br/><hr/>
<hr/><br/>


Vamos a utilizar ***Modals*** para crear una especie de formulario desde el cual poder introducir nuevos Blogs.

En esta sección veremos cómo instalar, utilizar y customizar ***Modals*** en nuestra aplicación.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Instalar react-modal

Lo primero que haremos para poder usar modals es importar la librería ***react-modal*** en nuestro proyecto.

Para ello, desde la terminal, nos situamos en la carpeta raíz de nuestro proyecto y ejecutamos el siguiente comando:

```bash
npm i react-modal
```

<br/>

Una vez instalada, veremos que nuestro `package.json` se ha actualizado con la nueva dependencia.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Crear un Modal

Una vez instalada la librería, vamos a crear un ***Modal*** para poder introducir nuevos Blogs en nuestra aplicación.

Para ello, vamos a crear un nuevo archivo (*directorio `src/components/modals`*) llamado `blog-modal.js`, y en él crearemos el siguiente componente:

```js
// blog-modal.js

import React, { Component } from 'react';
import ReactModal from 'react-modal';

export default class BlogModal extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <ReactModal isOpen={true}>
                <h1>I'm in a modal!</h1>
            </ReactModal>
        );
    }
}
```

<br/>

Por ahora, lo único que hemos hecho es importar el componente `ReactModal` de la librería `react-modal`, y hemos creado un componente que renderiza un `ReactModal` con un título.

A este componente le hemos pasado una prop `isOpen` con el valor `true`, lo que hace que el modal se muestre en pantalla. Más adelante, lo modificaremos para que se abra el modal cuando hagamos click en un botón, por ahora, lo dejamos así para ver que funciona y se abra automáticamente.

<br/>

Ahora, volveremos al archivo `blog.js` y lo importaremos para poder utilizarlo:

```js
// blog.js

// ...
import BlogModal from './modals/blog-modal';

export default class Blog extends Component {
    // ...

    render() {
        return (
            <div className='blog-container'>
                <BlogModal />
                
                /* ... */
            </div>
        );
    }
}
```

<br/>

Hemos añadido el componente en la parte superior del `return` del método `render()`. Esto nos facilitará saber si en un componente se están renderizando modals o no.

Ahora, al arrancar la app y entrar en la página de Blogs, veremos que se nos muestra el modal con el título que hemos definido.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Abrir y cerrar Modals

Hasta ahora, hemos creado un modal que se abre y se mantiene abierto automáticamente. En esta sección, veremos cómo abrir y cerrar modals de forma manual, a base de pulsar botones o links.


<br/><hr/><br/>


### Abrir un Modal

Para abrir un modal, lo primero que haremos será modificar la propiedad `isOpen` del componente `BlogModal` para que sea dinámica, y no esté siempre a `true`:

```js
// blog-modal.js

// ...

export default class BlogModal extends Component {
    // ...

    render() {
        return (
            <ReactModal isOpen={this.props.modalIsOpen}>
                /* ... */
            </ReactModal>
        );
    }
}
```

<br/>

Ahora que nuestro modal se abre en base a una prop, vamos a modificar el componente `Blog` para modificar este valor:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...

        this.state = {
            // ...
            blogModalIsOpen: false
        };

        // ...
        this.handleNewBlogClick = this.handleNewBlogClick.bind(this);
    }

    handleNewBlogClick() {
        this.setState({
            blogModalIsOpen: true
        });
    }

    // ...

    render() {
        // ...

        return (
            <div className='blog-container'>
                <BlogModal modalIsOpen={this.state.blogModalIsOpen} />

                <div className="new-blog-link">
                    <a onClick={this.handleNewBlogClick}>
                        Open Modal
                    </a>
                </div>

                /* ... */
            </div>
        );
    }
}
```

<br/>

Hemos creado un nuevo estado `blogModalIsOpen` que inicializamos a `false`, y hemos creado un método `handleNewBlogClick()` que se encarga de cambiar el valor de esta propiedad a `true`.

Después, hemos añadido un link que, al hacer click, ejecuta este nuevo método, y, como resultado, se abre el modal.


<br/><hr/><br/>


### Cerrar un Modal

Ahora que ya sabemos cómo abrir un modal, vamos a ver cómo cerrarlo.

En primer lugar, vamos a añadir una nueva propiedad al componente `ReactModal` que se está renderizando en el componente `BlogModal`:

```js
// blog-modal.js

// ...

export default class BlogModal extends Component {
    // ...

    render() {
        return (
            <ReactModal
                // ...
                onRequestClose={() => {
                    console.log('testing modal close');
                }}
            >
                /* ... */
            </ReactModal>
        );
    }
}
```

<br/>

Si ejecutamos el código y abrimos el modal, veremos que se imprime el mensaje por pantalla siempre que se clica fuera del modal, o se pulsa la tecla `ESC`. Esto siginifica que podemos hacer que el modal se cierre en estos casos.

Modificamos el `console.log()` por lo siguiente:

```js
// blog-modal.js

// ...

export default class BlogModal extends Component {
    // ...

    render() {
        return (
            <ReactModal
                // ...
                onRequestClose={() => {
                    this.props.handleModalClose();
                }}
            >
                /* ... */
            </ReactModal>
        );
    }
}
```

<br/>

Ahora, accedemos al archivo `blog.js` y creamos y pasamos dicho método como `prop` al componente `BlogModal`:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...
        this.handleModalClose = this.handleModalClose.bind(this);
    }

    // ...

    handleModalClose() {
        this.setState({
            blogModalIsOpen: false
        });
    }

    // ...

    render() {
        // ...

        return (
            <div className='blog-container'>
                <BlogModal
                    /* ... */
                    handleModalClose={this.handleModalClose}
                />

                /* ... */
            </div>
        );
    }
}
```

<br/>

Ahora, si abrimos el modal y hacemos click fuera de él, veremos que se cierra. También se cierra si pulsamos la tecla `ESC`.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Dar estilos al Modal

Para estilar el Modal, lo que haremos será modificar el código del componente `BlogModal` de tal forma que creemos los estilos `inline` en el propio componente.

Esto lo hacemos porque queremos que se sobreescriban los estilos por defecto de la librería `react-modal`.

Para ello, leyendo la [documentación de la librería](https://www.npmjs.com/package/react-modal), veremos que podemos crear un objeto con los estilos que queremos y aplicarlo en la propiedad `style` del componente `ReactModal`:

```js
// blog-modal.js

// ...

export default class BlogModal extends Component {
    constructor(props) {
        // ...

        this.customStyles = {
            content: {
                width: '800px',
                marginRight: '-50%',
                top: '50%',
                left: '50%',
                right: 'auto',
                transform: 'translate(-50%, -50%)'
            },
            overlay: {
                backgroundColor: 'rgba(1, 1, 1, 0.75)'
            }
        };
    }

    render() {
        return (
            <ReactModal
                /* ... */
                style={this.customStyles}
            >
                /* ... */
            </ReactModal>
        );
    }
}
```

<br/>

Hemos creado un objeto `customStyles` que contiene dos propiedades: `content` y `overlay`. El nombre de estas propiedades coincide con los nombres de las clases que traen por defecto los estilos de la librería `react-modal`, y son los que queremos sobreescribir.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Corregir errores de consola

Si abrimos el modal, veremos que nos aparece un error en la consola. Este error es debido a la accesibilidad de la librería `react-modal` cuando se está utilizando un elemento como el *screen reader*.

Para solucionarlo, abriremos el archivo `index.html` y miraremos cuál es el nombre de la clase o id de nuestra aplicación (*en nuestro caso, es una clase llamada `app-wrapper`*).

Sabiendo esto, volveremos al archivo `blog-modal.js` y añadiremos la siguiente línea de código debajo de las importaciones:

```js
ReactModal.setAppElement('.app-wrapper');
```


<br/><hr/>
<hr/><br/>


[<< SCROLL INFINITO](./35_scroll_infinito.md#scroll-infinito) | [HOME](../../../README.md#devcamp) | [BLOG FORM >>](./37_blog_form.md#blog-form)
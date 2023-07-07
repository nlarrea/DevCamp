# Modals

<div id='index'></div>

* [Instalar react-modal](#instalar-react-modal)
* [Crear un Modal](#crear-un-modal)

<br/>


[<< SCROLL INFINITO](./35_scroll_infinito.md#scroll-infinito) | [HOME](../../../README.md#devcamp)


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
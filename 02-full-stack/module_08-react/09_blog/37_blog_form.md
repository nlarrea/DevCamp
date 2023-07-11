# Blog Form

<div id="index"></div>

* [Crear el componente BlogForm](#crear-el-componente-blogform)

<br/>


[<< MODALS](./36_modals.md#modals) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


En esta sección vamos a crear el formulario para crear nuevos blogs y cargarlos a la página de forma automática.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href="#index">Volver arriba</a>
</div>


## Crear el componente BlogForm

Vamos a crear un nuevo componente llamado `BlogForm`. Para ello, dentro de la carpeta `src/components/blog` crearemos el archivo `blog-form.js` con el siguiente contenido:

```js
// blog-form.js

import React, { Component } from 'react';

export default class BlogForm extends Component {
    render() {
        return (
            <form>
                <input type="text" />
                <input type="text" />

                <button>Save</button>
            </form>
        );
    }
}
```

<br/>

Ahora, como queremos que este formulario se muestre en el modal que hemos creado en la sección anterior, vamos a importar este componente en el archivo `blog-modal.js`:

```js
// blog-modal.js

// ...

import BlogForm from '../blog/blog-form';

// ...

export default class BlogModal extends Component {
    // ...

    render() {
        return (
            <ReactModal
                /* ... */
            >
                <BlogForm />
            </ReactModal>
        );
    }
}
```

<br/>

Si arrancamos la aplicación, veremos que al abrir el modal se mostrarán dos `inputs` de tipo texto y un botón.
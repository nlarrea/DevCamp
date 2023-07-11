# Blog Form

<div id="index"></div>

* [Crear el componente BlogForm](#crear-el-componente-blogform)
* [Crear los handlers para los inputs](#crear-los-handlers-para-los-inputs)
* [Crear Blogs](#crear-blogs)
    * [Enviar datos a la API](#enviar-datos-a-la-api)
    * [Añadir el formulario a la app](#añadir-el-formulario-a-la-app)

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


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href="#index">Volver arriba</a>
</div>


## Crear los handlers para los inputs

En primer lugar, vamos a añadir los `handlers` para los inputs. Para ello, comenzaremos por crear el encargado de manejar los datos desde el componente padre (`blog-modal.js`):

```js
// blog-modal.js

// ...

export default class BlogModal extends Component {
    constructor(props) {
        // ...

        this.handleSuccessfulFormSubmission = this.handleSuccessfulFormSubmission.bind(this);
    }


    handleSuccessfulFormSubmission(blog) {
        console.log('blog from blog form', blog);
    }


    render() {
        return(
            <ReactModal /* ... */>
                <BlogForm
                    handleSuccessfulFormSubmission={this.handleSuccessfulFormSubmission}
                />
            </ReactModal>
        );
    }
}
```

<br/>

Después, accederemos al componente hijo (`blog-form.js`) y crearemos los `handlers` para los inputs:

```js
// blog-form.js

// ...

export default class BlogForm extends Component {
    constructor(props) {
        super(props);

        this.state = {
            title: '',
            blog_status: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleSubmit(event) {
        this.props.handleSuccessfulFormSubmission(this.state);
        event.preventDefault();
    }


    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }


    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input
                    type="text"
                    name='title'
                    placeholder='Blog Title'
                    onChange={this.handleChange}
                    value={this.state.title}
                />
                
                <input
                    type="text"
                    name='blog_status'
                    placeholder='Blog Status'
                    onChange={this.handleChange}
                    value={this.state.blog_status}
                />

                /* ... */
            </form>
        );
    }
}
```

<br/>

Ahora, al entrar en la aplicación y abrir el modal, podremos escribir en los inputs y ver cómo se muestra el estado del componente hijo a través del `handler` del componente padre.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href="#index">Volver arriba</a>
</div>


## Crear Blogs

### Enviar datos a la API

Ahora que hemos visto que los `handlers` funcionan correctamente, vamos a emparejar el formulario con la API. Para ello, comenzaremos por abrir el archivo `blog-form.js` y añadir el siguiente código:

```js
// blog-form.js

// ...
import axios from 'axios';

export default class BlogForm extends Component {
    // ...


    buildForm() {
        let formData = new FormData();

        formData.append('portfolio_blog[title]', this.state.title);
        formData.append('portfolio_blog[blog_status]', this.state.blog_status);

        return formData;
    }


    handleSubmit(event) {
        axios.post(
            'https://nlarrea.devcamp.space/portfolio/portfolio_blogs',
            this.buildForm(),
            { withCredentials: true }
        ).then(response => {
            this.props.handleSuccessfulFormSubmission(response.data);
        }).catch(error => {
            console.log('handleSubmit for blog error', error);
        });

        event.preventDefault();
    }


    // ...
}
```

<br/>

Hemos utilizado el `prop` del `handler` creado en el componente padre para mostrar los datos que se han enviado a la API.

Aún no hemos actualizado la página, pero si abrimos la web donde tenemos la API y refrescamos, veremos que lo que escribamos en el formulario se añade a la lista de blogs.


<br/><hr/><br/>


### Añadir el formulario a la app

Una vez que hemos comprobado que el blog se crea correctamente, vamos a hacer que éste se muestre en la aplicación.

Comenzaremos por el archivo `blog-form.js` y modificaremos el siguiente código:

```js
// blog-form.js

// ...

export default class BlogForm extends Component {
    // ...


    handleSubmit(event) {
        axios.post(/* ... */)
        .then(response => {
            this.props.handleSuccessfulFormSubmission(response.data.portfolio_blog);

            // clear the blog form
            this.setState({
                title: '',
                blog_status: ''
            });
        }).catch(error => {
            // ...
        });

        // ...
    }


    // ...
}
```

<br/>

Hemos modificado los datos enviados al `handler` del componente padre para que sólo se muestre el blog que se ha creado.

Además, para vaciar los inputs del formulario, hemos modificado el estado del componente.

<br/>

Ahora, accederemos al archivo `blog-modal.js` y modificaremos el siguiente código:

```js
// blog-modal.js

// ...

export default class BlogModal extends Component {
    // ...


    handleSuccessfulFormSubmission(blog) {
        this.props.handleSuccessfulNewBlogSubmission(blog);
    }


    // ...
}
```

<br/>

Aún no hemos creado ese `handler` que se ha obtenido como `prop`, pero lo que hemos hecho es enviar el blog que se ha creado al componente padre, es decir, al componente `Blog`.

<br/>

Por último, accederemos al archivo `blog.js` y modificaremos el siguiente código:

```js
// blog.js

// ...

export default class Blog extends Component {
    constructor() {
        // ...

        this.handleSuccessfulNewBlogSubmission = this.handleSuccessfulNewBlogSubmission.bind(this);
    }


    handleSuccessfulNewBlogSubmission(blog) {
        this.setState({
            blogModalIsOpen: false,
            blogItems: [blog].concat(this.state.blogItems)
        });
    }


    // ...


    render() {
        // ...

        return (
            <div className='blog-container'>
                <BlogModal
                    /* ... */
                    handleSuccessfulNewBlogSubmission={this.handleSuccessfulNewBlogSubmission}
                />

                /* ... */
            </div>
        );
    }
}
```

<br/>

Hemos creado el `handler` que recibe el nuevo blog desde el formulario del modal, y lo hemos añadido al estado del componente, en la primera posición.
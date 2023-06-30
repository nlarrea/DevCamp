# Editar PortfolioItems

<div id='index'></div>

* [Crear el handler de editar](#crear-el-handler-de-editar)
* [Añadir el link de editar](#añadir-el-link-de-editar)
    * [Modificar el texto Edit](#modificar-el-texto-edit)
    * [Modificar el estilo de los iconos](#modificar-el-estilo-de-los-iconos)
* [Actualizar el formulario](#actualizar-el-formulario)
* [Actualizar los datos de la API](#actualizar-los-datos-de-la-api)
* [Actualizar el Sidebar](#actualizar-el-sidebar)
* [Actualizar los Dropzones](#actualizar-los-dropzones)
    * [Mostrar las imágenes](#mostrar-las-imágenes)
    * [Eliminar las imágenes](#eliminar-las-imágenes)

<br/>


[<< FONTAWESOME](./32_usar_fontawesome.md#fontawesome) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


Siguiendo las siglas **CRUD**, hemos realidazo ya las siguientes operaciones:

* **Create**: Crear un nuevo portfolio-item
* **Read**: Leer todos los portfolio-items
* **Delete**: Eliminar un portfolio-item

<br/>

Ahora vamos a realizar la operación **Update**, es decir, editar un portfolio-item.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Crear el handler de editar

Para poder editar los `PortfolioItems`, vamos a crear un nuevo handler en el componente `PortfolioManager` que se encargue de ello.

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    constructor(props) {
        // ...

        this.state = {
            // ...
            portfolioToEdit: {}
        };

        // ...
        this.handleEditClick = this.handleEditClick.bind(this);
    }

    handleEditClick(portfolioItem) {
        this.setState({
            portfolioToEdit: portfolioItem
        });
    }

    // ...

    render() {
        return (
            <div /* ... */>
                /* ... */

                <div className="right-column">
                    <PortfolioSidebarList
                        /* ... */
                        handleEditClick={this.handleEditClick}
                    />
                </div>
            </div>
        );
    }
}
```

<br/>

Por ahora, lo que hace el *handler* es editar una nueva propiedad que hemos añadido al estado, llamada `portfolioToEdit`, y le asigna el `portfolioItem` que le pasamos como argumento.

Ahora, pasaremos este *handler* como `prop` al componente `PortfolioSidebarList` para poder utilizarlo en dicho componente, y, al igual que con la opción de eliminar, añadiremos un nuevo link que nos permita editar el `portfolioItem` en cada uno de dichos ítems.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Añadir el link de editar

Para crear un link de editar para cada uno de los ítems, debemos acceder al componente `PortfolioSidebarList` y añadirlo de la siguiente manera:

```js
// portfolio-sidebar-list.js

// ...

const PortfolioSidebarList = (props) => {
    const portfolioList = props.data.map(portfolioItem => {
        return (
            <div /* ... */>
                /* ... */
                
                <div className="text-content">
                    /* ... */

                    <div className="actions">
                        <a className="action-icon" onClick={() => props.handleEditClick(portfolioItem)}>
                            Edit
                        </a>
                    
                        <a className='action-icon' onClick={() => props.handleDeleteClick(portfolioItem)}>
                            <FontAwesomeIcon icon='trash' />
                        </a>
                    </div>
                </div>
            </div>
        );
    });

    // ...
}

// ...
```

<br/>

Hemos creado un nuevo `div` con la clase `actions` para agrupar en él los links de editar y de eliminar los ítems del portfolio.

Hemos cambiado también la clase `delete-icon` por la clase `action-icon` para que ambos links tengan el mismo estilo (*más adelante modificaremos el estilo de dicha clase*).

Si accedemos a la aplicación ahora, veremos el texto `Edit` en cada uno de los ítems del portfolio, y, al hacer click en él, se actualizará la propiedad `portfolioToEdit` del estado de `PortfolioManager` ya que le hemos pasado como argumento al *handler* dicho `PortfolioItem`.


<br/><hr/><br/>


### Modificar el texto Edit

Ahora que ya tenemos el link de editar y que hemos aprendido a usar **FontAwesome**, vamos a sustituir el texto por un icono.

Lo primero que debemos hacer es escoger un icono e importarlo en `app.js`:

```js
// app.js

// ...
import { faTrash, faSignOutAlt, faEdit } from '@fortawesome/free-solid-svg-icons';

// ...

library.add(faTrash, faSignOutAlt, faEdit);

// ...
```

<br/>

Hecho esto, volveremos al archivo `portfolio-sidebar-list.js` y sustituiremos el texto `Edit` por el icono que acabamos de importar:

```js
// portfolio-sidebar-list.js

// ...

const PortfolioSidebarList = (props) => {
    const portfolioList = props.data.map(portfolioItem => {
        return (
            <div /* ... */>
                /* ... */
                
                <div className="text-content">
                    /* ... */

                    <div className="actions">
                        <a className="action-icon" onClick={() => props.handleEditClick(portfolioItem)}>
                            <FontAwesomeIcon icon='edit' />
                        </a>
                    
                        /* ... */
                    </div>
                </div>
            </div>
        );
    });

    // ...
}

// ...
```

<br/>

Ahora, veremos que tenemos el icono deseado en la aplicación.


<br/><hr/><br/>


### Modificar el estilo de los iconos

Hemos mencionado antes que se ha cambiado el nombre de la clase `delete-icon`, por lo que debemos modificar ciertos estilos para mantener el estilo del icono eliminar, y para que el nuevo icono también tenga el mismo estilo.

Para conseguirlo, realizaremos los siguientes cambios:

```scss
// _portfolio-sidebar.scss

// ...

.portfolio-sidebar-list-wrapper {
    // ...

    .text-content {
        // ...

        .actions {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;

            .action-icon {
                cursor: pointer;
                color: variables.$offwhite;
                font-size: 1.5em;
                transition: 0.5s ease-in-out;

                &:hover {
                    color: variables.$warning;
                }
            }
        }
    }
}
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Actualizar el formulario

Ahora que ya tenemos el `PortfolioItem` que queremos editar, debemos actualizar el formulario para que rellene con los datos de dicho `PortfolioItem` y nos permita editarlos.

Para ello, hay que crear una conexión entre el `PortfolioManager`, que es donde tenemos los datos del ítem a editar, y el `PortfolioForm`, que es donde tenemos el formulario.

En primer lugar, crearemos un método para devolver al valor inicial el `portfolioToEdit`, y pasaremos como `props` tanto el método como el `portfolioToEdit` al componente `PortfolioForm`:

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    constructor(props) {
        // ...
        
        this.clearPortfolioToEdit = this.clearPortfolioToEdit.bind(this);
    }

    clearPortfolioToEdit() {
        this.setState({
            portfolioToEdit: {}
        });
    }

    // ...

    render() {
        return (
            <div className='portfolio-manager-wrapper'>
                /* <div className="left-column">
                    <PortfolioForm
                        /* ... */
                        clearPortfolioToEdit={this.clearPortfolioToEdit}
                        portfolioToEdit={this.state.portfolioToEdit}
                    />
                </div> */

                /* ... */
            </div>
        );
    }
}
```

<br/>

Hecho esto, modificaremos el archivo `portfolio-form.js` para que, si existe un `portfolioToEdit`, rellene el formulario con los datos de dicho `PortfolioItem`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    componentDidUpdate() {
        if (Object.keys(this.props.portfolioToEdit).length > 0) {
            const { 
                id,
                name,
                description,
                category,
                position,
                url,
                thumb_image,
                banner_image,
                logo
             } = this.props.portfolioToEdit;

             this.props.clearPortfolioToEdit();

             this.setState({
                id,
                name: name || '',
                description: description || '',
                category: category || 'eCommerce',
                position: position || '',
                url: url || '',
             });
        }
    }

    // ...
}
```

<br/>

El método `componentDidUpdate()` se ejecuta cada vez que se actualiza algo en el formulario, por ello, introducimos una sentencia `if` para comprobar si se ha indicado que debe editarse o no un `PortfolioItem` (o simplemente se está rellenando el formulario para crear un ítem nuevo).

Lo que hace este código es que, si existe un `portfolioToEdit` (*es decir, se ha clicado en el icono de editar*), en primer lugar, almacena los valores en constantes haciendo uso de la propiedad de JS de deconstruir objetos, y se limpia el `portfolioToEdit` para que no siga entrando en el `if`.

Después, se actualiza el estado del formulario con los valores del `PortfolioItem` que se quiere editar. En caso de no tener algún valor asignado, se asigna un valor por defecto.

Como el estado se actualiza, los componentes del formulario actualizan sus valores, y, por tanto, se rellenan dichos campos con los valores del `PortfolioItem`.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Actualizar los datos de la API

Si clicamos en **editar** y después de modificar algún dato clicamos en el botón **Save**, veremos que en lugar de actualizar los datos del ítem, se crea uno nuevo.

Para evitar esto, debemos modificar el método `handleSubmit()` del componente `PortfolioForm` para que, en lugar de hacer un `POST` a la API, haga un `PATCH`. Además, habría que modificar el link de la API para que haga referencia al ítem que se quiere editar.

He aquí el código:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    constructor(props) {
        // ...

        this.state = {
            // ...
            /* axios config */
            editMode: false,
            apiUrl: 'https://nlarrea.devcamp.space/portfolio/portfolio_items',
            apiAction: 'post'
        }

        // ...
    }

    componentDidUpdate() {
        if (Object.keys(this.props.portfolioToEdit).length > 0) {
            // ...

            this.setState({
                // ...
                /* axios config */
                editMode: true,
                apiUrl: `https://nlarrea.devcamp.space/portfolio/portfolio_items/${id}`,
                apiAction: 'patch'
            });

            // ...
        }
    }

    // ...

    handleSubmit() {
        axios({
            method: this.state.apiAction,
            url: this.state.apiUrl,
            data: this.buildForm(),
            withCredentials: true
        }).then(/* ... */)
        .catch(/* ... */);

        // ...
    }

    // ...
}
```

<br/>

En primer lugar, se han añadido nuevas propiedades al estado:

* **editMode**: indica si se desea editar un ítem o no (*lo utilizaremos más adelante*).
* **apiUrl**: indica la URL de la API a la que se hará la petición.
* **apiAction**: indica el tipo de petición que se hará a la API.

<br/>

Los valores por defecto de dichas propiedades indican que se debe crear un nuevo ítem.

Por ello, en el método `componentDidUpdate()`, se ha añadido el código para actualizar dichas propiedades para indicar que sí se quiere editar el ítem, indicando la nueva url y el tipo de petición.

En el caso de la `apiUrl`, se ha añadido el `id` del `PortfolioItem` que se quiere editar de forma dinámica.

Por último, en el método `handleSubmit()`, se ha realizado la configuración necesaria para poder modificar el tipo de petición y la url de forma dinámica, y así poder hacer un `PATCH` en lugar de un `POST` sin tener que crear un nuevo *handler* repitiendo gran parte del código.


<br/><hr/>
<hr/><br>


## Actualizar el Sidebar

Por ahora, hemos conseguido actualizar la API con los datos editados en lugar de crear un nuevo ítem, pero en el `Sidebar` se crea uno nuevo, hasta que se recarga la página, que entonces vemos que se ha actualizado el ítem.

Para evitar que se añada un nuevo `PortfolioItem` cada vez que se edita uno, debemos modificar el método `handleSubmit()` del `portfolio-form.js`. En primer lugar, abriremos el archivo `portfolio-manager.js` para realizar las siguientes operaciones:

* Modificar el nombre del método `handleSuccessfulFormSubmission()` por `handleNewFormSubmission()`.
* Crear el método `handleEditFormSubmission()`.

```js
// portfolio-manager.js

// ...

export default class PortfolioManager extends Component {
    constructor(props) {
        // ...

        this.handleNewFormSubmission = this.handleNewFormSubmission.bind(this);
        this.handleEditFormSubmission = this.handleEditFormSubmission.bind(this);
        // ...
    }

    // ...

    handleEditFormSubmission() {
        this.getPortfolioItems();
    }

    handleNewFormSubmission(portfolioItem) {
        // this.setState({
        //     portfolioItems: [portfolioItem].concat(this.state.portfolioItems)
        // });
    }

    // ...

    render() {
        return (
            <div className='portfolio-manager-wrapper'>
                <div className="left-column">
                    <PortfolioForm
                        handleEditFormSubmission={this.handleEditFormSubmission}
                        handleNewFormSubmission={this.handleNewFormSubmission}
                        /* ... */
                    />
                </div>

                /* ... */
            </div>
        );
    }
}
```

<br/>

El nuevo método solo debe llamar al método `getPortfolioItems()` para que se actualice el estado del componente `PortfolioManager` y, por tanto, se actualice el `Sidebar`. El método que ya teníamos, añadía un nuevo ítem al estado, por lo que no queremos que se llame cuando se edita un `PortfolioItem`.

Ahora, vamos al componente hijo, `PortfolioForm`, para modificar el método `handleSubmit()`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    handleSubmit(event) {
        axios({/* ... */})
        .then(response => {
            // send data to the API
            if (this.state.editMode) {
                this.props.handleEditFormSubmission();
            } else {
                this.props.handleNewFormSubmission(response.data.portfolio_item);
            }

            // remove data from the form when submited
            this.setState({
                // ...,
                editMode: true,
                apiUrl: `https://nlarrea.devcamp.space/portfolio/portfolio_items/${id}`,
                apiAction: 'patch'
            });

            // ...
        }).catch(error => {
            console.log('portfolio form handleSubmit error', error);
        })

        // ...
    }

    // ...
}
```

<br/>

Si editamos algún récord que ya tuvieramos, veremos que ahora el `Sidebar` se actualiza en lugar de añadir un nuevo componente.


<br/><hr/>
<hr/><br/>


## Actualizar los Dropzones

### Mostrar las imágenes

Si editamos un ítem, veremos que el `Dropzone` no se actualiza, por lo que no se puede editar la imagen que se ha subido anteriormente.

Para solucionar esto, vamos a realizar los siguientes cambios en el componente `PortfolioForm`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    componentDidUpdate() {
        if (Object.keys(this.props.portfolioToEdit).length > 0) {
            const {
                // ...,
                thumb_image_url,
                banner_image_url,
                logo_url
            } = this.props.portfolioToEdit;

            // ...

            this.setState({
                // ...,
                thumb_image: thumb_image_url || '',
                banner_image: banner_image_url || '',
                logo: logo_url || ''
            });
        }
    }

    // ...

    render() {
        return (
            <form /* ... */>
                /* ... */

                <div className="image-uploaders">
                    {this.state.thumb_image && this.state.editMode ? (
                        <div className="portfolio-manager-image-wrapper">
                            <img src={this.state.thumb_image} />
                        </div>
                    ) : (
                        <DropzoneComponent
                            ref={this.thumbRef}
                            config={this.componentConfig()}
                            djsConfig={this.djsConfig()}
                            eventHandlers={this.handleThumbDrop()}
                        >
                            <div className='dz-message'>Thumbnail</div>
                        </DropzoneComponent>
                    )}

                    /* ... */
                </div>

                /* ... */
            </form>
        )
    }
}
```

<br/>

Por ahora, hemos modificado únicamente el `DropzoneComponent` del `thumb_image`, después modificaremos el resto de la misma manera.

Lo que se ha hecho es usar un ***operador ternario*** para, en caso de haber imagen y estar en el *modo de edición*, mostrar la imagen que se ha subido anteriormente, y en caso contrario, mostrar el `DropzoneComponent` para poder subir una nueva imagen.

Comprobamos si esto funciona y **repetimos el proceso para el resto de imágenes**.


<br/><hr/><br/>


### Editar el estilo

Si se ha comprobado el funcionamiento del código introducido en el apartado anterior, se habrá visto que las imágenes ocupan mucho espacio.

Vamos a modificar el estilo de las imágenes para que se vean más pequeñas y centradas en el lugar que ocupaban dichos `DropzoneComponent`:

```scss
// _portfolio-form.scss

// ...

.portfolio-form-wrapper {
    // ...

    .portfolio-manager-image-wrapper {
        img {
            width: 100%;
            height: 120px;
            object-fit: cover;
            border-radius: 5px;
        }
    }
}
```


<br/><hr/><br/>


### Eliminar imágenes

Vamos a realizar el proceso para, en caso de querer editar alguno de los ítems, poder eliminar las imágenes que se han subido anteriormente (*ya sea para subir una nueva o para no tener ninguna*).

Vamos a partir del archivo `portfolio-form.js`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    constructor(props) {
        // ...

        this.deleteImage = this.deleteImage.bind(this);

        // ...
    }

    deleteImage(imageType) {
        // por ahora, solo mostraremos qué imagen se quiere eliminar
        console.log('deleteImage', imageType);
    }

    // ...

    render() {
        return (
            <form onSubmit={this.handleSubmit} className='portfolio-form-wrapper'>
                /* ... */

                <div className="image-uploaders">
                    {this.state.thumb_image && this.state.editMode ? (
                        <div className="portfolio-manager-image-wrapper">
                            /* ... */

                            <div className="image-removal-link">
                                <a onClick={() => this.deleteImage('thumb_image')}>
                                    Remove File
                                </a>
                            </div>
                        </div>
                    ) : (
                        /* DropzoneComponent del thumb */
                    )}

                    {this.state.banner_image && this.state.editMode ? (
                        <div className="portfolio-manager-image-wrapper">
                            /* ... */

                            <div className="image-removal-link">
                                <a onClick={() => this.deleteImage('banner_image')}>
                                    Remove File
                                </a>
                            </div>
                        </div>
                    ) : (
                        /* DropzoneComponent del banner */
                    )}

                    {this.state.logo && this.state.editMode ? (
                        <div className="portfolio-manager-image-wrapper">
                            /* ... */

                            <div className="image-removal-link">
                                <a onClick={() => this.deleteImage('logo')}>
                                    Remove File
                                </a>
                            </div>
                        </div>
                    ) : (
                        /* DropzoneComponent del logo */
                    )}
                </div>

                /* ... */
            </form>
        );
    }
}
```

<br/>

Para comprobar que está funcionando, basta con ir al apartado de `Portfolio Manager` y editar alguno de los ítems, y ver que al pulsar en `Remove File` se muestra por consola el nombre de la imagen que se quiere eliminar.

Teniendo esto, vamos a abrir el archivo `portfolio-form.scss` y vamos a modificar el estilo de los enlaces que acabamos de añadir para alertar a los usuarios de que se van a eliminar las imágenes:

```scss
// _portfolio-form.scss

@use './variables' as var;
/* ... */

.portfolio-form-wrapper {
    /* ... */

    .portfolio-manager-image-wrapper {
        /* ... */

        .image-removal-link {
            display: flex;
            justify-content: center;

            a {
                cursor: pointer;
                color: var.$warning;
                font-weight: 700;
            }
        }
    }
}
```

<br/>

Llegados a este punto y antes de continuar, vamos a solucionar un pequeño progblema que se ha generado con las imágenes. Y es que si tratamos de editar un ítem que no tiene imágenes, y añadimos una, veremos que la imagen no se muestra correctamente.

Para solucionar esto, vamos a realizar las siguientes modificaciones en el archivo `portfolio-form.js`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    componentDidUpdate() {
        if (Object.keys(this.props.portfolioToEdit).length > 0) {
            // ...

             this.setState({
                // ...
                // modify the names
                thumb_image_url: thumb_image_url || '',
                banner_image_url: banner_image_url || '',
                logo_url: logo_url || ''
             });
        }
    }

    // ...

    render() {
        return (
            <form onSubmit={this.handleSubmit} className='portfolio-form-wrapper'>
                /* ... */

                <div className="image-uploaders">
                    {this.state.thumb_image_url && this.state.editMode ? (
                        /* ... */
                    ) : (
                        /* ... */
                    )}

                    {this.state.banner_image_url && this.state.editMode ? (
                        /* ... */
                    ) : (
                        /* ... */
                    )}

                    {this.state.logo_url && this.state.editMode ? (
                        /* ... */
                    ) : (
                        /* ... */
                    )}
                </div>

                /* ... */
            </form>
        )
    }
}
```

<br/>

Finalmente, vamos a modificar el método `deleteImage()` para que, en lugar de mostrar por consola el nombre de la imagen que se quiere eliminar, se elimine la propia imagen:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    deleteImage(imageType) {
        axios.delete(
            `https://api/.devcamp.space/portfolio/delete-portfolio-image/${this.state.id}?image_type=${imageType}`,
            { withCredentials: true }
        ).then(response => {
            this.setState({
                [`${imageType}_url`]: ''
            });
        }).catch(error => {
            console.log('deleteImage error', error);
        });
    }
}
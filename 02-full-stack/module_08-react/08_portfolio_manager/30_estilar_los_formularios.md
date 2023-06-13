# Dar estilo a los formularios

<div id='index'></div>

* [Inputs](#inputs)
* [Textarea](#textarea)
* [Selectores](#select)
* [Grid Styles](#grid-styles)
* [Botones](#botones)
* [Dropzones](#dropzones)
    * [Modificar estilos](#modificar-estilos)
    * [Modificar contenido](#modificar-contenido)

<br/>


[<< TERMINAR FUNCIONALIDAD DEL FORMULARIO](./29_terminar_funcionalidad_formulario.md#terminar-la-funcionalidad-del-formulario) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>

En este apartado vamos a dar estilo a los elementos de los dos formularios que existen en nuestra aplicación:

* Login
* PortfolioForm

<br/>

Como van a tratarse de elementos *iguales* con diferentes clases, en diferentes secciones, vamos a crear ***mixins*** para dar los estilos a los elementos.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Inputs

Los primeros elemenos que vamos a estilar son los propios inputs. Sin embargo, antes de comenzar, vamos a modificar el método `render()` del componente `PortfolioForm` para eliminar el `div` que envuelve todos los elementos y el `h1` que muestra el título del formulario.

El objetivo de hacer esto, es que únicamente se devuelva un elemento: el formulario (`form`) en cuestión con todos sus inputs dentro.

He aquí el método `render()`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    render() {
        return (
            <form onSubmit={this.handleSubmit} className='portfolio-form-wrapper'>
                <div>
                    <input
                        type="text"
                        name='name'
                        placeholder='Portfolio Item Name'
                        value={this.state.name}
                        onChange={this.handleChange}
                    />
                    
                    <input
                        type="text"
                        name='url'
                        placeholder='URL'
                        value={this.state.url}
                        onChange={this.handleChange}
                    />
                </div>
                
                <div>
                    <input
                        type="text"
                        name='position'
                        placeholder='Position'
                        value={this.state.position}
                        onChange={this.handleChange}
                    />
                    
                    <select
                        name='category'
                        value={this.state.category}
                        onChange={this.handleChange}
                    >
                        <option value="eCommerce">eCommerce</option>
                        <option value="Scheduling">Scheduling</option>
                        <option value="Enterprise">Enterprise</option>
                    </select>
                </div>

                <div>
                    <textarea
                        type="text"
                        name='description'
                        placeholder='Description'
                        value={this.state.description}
                        onChange={this.handleChange}
                    />
                </div>

                <div className="image-uploaders">
                    <DropzoneComponent
                        ref={this.thumbRef}
                        config={this.componentConfig()}
                        djsConfig={this.djsConfig()}
                        eventHandlers={this.handleThumbDrop()}
                    />

                    <DropzoneComponent
                        ref={this.bannerRef}
                        config={this.componentConfig()}
                        djsConfig={this.djsConfig()}
                        eventHandlers={this.handleBannerDrop()}
                    />

                    <DropzoneComponent
                        ref={this.logoRef}
                        config={this.componentConfig()}
                        djsConfig={this.djsConfig()}
                        eventHandlers={this.handleLogoDrop()}
                    />
                </div>

                <div>
                    <button type='submit'>Save</button>
                </div>
            </form>
        );
    }
}
```

<br/>

Como se puede observar, hemos añadido también un `className` al formulario para poder darle estilos.

Ahora, vamos a modificar el archivo `_mixins.scss` para añadir los estilos de los inputs:

```scss
// _mixins.scss

// ...

@mixin input-element {
    input {
        width: 100%;
        padding: 5px 0;
        margin-bottom: 21px;

        font-family: 'Titillium Web', sans-serif;
        font-size: 1.1em;
        
        border: 0px;
        border-bottom: 1px solid variables.$teal;
        background-color: transparent;
        color: variables.$charcoal;
        
        transition: all 0.5s ease-in-out;

        &:focus {
            outline: none;
            border-bottom: 1px solid variables.$dark-teal;
        }
    }
}
```

<br/>

Hemos creado un estilo bastante *limpio* donde nuestros inuts tendrán un borde inferior color `teal` y, al hacer `focus` en ellos, el borde inferior cambiará a un color más oscuro.

Hecho esto, debemos implementar dichos estilos en nuestros inputs, para eso, crearemos el archivo `_portfolio-form.scss`, y lo añadiremos al `main.scss`. A continuación, escribiremos lo siguiente en el nuevo archivo:

```scss
// _portfolio-form.scss

@use './mixins';

.portfolio-form-wrapper {
    display: grid;
    grid-template-columns: 1fr;
    padding: 42px;

    @include mixins.input-element();
}
```

<br/>

Si volvemos a la página de nuestra aplicación y vemos los inputs, veremos que ya tienen los estilos que hemos definido.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Textarea

Queremos que todos los `textarea` de la aplicación (en caso de añadir más, puesto que por ahora solo tenemos uno) sean iguales. Por ello, en este caso, **no vamos a usar ningún `mixin`**.

Crearemos un nuevo archivo llamado `_forms.scss` y lo añadiremos al `main.scss`. A continuación, escribiremos lo siguiente en el nuevo archivo:

```scss
// _forms.scss

textarea {
    height: 100px;
    padding: 10px;

    border: 1px solid variables.$teal;
    background-color: transparent;

    font-size: 1rem;
    
    outline: none;
}
```

<br/>

Si volvemos a la página de nuestra aplicación y vemos el `textarea`, veremos que ya tiene los estilos que hemos definido.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Select

En este caso, tampoco vamos a usar mixins, sin embargo, añadiremos una clase al `select` para poder darle estilos. Esto lo hacemos para poder personalizar mejor (dando más especificidad) los estilos de los `select` de la aplicación.

Iremos al archivo `portfolio-form.js` y añadiremos la clase `select-element` al `select`:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    render() {
        return (
            <form onSubmit={this.handleSubmit} className='portfolio-form-wrapper'>
                /* ... */
                
                <div>
                    /* ... */
                    
                    <select
                        /* ... */
                        className='select-element'
                    >
                        /* ... */
                    </select>
                </div>

                /* ... */
            </form>
        );
    }
}
```

<br/>

Después, en el archivo `_forms.scss`, añadiremos los estilos del `select`:

```scss
// _forms.scss

.select-element {
    width: 100%;

    border: 1px solid #ccc;
    border-radius: 3px;
    background-color: transparent;
    
    font-size: 0.8rem;
    
    overflow: hidden;
    outline: none;
}
```

<br/>

Si volvemos a la página de nuestra aplicación y vemos el `select`, veremos que ya tiene los estilos que hemos definido.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Grid Styles

El formulario sigue una distribución de filas y columnas. Para implementarla, lo más sencillo es utilizar un `display: grid`. Sin embargo, hay ocasiones en las que debe haber una cantidad de columnas, y en otras, otra.

Para solucionar esto, vamos a crear un archivo `_grid.scss` y lo añadiremos al `main.scss`. Después, vamos a crear en él tres clases con las que podremos definir la cantidad de columnas que queremos que tenga un elemento:

```scss
// _grid.scss

.one-column {
    display: grid;
    grid-template-columns: 1fr;
    gap: 21px;
}

.two-column {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 21px;
}

.three-column {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 21px;
}
```

<br/>

Ahora, daremos esos nombres de clase a los elementos que agrupen los inputs en base a la cantidad de columnas:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...
    
    render() {
        return (
            <form onSubmit={this.handleSubmit} className='portfolio-form-wrapper'>
                <div className='two-column'>
                    /* input (name) & input (url) */
                </div>
                
                <div className='two-column'>
                    /* input & select */
                </div>

                <div className='one-column'>
                    /* textarea */
                </div>

                <div className="image-uploaders three-column">
                    /* dropzones */
                </div>

                /* ... */
            </form>
        );
    }
}
```

<br/>

Hecho esto, veremos que el formulario luce bastante mejor, sin embargo debemos modificar un par de cosas aún.

En primer lugar, accederemos al archivo `_portfolio-form.scss` y añadiremos un `gap` a la clase `portfolio-form-wrapper`. Además, indicaremos que el margen inferior de los `input` sea `0`:

```scss
// _portfolio-form.scss

.portfolio-form-wrapper {
    display: grid;
    grid-template-columns: 1fr;
    gap: 21px;
    padding: 42px;

    @include mixins.input-element();

    input {
        margin-bottom: 0;
    }
}
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Botones

Modificar el estilo de los botones de `submit` va a ser una tarea muy sencilla: solo debemos añadir a dichos botones la clase `btn`, puesto que ya creamos los estilos de dicha clase en el archivo `_buttons.scss`.

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...
    
    render() {
        return (
            <form /* ... */>
                /* ... */

                <div>
                    <button type='submit' className='btn'>Save</button>
                </div>
            </form>
        );
    }
}
```

<br/>

Si miramos cómo se ve la página ahora, veremos que se ha aplicado dicho estilo al botón.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Dropzones

### Modificar estilos

Habíamos definido un `grid` de tres columnas para estos elemenos, sin embargo, vamos a modificarlo para que tengan el mismo alto que ancho.

En primer lugar, les eliminaremos la clase `three-column` del `div` que contiene estos componentes y le dejaremos la clase `image-uploaders`.

Como la clase `three-column` ya no se usa, la podemos eliminar del archivo `_grid.scss`.

A continuación, daremos estilo a la clase `image-uploaders` en el archivo `_portfolio-form.scss`:

```scss
// _portfolio-form.scss

// ...

.portfolio-form-wrapper {
    // ...

    .image-uploaders {
        display: grid;
        grid-template-columns: repeat(3, 200px);
        gap: 21px;
    }
}
```

<br/>

Hemos usado en varias ocasiones las dos líneas siguientes:

```scss
display: grid;
gap: 21px;
```

<br/>

Por lo que vamos a crear un `mixin` en el archivo `_mixins.scss` para no tener que repetirnos:

```scss
// _mixins.scss

// ...

@mixin base-grid {
    display: grid;
    gap: 21px;
}
```

<br/>

Ahora, modificaremos los estilos de la siguiente manera:

```scss
// _grid.scss

@use './mixins';

.one-column {
    @include mixins.base-grid();
    grid-template-columns: 1fr;
}

.two-column {
    @include mixins.base-grid();
    grid-template-columns: repeat(2, 1fr);
}
```

```scss
// _portfolio-form.scss

// ...

.portfolio-form-wrapper {
    // ...    

    .image-uploaders {
        @include mixins.base-grid();
        grid-template-columns: repeat(3, 200px);
    }
}
```


<br/><hr/><br/>


### Modificar contenido

Tenemos tres dropzones con el mismo texto, por lo que al usuario le es imposible saber en qué orden debe subir las imágenes. Para solucionar esto, vamos a modificar el contenido de cada uno de ellos.

En React se trabaja con componentes *principal*, y cada componente está formado por otros componentes *hijos*. En el caso del `DropzoneComponent`, si accedemos a él clicando en `inspeccionar` en el navegador, veremos que en su interior tiene un elemento `div` con la clase `dz-message`. Ese es el elemento que contiene el texto que se muestra por defecto en el dropzone, y el que vamos a modificar:

```js
// portfolio-form.js

// ...

export default class PortfolioForm extends Component {
    // ...

    render() {
        return (
            <form /* ... */>
                /* ... */

                <div /* ... */>
                    <DropzoneComponent /* ... */>
                        <div className='dz-message'>Thumbnail</div>
                    </DropzoneComponent>

                    <DropzoneComponent /* ... */>
                        <div className='dz-message'>Banner</div>
                    </DropzoneComponent>

                    <DropzoneComponent /* ... */>
                        <div className='dz-message'>Logo</div>
                    </DropzoneComponent>
                </div>

                /* ... */
            </form>
        );
    }
}
```

<br/>

Si miramos la página ahora, veremos que el texto de cada dropzone ha cambiado. Ahora tenemos tres dropzones con textos diferentes:

* Thumbnail
* Banner
* Logo
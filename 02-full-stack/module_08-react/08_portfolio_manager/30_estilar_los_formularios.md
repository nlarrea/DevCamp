# Dar estilo a los formularios

<div id='index'></div>

* [Inputs](#inputs)

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
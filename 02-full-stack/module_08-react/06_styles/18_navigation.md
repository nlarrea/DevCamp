# Navigation component

<div id="index"></div>

* [Estilos para los links de navegación](#estilos-para-los-links-de-navegación)
    * [Crear y usar variables para los colores](#crear-y-usar-variables-para-los-colores)
    * [Finalizar los estilos de los links de navegación](#finalizar-los-estilos-de-los-links-de-navegación)

<br/>

[<< USAR ESTILOS](./17_styles.md#usar-estilos-en-react) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


Tenemos un componente encargado de la navegación. Este va a ser el primer componente que vamos a estilar dentro de nuestra aplicación (portfolio).

En primer lugar, queremos que aparezcan los links en la parte superior izquierda de la pantalla, y nuestro nombre en la parte superior derecha.

Para ello, lo lógico es usar un contenedor **Flexbox**. En primer lugar, comenzaremos creando una clase para el componente `NavigationComponent`, que será el que contenga todos los ítems de navegación en su interior. Además, separaremos en dos clases diferentes los ítems de navegación, y nuestro nombre.

```jsx
// navigation-container.js

// ...

export default class NavigationComponent extends Component {
    // ...

    render() {
        return {
            <div className="nav-wrapper">
                <div className="left-side">
                    <NavLink exact to='/' activeClassName='nav-link-active'>Home</NavLink>
                    <NavLink to='/about-me' activeClassName='nav-link-active'>About</NavLink>
                    <NavLink to='/contact' activeClassName='nav-link-active'>Contact</NavLink>
                    <NavLink to='/blog' activeClassName='nav-link-active'>Blog</NavLink>
                    {false ? <button>Add Blog</button> : null}
                </div>

                <div className="right-side">
                    NAIA LARREA
                </div>
            </div>
        }
    }
}
```

<br/>

Una vez hecho esto, le añadiremos el estilo deseado:

```scss
// _navigation.scss

.nav-wrapper {
    display: flex;
    justify-content: space-between;
    padding: 30px;
}
```


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="index">Volver arriba</a>
</div>


## Estilos para los links de navegación

Ya tenemos la distribución del panel de navegación, ahora vamos a modificar los estilos de los links de navegación.

En primer lugar, vamos a crear insertar cada link dentro de una etiqueta `div` a la que pondremos la clase `nav-link-wrapper`. Esto nos permitirá modificar los estilos de todos los links de navegación a la vez.

```jsx
// navigation-container.js

// ...

export default class NavigationComponent extends Component {
    // ...

    render() {
        return {
            <div className="nav-wrapper">
                <div className="left-side">
                    <div className="nav-link-wrapper">
                        <NavLink exact to='/' activeClassName='nav-link-active'>Home</NavLink>
                    </div>

                    <div className="nav-link-wrapper">
                        <NavLink to='/about-me' activeClassName='nav-link-active'>About</NavLink>
                    </div>

                    <div className="nav-link-wrapper">
                        <NavLink to='/contact' activeClassName='nav-link-active'>Contact</NavLink>
                    </div>

                    <div className="nav-link-wrapper">
                        <NavLink to='/blog' activeClassName='nav-link-active'>Blog</NavLink>
                    </div>
                </div>

                <div className="right-side">
                    NAIA LARREA
                </div>
            </div>
        }
    }
}
```

<br/>

Ahora, procedemos a añaadir los estilos:

```scss
// _navigation.scss

.nav-wrapper {
    // ...

    .left-side {
        // para mantener los links en una sola línea
        display: flex;
    }

    .nav-link-wrapper {
        height: 22px;
        
        // para la animación al hacer hover
        border-bottom: 1px solid transparent;
        transition: 0.5s ease-in-out;

        a {
            color: black;
            text-decoration: none;
        }

        &:hover {
            border-bottom: 1px solid black;
        }
    }
}
```


<br/><hr/><br/>


### Crear y usar variables para los colores

Vamos a crear un nuevo archivo dentro del mismo directorio. Este archivo se llamará `_variables.scss`. En él, crearemos las variables que queramos usar en nuestro proyecto.

Por ahora, crearemos una serie de colores:

```scss
$teal: #26bfd4;
$dark-teal: #207b88;
$charcoal: #42454a;
$offwhite: #f6f6f6;
$blue: #008dff;
$warning: #922a2a;
$grey: #8a8a8a;
```

<br/>

Ahora, importaremos este archivo tanto en el archivo `main.scss` como en el archivo `_navigation.scss`, archivo en el que además usaremos una de estas variables ya:

```scss
// main.scss

@use "./variables";
@use "./base";
@use "./navigation";
```

```scss
// _navigation.scss

@use "./variables";

.nav-wrapper {
    // ...

    .left-side {
        // ...
    }

    .nav-link-wrapper {
        // ...

        a {
            color: variables.$grey; // cambio de color
            text-decoration: none;

            // añadimos el cambio de color al hacer hover
            &:hover {
                color: black;
            }
        }

        &:hover {
            border-bottom: 1px solid black;
        }
    }
}
```


<br/><hr/><br/>


### Finalizar los estilos de los links de navegación

Vamos a añadir un poco más de estilo a los links de navegación. Cuando creamos los componentes, les añadimos la clase `nav-link-active`, esta clase servirá para mantener un estilo en el link que esté activo.

Para ello, añadiremos lo siguiente:

```scss
// _navigation.scss

@use "./variables";

.nav-wrapper {
    // ...

    .nav-link-wrapper {
        // ...

        margin-right: 20px;
        text-transform: uppercase;
        font-size: 0.9rem;

        .nav-link-active {
            color: black;
            border-bottom: 1px solid black;
        }

        // ...
    }
}
```

<br/>

Lo que hemos hecho es:

* Añadir un margen en el lado derecho de nuestros links.
* Hacer que todos estén escritos en mayúsculas.
* Añadir un tamaño de fuente del 90% del tamaño de `root`.
* Cambiar el color a negro y añadir el borde inferior al link que esté activo.
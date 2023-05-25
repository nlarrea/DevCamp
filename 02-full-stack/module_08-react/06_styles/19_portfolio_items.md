# Homepage Portfolio Items

<div id="index"></div>

* [Modificar la estructura](#modificar-la-estructura)
    * [Añadir clases](#añadir-clases)
    * [Añadir estilos](#añadir-estilos)
* [Estilos Inline en React](#estilos-inline-en-react)
* [Poner elementos sobre las imágenes de fondo](#poner-elementos-sobre-las-imágenes-de-fondo)

<br/>

[<< NAVBAR](./18_navigation.md#navigation-component) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>

En este apartado vamos a trabajar con los `PortfolioItem` que se muestran en la página `HOME`.

Ahora mismo, estos componentes se posicionan uno debajo del otro, pero queremos que se muestren en forma de rejilla.


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Modificar la estructura

### Añadir clases

En primer lugar, vamos a necesitar añadir clases a los elementos para poder referirnos a ellos. Vamos a empezar modificando el componente `PortfolioContainer`:

```jsx
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    // ...

    render() {
        return (
            <div>
                /* ... */

                <div className="portfolio-items-wrapper">
                    {this.portfolioItems()}
                </div>
            </div>
        )
    }
}
```

<br/>

Ahora, vamos a modificar el componente `PortfolioItem`:

```jsx
// portfolio-item.js

// ...

export default function(props) {
    // ...
    
    return (
        <div className='portfolio-item-wrapper'>
            <img src={thumb_image_url} />
            <img src={logo_url} />
            <div>{description}</div>
            <Link to={`/portfolio/${id}`}>Link</Link>
        </div>
    )
}
```

<br/>

Aunque parece que hemos añadido la misma clase a ambos componentes, he de señalar que no es así:

* PortfolioContainer: `portfolio-items-wrapper`
* PortfolioItem: `portfolio-item-wrapper`

<br/>

Como `PortfolioItem` va dentro de `PortfolioContainer`, el primero lleva la clase en singular, y el componente *padre* la lleva en plural.


<br/><hr/><br/>


### Añadir estilos

Una vez hecho esto, vamos a modificar los estilos de estos componentes.

Vamos a crear otro archivo llamado `_portfolio.scss` dentro de la carpeta `styles`, y vamos a importarlo desde el `main.scss`:

```scss
// main.scss

@use "./variables";
@use "./base";
@use "./navigation";
@use "./portfolio";
```

```scss
// _portfolio.scss

.portfolio-items-wrapper {
    display: grid;
    grid-template-columns: repeat(3, 1fr);

    .portfolio-item-wrapper {
        position: relative;
    }
}
```


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Estilos Inline en React

Las imágenes de los `PortfolioItem` realmente son imágenes de fondo, lo que significa que debemos realizar ciertas modificaciones en el componente.

En primer lugar, eliminaremos la imagen `thumb_image_url`, puesto que debemos *enviarla* como imagen de fondo. Dado a que esta imagen es una obtenida de una API, no podemos *harcodear* en los estilos las imágenes, por lo que debemos hacerlo de forma dinámica, utilizando estilos **inline**.

Para ello, vamos a modificar el componente `PortfolioItem`:

```jsx
// portfolio-item.js

// ...

export default function(props) {
    // ...
    
    return (
        <div className='portfolio-item-wrapper'>
            <div
                className='portfolio-img-background'
                style={{
                    backgroundImage: `url(${thumb_image_url})`
                }}
            />

            <img src={logo_url} />
            <div>{description}</div>
            <Link to={`/portfolio/${id}`}>Link</Link>
        </div>
    )
}
```

<br/>

Lo que hemos hecho es añadir un `div` con la clase `portfolio-img-background`. Le hemos añadido estilos, que como se requiere de JS, se usan los `{}`. Dentro de estos estilos, estamos mandando un objeto, por lo que volveremos a usar `{}`.

La propiedad o *estilo* que se quiere modificar es `background-image`, pero como se trata de React, debemos usar `backgroundImage`, a quien le pasamos de forma dinámica la url de cada imagen de fondo.

Finalmente, volveremos al archivo `_portfolio.scss` para añadir los estilos de este nuevo elemento:

```scss
// _portfolio.scss

.portfolio-items-wrapper {
    // ...
    
    .portfolio-item-wrapper {
        // ...

        .portfolio-img-background {
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 350px;
            width: 100%;    // que ocupe todo el ancho del padre
        }
    }
}
```


<br/><hr/>
<hr/><br/>


<div align="right">
    <a href="#index">Volver arriba</a>
</div>


## Poner elementos sobre las imágenes de fondo

Ahora que tenemos las imágenes de fondo, vamos a poner encima de ellas el logo y la descripción.

Como hemos hecho anteriormente, lo primero será modificar el componente para añadir las clases necesarias y situar los elementos como nosotros deseemos:

```jsx
// portfolio-item.js

// ...

export default function(props) {
    // ...
    
    return (
        <div className='portfolio-item-wrapper'>
            <div
                className='portfolio-img-background'
                style={{
                    backgroundImage: `url(${thumb_image_url})`
                }}
            />

            <div className="img-text-wrapper">
                <div className="logo-wrapper">
                    <img src={logo_url} />
                </div>

                <div className="subtitle">{description}</div>
            </div>
        </div>
    )
}
```

<br/>

Ahora, vamos a modificar los estilos:

```scss
// _portfolio.scss

@use "./variables";

.portfolio-items-wrapper {
    // ...

    .portfolio-item-wrapper {
        // ...

        .img-text-wrapper {
            position: absolute;
            top: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100%;
            text-align: center;
            padding: 0 100px;
            
            .subtitle {
                // que no se vea hasta que se haga hover
                transition: 1s ease-in-out;
                color: transparent;
            }
        }

        .img-text-wrapper:hover .subtitle {
            color: variables.$teal;
            font-weight: 400;
        }

        .logo-wrapper img {
            width: 100%;    // ocupar el ancho del padre
            margin-bottom: 20px;
        }
    }
}
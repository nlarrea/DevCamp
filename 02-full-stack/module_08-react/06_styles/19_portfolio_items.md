# Homepage Portfolio Items

<div id="index"></div>

* [Modificar la estructura](#modificar-la-estructura)

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
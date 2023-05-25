# Mixins

[<< PORTFOLIO ITEMS](./19_portfolio_items.md#homepage-portfolio-items) | [HOME](../../../README.md#devcamp) | [AUTENTICACIÓN >>](../07_authentication/21_auth.md#auth-component)


<br/><hr/>
<hr/><br/>


En este apartado vamos a crear un estilo para los botones que estamos usando como *filtro* en la aplicación.

Vamos a crear un estilo de base que pueda ser aplicado a cualquier botón utilizando un **mixin**. Después, aplicaremos este estilo a los botones de filtro.

En primer lugar, añadiremos la clase `.btn` a los botones de filtro:

```jsx
// portfolio-container.js

// ...

export default class PortfolioContainer extends Component {
    // ...

    render() {
        // ...

        return (
            <div className="portfolio-items-wrapper">
                <button className='btn' onClick={() => this.handleFilter('eCommerce')}>eCommerce</button>
                <button className='btn' onClick={() => this.handleFilter('Scheduling')}>Scheduling</button>
                <button className='btn' onClick={() => this.handleFilter('Enterprise')}>Enterprise</button>
                
                /* ... */
            </div>
        )
    }
}
```

<br/>

Como se puede observar, hemos metido los botones dentro del `div` con la clase `.portfolio-items-wrapper`. Esto es porque los botones también van a seguir el estilo *grid* que hemos implementado en los elementos de esta clase.

Ahora, vamos a importar en el fichero `main.scss` los ficheros que vamos a crear:

* `_mixins.scss`
* `_button.scss`

<br/>

```scss
// main.scss

@use "./variables";
@use "./mixins";
@use "./base";
@use "./button";
@use "./navigation";
@use "./portfolio";
```

<br/>

En el fichero `_mixins.scss` vamos a crear el mixin que nos permitirá aplicar el estilo de base a los botones:

```scss
// _mixins.scss

@use "./variables";

@mixin base-btn {
    cursor: pointer;
    height: 42px;
    font-size: 1em;
    font-weight: 500;
    border: 1px solid transparent;
    transition: all 0.5s ease-in-out;
    background-color: variables.$teal;
    color: white;

    &:active, &:focus {
        outline: none;
    }

    &:hover {
        background-color: variables.$dark-teal;
    }
}
```

<br/>

Finalmente, vamos a aplicar dicho estilo a los botones:

```scss
// _button.scss

@use "./mixins";

.btn {
    @include mixins.base-btn();
}
```


<br/><hr/>
<hr/><br/>


[<< PORTFOLIO ITEMS](./19_portfolio_items.md#homepage-portfolio-items) | [HOME](../../../README.md#devcamp) | [AUTENTICACIÓN >>](../07_authentication/21_auth.md#auth-component)
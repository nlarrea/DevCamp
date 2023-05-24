# Navigation component

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
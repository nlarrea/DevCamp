# NavLink

En el apartado anterior se ha visto cómo crear rutas de navegación en React. En esta sección se va a hablar de cómo crear enlaces que nos permitan navegar entre las diferentes rutas. O, dicho de otra manera, cómo ligar dichas rutas a elementos de la interfaz de usuario para poder navegar a las *diferentes páginas* de nuestra aplicación.

<br/>

Para ello, vamos a acceder a nuestro archivo `navigation-container.js`, donde previamente teníamos los botones indicando las posibles diferentes páginas a visitar.

Por ahora, solo disponemos de los archivos `home.js` y `about.js`, por lo que vamos a crear dos enlaces que nos permitan navegar entre estas dos páginas:

```jsx
// navigation-container.js

// ...
import { NavLink } from 'react-router-dom';

export default class NavigationComponent extends Component {
    constructor() {
        super();
    }

    render() {
        return (
            <div>
                <NavLink exact to='/'>Home</NavLink>
                <NavLink to='/about-me'>About</NavLink>
                <!-- ... -->
            </div>
        );
    }
}
```

<br/>

Como se puede observar, se ha utilizado el componente `NavLink` para crear los enlaces. Este componente es similar a utilizar la etiqueta `a`. Sin embargo, si se usara dicha etiqueta, se perdería la funcionalidad de React, podría llevar a un comportamiento inesperado, y otros problemas, además de volver a cargar la página, lo cual ralentizaría su funcionamiento, por lo que no se recomienda.

Además de esto, haciendo uso de `NavLink`, se añade de forma automática la clase `active` a aquel link en el que el usuario ha clicado. Con esto, se puede utilizar la propiedad `activeClassName` para reescribir el nombre de la clase `active` por el que se desee, lo cual puede ser útil para aplicar estilos a dicho link.
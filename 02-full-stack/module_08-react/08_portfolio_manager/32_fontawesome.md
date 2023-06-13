# FontAwesome

<div id='index'></div>

* [Instalar FontAwesome](#instalar-fontawesome)
* [Importar los iconos](#importar-los-iconos)
* [Sustituir el texto por iconos](#sustituir-el-texto-por-iconos)
    * [Texto Delete](#texto-delete)
    * [Estilar el icono delete](#estilar-el-icono-delete)

<br/>


[<< ELIMINAR PORTFOLIO-ITEMS](./31_eliminar_portfolio_items.md#eliminar-portfolioitems) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>

Hemos utilizado un par de links a lo largo del proyecto a los que hemos añadido texto, sin embargo, vamos a modificarlos por iconos para hacer que la aplicación sea más atractiva.

Los iconos a usar van a ser de la librería [FontAwesome](https://fontawesome.com/), la cual vamos a instalar en el proyecto.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Instalar FontAwesome

Para instalar y utilizar FontAwesome en React, debemos utilizar tres librerías/componentes, por lo que este es el comando que debemos ejecutar:

```bash
npm i @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome
```

<br/>

Cuando se haya instalado todo, arrancaremos de nuevo el servidor para comprobar que funciona correctamente.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Importar los iconos

Una vez instaladas las dependencias necesarias, vamos a importar los iconos que queremos utilizar en el proyecto.

Para eso, accederemos al archivo `app.js` y añadiremos las siguientes líneas:

```js
// app.js

// ...
import { library } from '@fortawesome/fontawesome-svg-core';
import { FortAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash, faSignOutAlt } from '@fortawesome/free-solid-svg-icons';

// ...

library.add(faTrash, faSignOutAlt);
```

<br/>

Con esta líena:

```js
import { faTrash, faSignOutAlt } from '@fortawesome/free-solid-svg-icons';
```

<br/>

Hemos indicado qué iconos queremos importar, y con esta otra:

```js
library.add(faTrash, faSignOutAlt);
```

<br/>

Hemos añadido o conectado los iconos a la librería de FontAwesome.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Sustituir el texto por iconos

Ahora que ya tenemos los iconos importados, vamos a sustituir el texto de los links por dichos iconos.


<br/><hr/><br/>


### Texto Delete

Estos links se encuentran en el `sidebar` de la aplicación, dentro del archivo `portfolio-sidebar-list.js`.

Vamos a acceder a dicho archivo y a realizar los siguientes cambios:

```js
// portfolio-sidebar-list.js

// ...
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const PortfolioSidebarList = (props) => {
    const portfolioItems = props.data.map(portfolioItem => {
        return (
            <div /* ... */>
                /* ... */
                
                <a onClick={() => props.handleDeleteClick(portfolioItem)}>
                    <FontAwesomeIcon icon='trash' />
                </a>
            </div>
        );
    });
}
```

<br/>

Hemos importado el componente `FontAwesomeIcon` y lo hemos utilizado para mostrar el icono de la papelera (`trash`).


<br/><hr/><br/>


### Estilar el icono delete

Habiendo añadido ya el icono encargado de eliminar los ítems que queramos, vamos a darle ciertos estilos.

En primer lugar, vamos a modificar el archivo `portfolio-sidebar-list.scss` para eliminar el ID de aquí y mantener solo el título y el link de eliminar. Vamos, también, a añadirle una clase al link que contiene el icono:

```js
// portfolio-sidebar-list.scss

// ...

const PortfolioSidebarList = (props) => {
    const portfolioList = props.data.map(portfolioItem => {
        return (
            <div key={portfolioItem.id} className='portfolio-item-thumb'>
                <div className='portfolio-thumb-img'>
                    <img src={portfolioItem.thumb_image_url} />
                </div>
                
                <div className="text-content">
                    <div className='title'>{portfolioItem.name}</div>
                    
                    <a className='delete-icon' onClick={() => props.handleDeleteClick(portfolioItem)}>
                        <FontAwesomeIcon icon='trash' />
                    </a>
                </div>
            </div>
        )
    });

    // ...
}

// ...
```

<br/>

Hemos cambiado también el `h1` por un `div` para darle el tamaño que queramos y hemos agrupado en un solo `div` los *elementos de texto*. Ahora, modificamos el estilo:

```scss
// _portfolio-sidebar.scss

// ...

.portfolio-sidebar-list-wrapper {
    .portfolio-item-thumb {
        // ...

        // nueva clase: agrupa elementos de texto
        .text-content {
            display: flex;
            justify-content: space-between;
            align-items: center;

            // title movido dentro de text-content
            .title {
                color: variables.$offwhite;
                font-size: 1.5em;
            }

            .delete-icon {
                cursor: pointer;
                color: variables.$offwhite;
                font-size: 1.5em;
                transition: all 0.5s ease-in-out;

                &:hover, &:focus {
                    outline: none;
                    color: variables.$warning;
                }
            }
        }
    }
}
```
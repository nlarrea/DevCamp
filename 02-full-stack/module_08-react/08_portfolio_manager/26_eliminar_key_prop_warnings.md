# Eliminar Key prop Warnings

<div id='index'></div>

* [Componente App](#componente-app)
* [Componente PorfolioSidebarList](#componente-portfoliosidebarlist)

<br/>


[<< PORFOLIO MANAGER](./25_crear_el_componente.md#crear-el-portfolio-manager) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>

Si abrimos la consola del navegador, veremos que tenemos una lista de avisos que nos dicen que no estamos pasando la propiedad `key` a los componentes que estamos renderizando.

Esto se debe a que tenemos listas o agrupaciones de componentes que no tienen una propiedad `key` definida.

Si nos fijamos en las advertencias, se nos indica que dichos componentes se encuentran en:

* `App`
* `PortfolioSidebarList`


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Componente App

Dentro de este componente, tenemos varias rutas definidas, sin embargo, solo hay un lugar en el que exista una lista de componentes: el método `authorizedPages()`.

En este método, tenemos un `return` donde se devuelve una lista. Por ahora, dicha lista contiene un único componente, sin embargo, al tratarse de una lista, es suficiente para que React nos muestre el aviso.

Para solucionarlo, pondremos un `key` a dicho componente. Como no tenemos un identificador único para el mismo, y es el único que tenemos, podemos escribir lo que queramos:

```js
// app.js

// ...

export default class App extends Component {
    // ...

    authorizedPages() {
        return [
            <Route
                key='portfolio-manager'
                path='/portfolio-manager'
                component={PortfolioManager}
            />
        ]
    }

    // ...
}
```

<br/>

Si recargamos la página, veremos que el aviso referido al componente `App` ha desaparecido.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Componente PortfolioSidebarList

Dentro de este componente tenemos una función que se encarga de renderizar una lista de componentes recibidos mediante `props`.

Se utiliza la función `map()` para recorrer el array de componentes y devolver un nuevo array con los mismos. Por lo que sabemos que es aquí donde tenemos que añadir el `key`.

Estamos devolviendo varios elementos, sin embargo, el `key` debe ir en el elemento padre, por lo que lo añadiremos al `div` que contiene a todos los elementos (*el de la clase `portfolio-item-thumb`*):

```js
// portfolio-sidebar-list.js

// ...

const PortfolioSidebarList = (props) => {
    const portfolioList = props.data.map(portfolioItem => {
        return (
            <div key={portfolioItem.id} className='portfolio-item-thumb'>
                /* ... */
            </div>
        );
    });

    // ...
}

// ...
```

<br/>

Como se trata de los ítems del portfolio, cada uno de los ítems tiene su propio `id`, por lo que podemos utilizarlo como `key`.

Si recargamos la página, veremos que el aviso referido al componente `PortfolioSidebarList` ha desaparecido, y ya no tenemos más avisos en la consola.


<br/><hr/>
<hr/><br/>


[<< PORFOLIO MANAGER](./25_crear_el_componente.md#crear-el-portfolio-manager) | [HOME](../../../README.md#devcamp)
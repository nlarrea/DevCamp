# Crear el Blog

<div id="index"></div>

* [Cambiar el componente funcional a uno basado en clase](#)

<br/>


[<< EDITAR PORTFOLIO ITEMS](../08_portfolio_manager/33_editar_portfolio_items.md#editar-portfolioitems) | [HOME](../../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Cambiar el componente funcional a uno basado en clase

Al comienzo del proyecto ya fue creado el componente funcional `blog.js`. Lo que haremos a continuación, será convertirlo en un componente basado en clase. Para ello, accederemos a la ruta `src/components/pages/blog.js` y cambiaremos el código por el siguiente:

```js
// blog.js

import React, { Component } from 'react';
// ...

export default class Blog extends Component {
    construsctor() {
        super();
    }

    render() {
        return (
            /* ... */
        );
    }
}
```

<br/>

Mantendremos el código que teníamos dentro de `return()`, pero modificaremos el resto de líneas para conseguir modificar el componente de forma correcta.

Si arrancamos la aplicación, veremos que nada debería haberse visto modificado (*puesto que no hemos añadido ni modificado elementos dentro del componente*).
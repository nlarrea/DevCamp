# Key prop

Cuando se trabaja con listas en React, es necesario que cada elemento tenga una propiedad `key` que sea única. Esta propiedad es necesaria para que React pueda identificar cada elemento de la lista y así poder actualizarlo de forma eficiente.

<br/>

Si accedemos al código del archivo `portfolio-container.js`, podemos ver que tenemos lo siguiente:

```js
portfolioItems() {
    return this.state.data.map(item => {
        return <PortfolioItem title={item.name} url={item.url} slug={item.id} />;
    });
}
```

<br/>

En este caso, cada elemento de la lista es un componente `PortfolioItem`, sin embargo, no se ha especificado la propiedad `key` en cada uno de ellos. Esto puede resultar en un error en la consola del navegador, el cual nos indica que React no puede identificar de forma única cada elemento de la lista.

Para solucionarlo, podemos agregar la propiedad `key` a cada elemento de la lista, de la siguiente forma:

```js
portfolioItems() {
    return this.state.data.map(item => {
        return <PortfolioItem key={item.id} title={item.name} url={item.url} slug={item.id} />;
    });
}
```
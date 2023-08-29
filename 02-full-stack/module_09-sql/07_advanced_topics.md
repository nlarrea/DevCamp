# Conceptos Avanzados

* [Índices](#índices)
    * [Ver los índices de una tabla](#ver-los-índices-de-una-tabla)
    * [Crear un nuevo índice](#crear-un-nuevo-índice)

* [Técnicas de normalización de bases de datos](#técnicas-de-normalización-de-bases-de-datos)

<br/>

[<< CONSULTAS RELACIONALES](./06_relational_queries.md#consultas-relacionales) | [HOME](../../README.md#devcamp)

<hr/><hr/><br/>

## Índices

Los índices son una herramienta que facilitan mucho la búsqueda de ciertas consultas. Hacen que estas consultas sean más rápidas y eficaces.

Por ejemplo, si se quiere encontrar un ítem concreto entre 5 millones de ítems sin usar índices, SQL irá ítem a ítem hasta encontrar el que se le ha indicado. Si se usaran índices, sabiendo que el ítem que se está buscando se encuentra en el índice `317` (*por ejemplo*), podemos acceder a él directamente, ahorrando mucho tiempo.

<br/>

<hr/><br/>

### Ver los índices de una tabla

Sin darnos cuenta, MySQL ya ha creado varios índices a lo largo del curso. Para poder ver qué índices tenemos haremos lo siguiente:

![index_01](./images/indexes/index_01.jpg)

1. **(Rojo):** Clicaremos en el botón de *información* de cualquiera de las tablas de nuestra base de datos, donde se abrirá un panel mostrando información de la misma.
2. **(Verde):** Seleccionaremos la pestaña de índices.
3. **(Morado):** Podremos ver qué índices tenemos creados ya en esa tabla.

<br/>

<hr/><br/>

### Crear un nuevo índice

Para crear más índices, desde el mismo panel mostrado [en el apartado anterior](#ver-los-índices-de-una-tabla), vamos a seguir estos pasos:

![index_02](./images/indexes/index_02.jpg)

1. **(Rojo):** Seleccionamos la columna en la cual queremos crear un índice.
2. **(Verde):** Clicamos el botón inferior derecho que dice `Create Index for Selected Columns...`.
3. **(Morado):** Se habrá abierto una ventana, donde podemos modificar una serie de características. Por ahora, dejamos los valores por defecto y clicamos en `Create`.

<br/>

Veremos que se ha creado el nuevo índice:

![index_03](./images/indexes/index_03.jpg)

<br/>

<hr/><hr/><br/>

## Técnicas de normalización de bases de datos

La normalización de bases de datos es esencialmente un conjunto de buenas prácticas y guías que nos permite construir y modelar una base de datos eficazmente.

He aquí una pequeña lista de buenas prácticas a seguir a la hora de crear una base de datos:

* **Cada tabla debe tener un único roll.** Es decir, es buena práctica tener una tabla `users` y otra `addresses`, y después relacionar ambas, pero no una tabla `x` donde se registren tanto usuarios como direcciones del mismo.
* **Utilizar el tipo de dato correcto para cada columna.** Puede resultar más fácil guardar *strings*, pero en ocasiones deberían utilizarse otro tipo de datos. Hay que ser inteligente y utilizar el tipo de dato que mejor se ajusta a las necesidades de cada variable.
* **Definir correctamente las características de cada columna.** Existen datos que deberían ser únicos (por ejemplo). Debemos asegurarnos de dar esa característica a ese tipo de columnas.
* **Utilizar siempre el mismo formato a la hora de nombrar las columnas.** No usar en algunas ***camelCase*** y en otras ***snake_case***, etc.
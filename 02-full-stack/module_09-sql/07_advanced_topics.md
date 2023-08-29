# Conceptos Avanzados

<div id='index'></div>

* [Índices](#índices)
    * [Ver los índices de una tabla](#ver-los-índices-de-una-tabla)
    * [Crear un nuevo índice](#crear-un-nuevo-índice)

* [Técnicas de normalización de bases de datos](#técnicas-de-normalización-de-bases-de-datos)
* [Modelizado de diagramas](#modelizado-de-diagramas)
    * [Crear un diagrama EER](#crear-un-diagrama-eer)
    * [Diagrama creado](#diagrama-creado)


<br/>

[<< CONSULTAS RELACIONALES](./06_relational_queries.md#consultas-relacionales) | [HOME](../../README.md#devcamp)

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

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

<div align='right'><a href='#index'>Volver arriba</a></div>

## Técnicas de normalización de bases de datos

La normalización de bases de datos es esencialmente un conjunto de buenas prácticas y guías que nos permite construir y modelar una base de datos eficazmente.

He aquí una pequeña lista de buenas prácticas a seguir a la hora de crear una base de datos:

* **Cada tabla debe tener un único roll.** Es decir, es buena práctica tener una tabla `users` y otra `addresses`, y después relacionar ambas, pero no una tabla `x` donde se registren tanto usuarios como direcciones del mismo.
* **Utilizar el tipo de dato correcto para cada columna.** Puede resultar más fácil guardar *strings*, pero en ocasiones deberían utilizarse otro tipo de datos. Hay que ser inteligente y utilizar el tipo de dato que mejor se ajusta a las necesidades de cada variable.
* **Definir correctamente las características de cada columna.** Existen datos que deberían ser únicos (por ejemplo). Debemos asegurarnos de dar esa característica a ese tipo de columnas.
* **Utilizar siempre el mismo formato a la hora de nombrar las columnas.** No usar en algunas ***camelCase*** y en otras ***snake_case***, etc.

<br/>

<hr/><hr/><br/>

## Modelizado de diagramas

Haciendo uso del MySQL Workbench se puede ver de forma visual la relación entre las diferentes tablas de la base de datos.

<br/>

<hr/><br/>

### Crear un diagrama EER

Crearemos diagramas EER siguiendo estos pasos:

![diagrams_01](./images/diagrams/diagrams_01.jpg)

> 1. Pulsamos `ctrl + R` para abrir el panel.
> 2. Seleccionamos la base de datos cuyo diagrama queremos.
> 3. Pulsamos `Next`.

<br/>

![diagrams_02](./images/diagrams/diagrams_02.jpg)

> Esperamos a que termine el proceso y clicamos en `Next`.

<br/>

![diagrams_03](./images/diagrams/diagrams_03.jpg)

> Seleccionamos la base de datos y clicamos en `Next`.

<br/>

![diagrams_04](./images/diagrams/diagrams_04.jpg)

> Esperamos a que termine el proceso y clicamos en `Next`.

<br/>

![diagrams_05](./images/diagrams/diagrams_05.jpg)

> Clicamos en `Execute >` y esperamos.

<br/>

![diagrams_06](./images/diagrams/diagrams_06.jpg)

> Se cambiará la pantalla de fondo. Cuando termine el proceso, clicamos en `Next`.

<br/>

![diagrams_07](./images/diagrams/diagrams_07.jpg)

> Para terminar, clicamos en `Finish`.

<br/>

<hr/><br/>

### Diagrama creado

Después de seguir todos estos pasos, veremos lo siguiente:

![diagrams_08](./images/diagrams/diagrams_08.jpg)

<br/>

Ahora tenemos una visualización de nuestras tablas de la base de datos. Podemos consultar de forma visual y rápida muchos aspectos y características de estas tablas:

* Podemos ver cómo están relacionadas entre sí con tan solo pasar el ratón sobre las *líneas* que las unen:

![diagrams_09](./images/diagrams/diagrams_09.jpg)

* Podemos ver cuáles son sus índices abriendo el selector `Indexes` que tienen en la parte de abajo:

![diagrams_10](./images/diagrams/diagrams_10.jpg)

* Podemos gestionar y manejar todos los aspectos de la base de datos desde aquí. Sin embargo, en este curso se opta por hacerlo mediante comandos, por lo que no se verá cómo hacerlo, simplemente, comentar que existe la opción.
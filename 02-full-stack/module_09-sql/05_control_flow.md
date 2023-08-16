# Control Flow

<div id='index'></div>

* [Aliases](#aliases)
    * [Alias en tablas](#alias-en-tablas)
* [Crear condiciones con CASE](#crear-condiciones-con-case)

<br/>

[<< FUNCIONES](./04_functions.md#funciones) | [HOME](../../..README.md#devcamp) |

<br/>

<hr/><hr/><br/>

En esta sección vamos a hablar de los controles de flujo. Si ya conoces otro(s) lenguaje(s) de programación, segurísimo que ya has hecho uso de los controles de flujo con anterioridad. Por ello, a partir de este punto vamos a ver cómo podemos hacer uso de sentencias como `if - else` en SQL.

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Aliases

Siguiendo con ejemplos utilizados en apartados anteriores donde queremos presentar los datos de una tabla a alguien, tenemos que los datos se muestran con encabezados que siguen este patrón: `tableName_columnName`. Esto puede ser difícil de leer o no muy *profesional*.

Para hacer que nuestras columnas se vean mejor, podemos crear **aliases** para las mismas haciendo uso de `AS`:

```sql
SELECT
addresses_street_one AS 'Street',
addresses_street_two AS 'Street 2',
addresses_city AS 'City',
addresses_state AS 'State',
addresses_postal_code AS 'Postal Code'
FROM addresses;
```

> Pueden no usarse las `''` para un alias. Sin embargo, éste no podrá tener ningún espacio.
>
> Para que se reconozca mejor cuál es el alias, se ha decidido usar las comillas siempre, aunque no sea necesario hacerlo.

<br/>

De esta forma, a la hora de mostrar o exportar los datos, se obtendría lo siguiente:

| Street         | Street 2 | City      | State | Postal Code |
| -------------- | -------- | --------- | ----- | ----------- |
| 123 Any Street |          | Manhattan | NY    | 53853       |
| ...            | ...      | ...       | ...   | ...         |

<br/>

<hr/><br/>

### Alias en tablas

Además de poder usar aliases en los nombres de las columnas, podemos usarlos también para hacer referencia a las tablas:

```sql
-- Sin alias
SELECT guides_title, guides_revenue
FROM guides
WHERE guides_revenue > 600;

-- Con alias
SELECT g.guides_title, g.guides_revenue
FROM guides g
WHERE g.guides_revenue > 600;
```

​	<br/>

Puede no parecer algo útil ahora mismo, sin embargo, a la hora de obtener datos de varias tablas, esto puede resultar de lo más práctico.

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Crear condicionales con CASE

En esta ocasión, vamos a ver cómo realizar condiciones haciendo uso de `CASE`. Esta palabra reservada (*acompañada de otras*) puede funcionar de la misma manera que una sentencia `if-else`.

Partiendo de la siguiente tabla `guides` (*mostrando únicamente las columnas `guides_title` y `guides_revenue`*):

| `guides_title`          | `guides_revenue` |
| ----------------------- | ---------------- |
| My Blog                 | 500              |
| Something Else          | 1500             |
| My Great Post           | 750              |
| My Blog                 | 1000             |
| My Blog                 | 750              |
| Another One of My Posts | 5000             |
| Guide by Jon            | 500              |

<br/>

Si quisiéramos generar un informe donde se mostrara simplemente un mensaje en función de la cantidad en `guides_revenue`, debería usarse un condicional. Para ello, haremos lo siguiente:

```sql
SELECT
guides_title,
CASE
    WHEN guides_revenue > 1000 THEN 'Best Seller'
    WHEN guides_revenue < 600 THEN 'Not Displayed'
    ELSE 'Average Sellers'
END AS 'status'
FROM guides;
```

<br/>

Vamos a explicar poco a poco qué es lo que hacemos con dichas líneas de código:

Las primeras dos líneas ya son conocidas: estamos seleccionando la columna `guides_title`.

Como se añade una coma (`,`) detrás del nombre de la columna (*antes del `FROM table_name`*), estamos indicando que vamos a seleccionar o crear otra columna. En este caso, se trata de un condicional:

* Si la columna `guides_revenue` tiene un valor mayor que 1000, se mostrará el mensaje `'Best Seller'` al lado del `guides_title` correspondiente.
* Si la columna `guides_revenue` tiene un valor menor que 600, se mostrará el mensaje `'Not Displayed'` al lado del `guides_title` correspondiente.
* En el resto de casos, se mostrará el mensaje `'Average Sellers'`.

>  Esta nueva columna tendrá como nombre `status`, gracias al `AS 'status'` añadido después del `END`. Si no se hubiera escrito dicho alias, se mostrarían todas las líneas desde el `CASE` hasta el `END` en la cabecera del resultado.

<br/>

Este es el resultado obtenido:

| `guides_title`          | `status`        |
| ----------------------- | --------------- |
| My Blog                 | Not Displayed   |
| Something Else          | Best Seller     |
| My Great Post           | Average Sellers |
| My Blog                 | Average Sellers |
| My Blog                 | Average Sellers |
| Another One of My Posts | Best Seller     |
| Guide by Jon            | Not Displayed   |

<br/>

En otros lenguajes de programación, la sentencia `CASE` tiene como equivalente un `if`. He aquí el mismo ejemplo escrito con **JavaScript** y **Python** para que quede más claro (*no de forma funcional, solo para entender qué se pretende hacer*):

```javascript
// JavaScript

if (guides_revenue > 1000) {
    'Best Seller';
} else if (guides_revenue < 600) {
    'Not Displayed';
} else {
    'Average Sellers';
}
```

```python
# Python

if guides_revenue > 1000:
    "Best Seller"
elif guides_revenue < 600:
    "Not Displayed"
else:
    "Average Sellers"
```


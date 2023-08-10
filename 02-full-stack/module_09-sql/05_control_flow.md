# Control Flow

<div id='index'></div>

* [Aliases](#aliases)
    * [Alias en tablas](#alias-en-tablas)

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
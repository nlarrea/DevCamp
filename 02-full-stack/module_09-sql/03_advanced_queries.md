# Consultas avanzadas

<div id='index'></div>

*   [Rangos](#rangos)
*   [Wildcard Search](#wildcard-search)
*   [Código más limpio al usar WHERE con IN](#código-más-limpio-al-usar-where-con-in)

<br/>

[<< CONSULTAS BÁSICAS](./02_basic_queries.md#sql-queries) | [HOME](../../../README.md#devcamp)

<br/><hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Rangos

Para utilizar rangos podemos utilizar componentes como `BETWEEN`, que tomará dos valores y mostrará los datos que se encuentren dentro o fuera de ese rango:

```sql
USE devcamp_sql_course_schema;

-- select items inside a given range
SELECT * FROM guides
WHERE guides_revenue BETWEEN 1000 AND 5000;

-- select items outside a given range
SELECT * FROM guides
WHERE guides_revenue NOT BETWEEN 1000 and 5000;
```

<br/><hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Wildcard Search

En ocasiones, desearemos realizar una búsqueda dentro de una cadena de texto para, por ejemplo, encontrar los elementos que contengan una palabra concreta dentro de una columna.

Para ello, podemos hacer uso de las **wildcard searches**, que consisten en utilizar los `%` como limitantes de la cadena de texto que queremos encontrar.

Por ejemplo, teniendo la siguiente base de datos:

| guides_id | guides_revenue | guides_users_id | guides_title            |
| --------- | -------------- | --------------- | ----------------------- |
| 1         | 500            | 1               | My Blog                 |
| 2         | 1500           | 2               | Something Else          |
| 3         | 750            | 2               | My Great Post!          |
| 4         | 1000           | 1               | My Blog                 |
| 5         | 750            | 2               | My Blog                 |
| 6         | 5000           | 1               | Another One of My Posts |

<br/>

Si quisiéramos obtener todos aquellas guías cuyo título contenga la palabra `My`, deberíamos hacer lo siguiente:

```sql
SELECT * FROM guides
WHERE guides_title LIKE '%My%';
```

<br/>

Este código nos mostraría todas las filas exceptuando la del `guides_title` con valor `Something Else` porque ésta no contiene la palabra `My`.

Si quisiéramos aquellas filas cuyo valor de `guides_title` **empezaran** por la palabra `My`, haríamos lo siguiente:

```sql
SELECT * FROM guides
WHERE guides_title LIKE 'My%';
```

<br/>

En este caso, se mostrarían todas las filas menos la segunda y la última en la tabla.

<br/><hr/><hr/><br/>

## Código más limpio al usar WHERE con IN

Para realizar consultas con ciertos filtros, podemos realizar lo siguinete:

```sql
SELECT * FROM addresses
WHERE addresses_city = 'Queens'
OR addresses_city = 'Manhattan';
```

<br/>

Esto es muy útil, sin embargo, ¿qué ocurriría si tuviéramos cientos de filtros a realizar? Este código podría ser muy tedioso.

Si vamos a comprobar siempre la misma columna, el código puede verse reducido significativamente si lo hacemos de la siguiente manera:

```sql
SELECT * FROM addresses
WHERE addresses_city IN ('Queens', 'Manhattan');
```

<br/>

Con esto, creamos una lista de posibles valores y usamos la palabra reservada `IN` para indicar que queremos las consultas cuya columna `addresses_city` tenga alguno de los valores de la lista.
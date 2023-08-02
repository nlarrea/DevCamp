# Consultas avanzadas

<div id='index'></div>

*   [Rangos](#rangos)
*   [Wildcard Search](#wildcard-search)
*   [Código más limpio al usar WHERE con IN](#código-más-limpio-al-usar-where-con-in)
*   [Subconsultas](#subconsultas)
    *   [Ejemplos adicionales de subconsultas](#ejemplos-adicionales-de-subconsultas)
    *   [Usar subconsultas para insertar datos](#usar-subconsultas-para-insertar-datos)

<br/>

[<< CONSULTAS BÁSICAS](./02_basic_queries.md#sql-queries) | [HOME](../../../README.md#devcamp) | [FUNCIONES >>](./04_functions.md#funciones)

<br/>

<hr/><hr/><br/>

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

<br/>

<hr/><hr/><br/>

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

<br/>

<hr/><hr/><br/>

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

<br/>

<hr/><hr/><br/>

## Subconsultas

En ocasiones querremos obtener datos de una fila concreta pero no tendremos forma de saber los valores de dicha fila como para poder realizar el filtro para obtener los datos deseados. En estas ocasiones, podremos realizar **subconsultas**.

Como ejemplo, utilizando la misma tabla que en el apartado de [Wildcard search](#wildcard-search), también mostrada a continuación:

| guides_id | guides_revenue | guides_users_id | guides_title            |
| --------- | -------------- | --------------- | ----------------------- |
| 1         | 500            | 1               | My Blog                 |
| 2         | 1500           | 2               | Something Else          |
| 3         | 750            | 2               | My Great Post!          |
| 4         | 1000           | 1               | My Blog                 |
| 5         | 750            | 2               | My Blog                 |
| 6         | 5000           | 1               | Another One of My Posts |

<br/>

Si quisiéramos obtener el `guides_title` y `guides_revenue` de la tabla cuyo `guides_revenue` tuviera el valor más alto de todos, haríamos algo asi:

```sql
SELECT guides_title, guides_revenue FROM guides
WHERE guides_revenue = 5000
```

<br/>

Pero, ***¿qué pasaría si no supieramos el valor más alto de `guides_revenue`?*** En primer lugar tendríamos que realizar una consulta para obtener el mayor valor de dicha columna, y entonces, obtener los valores deseados realizando el filtro de la columna con el valor obtenido. ***¿Y cómo se hace eso?*** Aquí es donde entran en juego las subconsultas:

```sql
SELECT guides_title, guides_revenue FROM guides
-- realizar el filtro
WHERE guides_revenue = (
  	-- seleccionar el valor más alto de guides_revenue
	SELECT MAX(CAST(guides_revenue AS UNSIGNED)) FROM guides
);
```

<br/>

<hr/><br/>

### Ejemplos adicionales de subconsultas

Partiendo de la siguiente tabla de datos:

| addresses_id | addresses_street_one | addresses_street_two | addresses_city | addresses_state | addresses_postal_code | addresses_users_id |
| ------------ | -------------------- | -------------------- | -------------- | --------------- | --------------------- | ------------------ |
| 1            | 123 Any Street       |                      | Manhattan      | NY              | 53853                 | 1                  |
| 2            | 123 Any Street       | Suite 333            | Phoenix        | AZ              | 84632                 | 1                  |
| 3            | 123 Any Street       |                      | Manhattan      | NY              | 53853                 | 2                  |
| 4            | 123 Any Street       |                      | Queens         | NY              | 53853                 | 3                  |

<br/>

Si quisiéramos obtener la información de aquellas filas cuya `addresses_city` fuera `'Queens'` o `'Manhattan'`, hemos visto en apartados anteriores que podría hacerse algo así:

```sql
SELECT * FROM addresses
WHERE addresses_city IN ('Queens', 'Manhattan');
```

<br/>

Sin embargo, si en lugar de obtener los datos coincidentes con esos dos valores, tomáramos aquellos que pertenezcan al `addresses_state` de `'NY'` y añadiéramos algún otro filtro, nos convendría más hacer uso de las subconsultas:

```sql
SELECT * FROM addresses
WHERE addresses_city IN (
	SELECT addresses_city FROM addresses
  	WHERE addresses_state = 'NY'
  	AND addresses_users_id = 1
);
```

<br/>

<hr/><br/>

### Usar subconsultas para insertar datos

Imaginemos que tenemos la siguiente tabla llamada `guides`:

| guides_id | guides_revenue | guides_users_id | guides_title            |
| --------- | -------------- | --------------- | ----------------------- |
| 1         | 500            | 2               | My Blog                 |
| 2         | 1500           | 3               | Something Else          |
| 3         | 750            | 3               | My Great Post           |
| 4         | 1000           | 2               | My Blog                 |
| 5         | 750            | 3               | My Blog                 |
| 6         | 5000           | 2               | Another One of My Posts |

<br/>

Si queremos crear un usuario y añadir, además, un *guide* para este nuevo usuario, habría que seguir los siguientes pasos:

1. Crear el nuevo usuario.
2. Crear un nuevo *guide*, para lo que es necesario obtener el ID del usuario.

<br/>

***Pero, ¿cómo podemos indicar cuál es el ID de ese nuevo usuario?***

Para ello, hay que realizar una subconsulta. He aquí la solución:

```sql
USE devcamp_sql_course_schema;

-- Creamos el nuevo usuario
INSERT INTO users (users_name, users_email)
VALUES ('Jon', 'jon@snow.com');

-- Creamos el nuevo 'guide'
INSERT INTO guides (guides_revenue, guides_title, guides_users_id)
VALUES (
	500,
    'Guide by Jon',
    -- Usamos una subconsulta para obtener el ID
    (SELECT users_id FROM users WHERE users_name = 'Jon' AND users_email = 'jon@snow.com' LIMIT 1)
);
```

<br/>

> Con el `LIMIT 1` nos aseguramos de que solo obtenemos un `users_id`, aunque no sería necesario en este caso puesto que el dato `users_email` está definido como `UNIQUE`.

Como no conocemos el `users_id` del nuevo usuario, debemos realizar una subconsulta para obtener ese dato. Si ahora hacemos una consulta de todos los elementos de la tabla `guides`, veremos la misma tabla que al principio pero con una fila más, que se corresponde con la que acabamos de crear.

<br/>

<hr/><hr/><br/>

[<< CONSULTAS BÁSICAS](./02_basic_queries.md#sql-queries) | [HOME](../../..README.md#devcamp) | [FUNCIONES >>](./04_functions.md#funciones)

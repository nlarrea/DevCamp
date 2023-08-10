# Funciones

<div id='index'></div>

* [Introducción a las funciones](#introducción-a-las-funciones)
* [Cambiar el tipo de dato de String a Decimal](#cambiar-el-tipo-de-dato-de-string-a-decimal)
* [Las funciones MIN, MAX, SUM, AVG y COUNT](#las-funciones-min,-max,-sum,-avg-y-count)
* [Generar informes resumidos con GROUP BY](#generar-informes-resumidos-con-group-by)
* [Utilizar comentarios](#utilizar-comentarios)
* [Deshabilitar temporalmente el Modo Seguro](#deshabilitar-temporalmente-el-modo-seguro)
* [Añadir una columna y llenarla con datos aleatorios](#añadir-una-columna-y-llenarla-con-datos-aleatorios)
* [Usar operadores matemáticos para obtener datos](#usar-operadores-matemáticos-para-obtener-datos)
* [Añadir nombres customizados a las columnas](#añadir-nombres-customizados-a-las-columnas)

<br/>

[<< CONSULTAS AVANZADAS](./03_advanced_queries.md#consultas-avanzadas) | [HOME](../../..README.md#devcamp) | [CONTROL FLOW >>](./05_control_flow.md#control-flow)

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Introducción a las funciones

En SQL es muy típico utilizar funciones para obtener cierta información de nuestras tablas. Con los ejemplos que hemos ido trabajando a lo largo de las secciones anteriores, podríamos crear una función que tomara todos los datos de `guides_revenue` y nos devolviera el total de dicha columna, por ejemplo.

A ese tipo de funciones se les llama ***aggregate functions***, que son aquellas que obtienen cierta cantidad *grande* de datos y devuelven uno solo.

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Cambiar el tipo de dato de String a Decimal

Antes de comenzar a entrar en profundidad con las funciones, vamos a cambiar el tipo de dato de la columna `guides_revenue` de la tabla `guides`. ***¿Por qué?*** Porque si tratamos de hacer esto:

```sql
USE devcamp_sql_course_schema;

SELECT MIN(guides_revenue) FROM guides;
```

<br/>

La respuesta que obtenemos es `1000`, sin embargo, si hacemos esto:

```sql
SELECT * FROM guides;
```

<br/>

Veremos que el valor más pequeño realmente es `500`. Esto se debe a que la columna `guides_revenue` es realmente de tipo texto. Para obtener el valor deseado, podríamos hacer esto (*como ya hemos visto en apartados anteriores*):

```sql
SELECT MIN(CAST(guides_revenue AS UNSIGNED)) FROM guides;
```

<br/>

Esto funcionaría, sin embargo, puede ser muy tedioso tener que realizar la operación `CAST()` siempre que se quiera trabajar con ese dato. Por ello, vamos a modificar el tipo de dato de la columna.

Para hacerlo, **existen 2 opciones**:

1. Realizar el cambio haciendo uso de la interfaz de MySQL.
    * Entrar en ajustes de la tabla `guides` pulsando la llave inglesa que aparece al hacer *hover* en el menú de la izquierda.
    * Seleccionar el tipo de dato de la columna deseada (*cambiar el `VARCHAR(45)` por `DECIMAL`*).
    * Pulsar `Apply` abajo a la derecha y aceptar.
2. Ejecutar este código:

```sql
ALTER TABLE `devcamp_sql_course_schema`.`guides` 
CHANGE COLUMN `guides_revenue` `guides_revenue` DECIMAL NOT NULL;
```

<br/>

Hecho esto, podemos volver a ejecutar la primera de las funciones:

```sql
SELECT MIN(guides_revenue) FROM guides;
```

<br/>

En esta ocasión, el resultado será `500`, por lo que veremos que funciona correctamente.

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Las funciones MIN, MAX, SUM, AVG y COUNT

Las funciones `MIN`, `MAX`, `SUM`, `AVG` y `COUNT` son *aggregate functions* también, porque toman un montón de información, realizan las operaciones necesarias y devuelven un único dato. Vamos a ver unos pocos ejemplos:

```sql
USE devcamp_sql_course_schema;

SELECT MIN(guides_revenue) FROM guides;		-- min value
-- 500

SELECT MAX(guides_revenue) FROM guides;		-- max value
-- 5000

SELECT SUM(guides_revenue) FROM guides;		-- summatory
-- 10000

SELECT AVG(guides_revenue) FROM guides;		-- average
-- 1428.5714

SELECT COUNT(*) FROM users;					-- counts how many users are in users table
-- 2004
```

<br/>

Además de estos ejemplos simples donde se toman todos los datos de las columnas o incluso de la tabla, una de las cosas que se puede hacer con estas funciones, es pasar cierto filtro, por ejemplo:

```sql
SELECT COUNT(*) FROM addresses
WHERE addresses_state = 'NY';
-- 3
```

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Generar informes resumidos con GROUP BY

Gracias a las funciones descritas en el [apartado anterior](#las-funciones-min,-max,-sum,-avg-y-count), combinadas con `GROUP BY`, podemos generar informes realmente interesantes de los datos que tenemos en las tablas de las bases de datos.

He aquí unos pocos ejemplos:

```sql
SELECT addresses_state, COUNT(addresses_state)
FROM addresses
GROUP BY addresses_state;
```

<br/>

El resultado de esta ejecución muestra lo siguiente:

| `addresses_state` | `COUNT(addresses_state)` |
| ----------------- | ------------------------ |
| NY                | 3                        |
| AZ                | 1                        |

<br/>

Como podemos observar, lo que ha ocurrido es que nos muestra todas las opciones (*valores únicos*) de la columna `addresses_state` y, a continuación, gracias a la función `COUNT()`, nos muestra cuántas veces se usa dicho valor. Esto puede resultar muy útil para saber la cantidad de usuarios que cumplen cierto requisito, por ejemplo.

Veamos otro ejemplo similar:

```sql
SELECT addresses_city, COUNT(addresses_city)
FROM addresses
GROUP BY addresses_city;
```

<br/>

Este es el resultado:

| `addresses_city` | `COUNT(addresses_city)` |
| ---------------- | ----------------------- |
| Manhattan        | 2                       |
| Phoenix          | 1                       |
| Queens           | 1                       |

<br/>

Incluso podríamos obtener la cantidad de ingresos que ha tenido cada usuario con la tabla `guides` y agruparlo por usuario:

```sql
SELECT guides_users_id, SUM(guides_revenue)
FROM guides
GROUP BY guides_users_id;
```

<br/>

Este sería el resultado:

| `guides_users_id` | `SUM(guides_revenue)` |
| ----------------- | --------------------- |
| 2                 | 6500                  |
| 3                 | 3000                  |
| 2006              | 500                   |

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Utilizar comentarios

Existen tres formas de crear comentarios en SQL:

* `-- Inline comment`: comentarios de una sola línea, bastante común de utilizar sobre alguna consulta o para dividir en secciones el código.
* `# Inline comment`: otra forma de generar comentarios en una sola línea.
* `/* Multiline comment */`: una forma de escribir un bloque entero de comentario que puede tener la cantidad de líneas que sean siempre que el texto vaya entre los signos de apertura (`/*`) y cierre (`*/`) de comentarios.

<br/>

Con los comentarios hay que tener en cuenta que por mucho que describamos el comportamiento de un bloque de código, si ese bloque se modifica para que realice otra función, el comentario **no se modifica solo**, es decir, **debemos modificar los comentarios que describen nuestro código cuando dicho código es modificado**.

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Deshabilitar temporalmente el Modo Seguro

En ocasiones, MySQL detiene la ejecución de nuestro código y no nos permite realizar ciertas operaciones porque las considera *peligrosas*. Esto ocurre, por ejemplo, cuando queremos rellenar o modificar los datos de todas las columnas de una tabla.

Para poder solucionar esto, existen dos opciones:

* Deshabilitar desde los ajustes de MySQL el Modo Seguro.
* Deshabilitar mediante comandos el Modo Seguro temporalmente (Recomendado).

<br/>

Esta última opción es la que vamos a realizar a continuación. Vamos a modificar toda la columna de `addresses_city` a un valor cualquiera a modo de ejemplo. Pero, para poder hacer esto, debemos deshabilitar el Modo Seguro.

He aquí el código:

```sql
-- Deshabilitar el modo seguro
SET SQL_SAFE_UPDATES = 0;

-- Modificar una columna entera
BEGIN;	# Para poder deshacer la modificación después
UPDATE addresses
SET addresses_city = 'Oops';
```

<br/>

A continuación, comprobaremos si se ha modificado la columna correctamente:

```sql
SELECT * FROM addresses;
```

<br/>

Veremos que todas las filas de la columna `addresses_city` tienen como valor la palabra `Oops`, por lo que ha funcionado correctamente.

Para devolver la columna a sus valores anteriores, finalmente ejecutaremos lo siguiente:

```sql
ROLLBACK;
```

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Añadir una columna y llenarla con datos aleatorios

Antes de realizar ningún tipo de operación, vamos a comenzar añadiendo una nueva columna a la tabla `guides` llamada `guides_qty`. De nuevo, tenemos dos opciones:

* Realizarlo *a mano*:
    * Clicar en la llave inglesa situada a la derecha del nombre de la tabla en el panel izquierdo.
    * Añadir la nueva columna:
        * **Nombre:** `guides_qty`
        * **Tipo:** `INT`
        * **Extras:** `NOT NULL`
    * Clicar en `Apply` abajo a la derecha.
* Ejecutar el siguiente comando:

```sql
ALTER TABLE `devcamp_sql_course_schema`.`guides` 
ADD COLUMN `guides_qty` INT NOT NULL AFTER `guides_title`;
```

<br/>

Hecho esto, veremos que al tener la condición `NOT NULL` todas las filas de dicha nueva columna tienen el valor `0`. Ahora, pongámonos en la situación en la que quisiéramos rellenar con datos aleatorios una columna entera. En este caso es relativamente sencillo porque nuestra tabla `guides` tiene pocas entradas, pero ***¿qué ocurriría si estuviéramos trabajando con una aplicación de miles de datos?***

Rellenar miles de filas con datos aleatorios a mano es impensable.

Para ello, podemos realizar lo siguiente:

```sql
-- Deshabilitar temporalmente el modo seguro
SET SQL_SAFE_UPDATES = 0;

BEGIN;	-- Por si acaso hacemos algo mal
UPDATE guides
SET guides_qty = RAND()*1000;

-- Ejecutar solo si queremos deshacer los cambios
ROLLBACK;
```

<br/>

Si ahora vemos cómo ha quedado la tabla `guides`, veremos que la nueva columna `guides_qty` está llena de valores aleatorios entre `1` y `1000` (*porque hemos multiplicado el resultado de `RAND()` por `1000`*).

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Usar operadores matemáticos para obtener datos

Habrá momentos en los que queramos obtener datos muy concretos para los que utilicemos las *aggregate functions*, sin embargo, en otras ocasiones, querremos obtener simplemente datos en los que una simple función matemática nos baste. Estos son los operadores más simples que se pueden utilizar en las consultas de SQL:

* `+`: sumas
* `-`: restas
* `*`: multiplicaciones
* `/`: divisiones

<br/>

He aquí un pequeño ejemplo, partiendo de la siguiente tabla `guides`:

| guides_id | guides_revenue | guides_users_id | guides_title            | guides_qty |
| --------- | -------------- | --------------- | ----------------------- | ---------- |
| 1         | 500            | 2               | My Blog                 | 543        |
| 2         | 1500           | 3               | Something Else          | 685        |
| 3         | 750            | 3               | My Great Post           | 847        |
| 4         | 1000           | 2               | My Blog                 | 148        |
| 5         | 750            | 3               | My Blog                 | 100        |
| 6         | 5000           | 2               | Another One of My Posts | 552        |
| 7         | 500            | 2006            | Guide by Jon            | 331        |

<br/>

Si quisiéramos obtener cuánto ha ganado cada usuario por sus posts, podríamos realizar la división entre `guides_revenue` y `guides_qty`:

```sql
USE devcamp_sql_course_schema;

SELECT
/* Seleccionamos estas columnas para mejorar
la legibilidad de los datos obtenidos */
guides_title,
guides_revenue,
guides_qty,
guides_revenue / guides_qty	-- Operación matemática
FROM guides;
```

<br/>

<hr/><hr/><br/>

<div align='right'><a href='#index'>Volver arriba</a></div>

## Añadir nombres customizados a las columnas

A la hora de presentar u exportar los datos, es muy importante saber cómo realizar esta presentación de tal forma que se diferencien y se obtenga fácilmente la información.

Si quisiéramos mostrar a alguien los datos almacenados en la tabla `users`, veríamos que tenemos miles de usuarios registrados en ella. A la hora de presentar estos datos, quizá no queda claro si la columna es el nombre, el apellido, etc. Para solucionar esto, podemos añadir columnas con nombres customizados al lado de cada dato.

He aquí un ejemplo sencillo:

```sql
USE devcamp_sql_course_schema;

SELECT 'Email:', users_email, 'Name:', users_name
FROM users;
```

<br/>

El resultado obtenido en este caso sería el siguiente:

| Email: | users_email    | Name: | users_name |
| ------ | -------------- | ----- | ---------- |
| Email: | test0@test.com | Name: | Demo 0     |
| Email: | test1@test.com | Name: | Demo 1     |
| Email: | test3@test.com | Name: | Demo 3     |
| Email: | ...            | Name: | ...        |

<br/>

Como ya hemos mencionado, esto puede resultar muy útil si pretendemos presentar miles de datos con columnas que pueden confundirse entre sí. De esta forma, queda mucho más claro a qué hace referencia cada uno de los datos.

Además, si se exporta la tabla a determinados formatos, los encabezados podrían no estar presentes. Exportando los datos de esta forma, no son necesarios dichos encabezados y se solucionaría ese problema.

<br/>

<hr/><hr/><br/>

[<< CONSULTAS AVANZADAS](./03_advanced_queries.md#consultas-avanzadas) | [HOME](../../..README.md#devcamp) | [CONTROL FLOW >>](./05_control_flow.md#control-flow)

# Consultas Relacionales

<div id='index'></div>

* [Inner Joins](#inner-joins)
    * [Varios condicionales en un Inner Join](#varios-condicionales-en-un-inner-join)


<br/>

[<< CONTROL FLOW](./05_control_flow.md#control-flow) | [HOME](../../README.md#devcamp) | 

<br/>

<hr/><hr/><br/>

Hasta ahora, a lo largo del curso, hemos visto cómo hacer diversas operaciones con las tablas y las bases de datos en general. En esta sección, vamos a ver cuál es uno de los motivos principales por los cuales SQL es una herramienta tan solicitada: las **consultas relacionales**.

***- ¿Qué son las consultas relacionales?***

Como su nombre indica, una consulta relacional es aquella consulta que obtiene información (*realiza consultas*) a más de una tabla a la vez. Es decir, relacionar los datos de una tabla con los datos de otra y obtener esa información. ¡Vamos a ver cómo se consigue esto!

<br/>

<hr/><hr/><br/>

## Inner Joins

Como siempre, vamos a explicar cómo realizar estas consultas con ejemplos. En primer lugar, vamos a recordar qué parámetros (*columnas*) tenemos en las tablas `guides` y `users`:

* Tabla `guides`:
    * `guides_id`
    * `guides_revenue`
    * `guides_users_id`
    * `guides_title`
    * `guides_qty`

* Tabla `users`:
    * `users_id`
    * `users_name`
    * `users_email`

<br/>

Partiendo de estas dos tablas, vamos a hacer una consulta que devuelva información de ambas:

```sql
SELECT * FROM guides							# (1)
INNER JOIN users								# (2)
ON guides.guides_users_id = users.users_id;		# (3)
```

<br/>

* **(1):** indicamos qué es lo que queremos obtener.
* **(2):** indicamos con qué tabla debemos relacionar la tabla anteriormente indicada.
* **(3):** indicamos qué columna de la primera tabla está relacionada con qué columna de la segunda.

<br/>

El resultado obtenido es el siguiente:

| `guides_id` | `guides_revenue` | `guides_users_id` | `guides_title`          | `guides_qty` | `users_id` | `users_names` | `users_email`    |
| ----------- | ---------------- | ----------------- | ----------------------- | ------------ | ---------- | ------------- | ---------------- |
| 1           | 500              | 2                 | My Blog                 | 543          | 2          | Kristine      | update@test.com  |
| 2           | 1500             | 3                 | Something Else          | 685          | 3          | Tiffany       | tiffany@test.com |
| 3           | 750              | 3                 | My Great Post           | 0            | 3          | Tiffany       | tiffany@test.com |
| 4           | 1000             | 2                 | My Blog                 | 0            | 2          | Kristine      | update@test.com  |
| 5           | 750              | 3                 | My Blog                 | 0            | 3          | Tiffany       | tiffany@test.com |
| 6           | 5000             | 2                 | Another One of My Posts | 0            | 2          | Kristine      | update@test.com  |
| 7           | 500              | 2006              | Guide by Jon            | 0            | 2006       | Jon           | jon@snow.com     |

<br/>

Como se puede observar, se ha recibido como resultado toda la información de ambas tablas. Esto se debe a que hemos utilizado un `SELECT *` a la hora de realizar la consulta.

> Utilizar `INNER JOIN` es exactamente lo mismo que usar solamente `JOIN`, porque es el tipo de unión por defecto.
>
> A partir de ahora, haremos uso de `JOIN` al realizar este tipo de uniones para que sea ligeramente más corto el código.

<br/>

He aquí otro ejemplo, donde seleccionaremos las columnas que deseemos obtener, haremos uso de [aliases](./05_control_flow#alias-en-tablas), y funciones vistas en otros apartados:

```sql
SELECT
	g.guides_title,
	g.guides_revenue,
	u.users_name,
	u.users_email
FROM guides g
JOIN users u
ON g.guides_users_id = u.users_id
ORDER BY g.guides_revenue DESC;
```

<br/>

Con esto, lo que conseguimos es lo siguiente:

| `guides_title`          | `guides_revenue` | `users_name` | `users_email`    |
| ----------------------- | ---------------- | ------------ | ---------------- |
| Another One of My Posts | 5000             | Kristine     | update@test.com  |
| Something Else          | 1500             | Tiffany      | tiffany@test.com |
| My Blog                 | 1000             | Kristine     | update@test.com  |
| My Great Post           | 750              | Tiffany      | tiffany@test.com |
| My Blog                 | 750              | Tiffany      | tiffany@test.com |
| My Blog                 | 500              | Kristine     | update@test.com  |
| Guide by Jon            | 500              | Jon          | jon@snow.com     |

<br/>

Como se puede observar en la tabla, tenemos las 4 columnas que habíamos seleccionado, podemos ver qué usuario ha realizado cada guía (*al igual que en el ejemplo anterior*), y tenemos la consulta ordenada de forma descendiente según la columna `guides_revenue`.

<br/>

<hr/><br/>

### Varios condicionales en un Inner Join

Hemos visto cómo realizar consultas simples utilizando la unión `INNER JOIN` (*también llamada simplemente `JOIN`*). Vamos a ver otro ejemplo donde añadir varias condiciones:

```sql
# 1 condición basada en la tabla `users`
SELECT * FROM guides g
JOIN users u
ON g.guides_users_id = u.users_id
WHERE u.users_name = 'Tiffany';

# 1 condición basada en la tabla `guides`
SELECT * FROM guides g
JOIN users u
ON g.guides_users_id = u.users_id
WHERE g.guides_revenue > 700;

# Varias condiciones basadas en ambas tablas
SELECT * FROM guides g
JOIN users u
ON g.guides_users_id = u.users_id
WHERE g.guides_revenue > 750
AND u.users_name = 'Tiffany'
OR u.users_name = 'Kristine';
```


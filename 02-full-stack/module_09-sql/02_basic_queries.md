# SQL Queries

<div id='index'></div>

* [Añadir registros a una base de datos](#añadir-registros-a-una-base-de-datos)
* [Consultar todos los registros de una tabla](#consultar-todos-los-registros-de-una-tabla)

<br/>


[<< TIPOS DE DATOS](./01_data_types.md#sql-data-types) | [HOME](../../README.md#devcamp)


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Añadir registros a una base de datos

Para añadir registros a las tablas que ya hemos creado, debemos escribir una serie de líneas de código SQL:

```sql
-- say which schema we're going to use
USE devcamp_sql_course_schema;

-- insert data to 'table-name' table

INSERT INTO users(users_name, users_email)
VALUES ("Kristine", 'kristine@test.com');

INSERT INTO users(users_name, users_email)
VALUES ("Tiffany", 'tiffany@test.com');

INSERT INTO users(users_name, users_email)
VALUES ("Jordan", 'jordan@test.com');

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("123 Any Street", "", 'Manhattan', 'NY', '53853', 2);

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("456 Any Street", "Suite 333", 'Phoenix', 'AZ', '84632', 2);

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("123 Any Street", "", 'Manhattan', 'NY', '53853', 3);

INSERT INTO addresses(addresses_street_one, addresses_street_two, addresses_city, addresses_state, addresses_postal_code, addresses_users_id)
VALUES ("123 Any Street", "", 'Queens', 'NY', '53853', 4);

INSERT INTO guides(guides_title, guides_users_id, guides_revenue)
VALUES ("My Blog", 2, 500);

INSERT INTO guides(guides_title, guides_users_id, guides_revenue)
VALUES ("Another Post", 3, 1500);

INSERT INTO guides(guides_title, guides_users_id, guides_revenue)
VALUES ("My Great Post", 3, 750);
```

<br/>

Si miramos las tablas, veremos que se han añadido los datos indicados.

<br/>

**Notas:**

* No es necesario seguir el orden de las columnas a la hora de insertar datos, pero sí el orden de la sentancia: `INSERT INTO table_name(column1, column2, column3, ...) VALUES (value1, value2, value3, ...)`.
* Si no se indica el valor de una columna, se insertará el valor por defecto, que puede ser `NULL` o un valor por defecto que se haya indicado al crear la tabla.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## Consultar todos los registros de una tabla

Para consultar todos los registros de una tabla, usaremos la siguiente sintaxis:

```sql
SELECT * FROM table_name;
```

<br/>

En nuestro caso, para cada una de las tablas:

```sql
SELECT * FROM users;
SELECT * FROM addresses;
SELECT * FROM guides;
```

<br/>

**Notas:**

* El asterisco `*` indica que queremos seleccionar todas las columnas de la tabla.
* Si queremos seleccionar solo algunas columnas, debemos indicarlas separadas por comas:

```sql
SELECT column1, column2, column3 FROM table_name;
```

<br/>

> Si tenemos varias líneas de código SQL, podemos ejecutar la línea que queramos seleccionando la línea y ejecutando el código (*con el símbolo del rayo, o con `Control + Enter`*).
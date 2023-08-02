# Funciones

<div id='index'></div>

* [Introducción a las funciones](#introducción-a-las-funciones)
* [Cambiar el tipo de dato de String a Decimal](#cambiar-el-tipo-de-dato-de-string-a-decimal)

<br/>

[<< CONSULTAS AVANZADAS](./03_advanced_queries.md#consultas-avanzadas) | [HOME](../../..README.md#devcamp)

<br/>

<hr/><hr/><br/>

## Introducción a las funciones

En SQL es muy típico utilizar funciones para obtener cierta información de nuestras tablas. Con los ejemplos que hemos ido trabajando a lo largo de las secciones anteriores, podríamos crear una función que tomara todos los datos de `guides_revenue` y nos devolviera el total de dicha columna, por ejemplo.

A ese tipo de funciones se les llama ***aggregate functions***, que son aquellas que obtienen cierta cantidad *grande* de datos y devuelven uno solo.

<br/>

<hr/><hr/><br/>

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
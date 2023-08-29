# SQL Data Types

<div id='index'></div>

Estos son los datos más comunes:

* [`CHARACTER`](#character)
* [`VARCHAR`](#varchar)
* [`BOOLEAN`](#boolean)
* [`SMALLINT`](#smallint)
* [`INTEGER`](#integer)
* [`DECIMAL`](#decimal)
* [`FLOAT`](#float)
* [`DATETIME`](#datetime)
* [`CLOB`](#clob)
* [`BLOB`](#blob)

<br/>


[<< PRIMEROS PASOS](./00_first_steps.md#sql) | [HOME](../../README.md#devcamp) | [SQL QUERIES >>](./02_basic_queries.md#sql-queries)


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## CHARACTER

* Fixed length string
* Fastest lookup for strings if properly structured
* Takes 100% space allocated
* 1 to 255 characters

**Explicación:** son tipos de datos de longitud fija, es decir, que ocupan el mismo espacio en memoria, independientemente de la longitud del dato que contengan.

> Por ejemplo, si tenemos un campo de tipo `CHAR(10)` y guardamos un dato de 5 caracteres, el campo ocupará 10 caracteres en memoria, los 5 del dato y 5 espacios en blanco.

<br/>

Si utilizamos:

```sql
CHAR(10)
```

* **Uso correcto:**

```sql
-- datos de longitud fija (siempre 10 caracteres)
"5555555555"    -- 10 caracteres
"9999999999"    -- 10 caracteres
```

* **Mal uso:**

```sql
5555555555      -- faltan las comillas ""
"John Smith"    -- nombre: cantidad de caracteres variable para cada registro
```

> Si el dato que se va a guardar es de longitud variable, se debe usar el tipo de dato `VARCHAR`.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## VARCHAR

* Variable length string
* Slower performance than properly formatted `CHAR`
* Dynamic memory allocation
* 1 to 65535 characters

**Explicación:** son tipos de datos de longitud variable, es decir, que ocupan el espacio en memoria que necesiten, dependiendo de la longitud del dato que contengan.

> Por ejemplo, si tenemos un campo de tipo `VARCHAR(10)` y guardamos un dato de 5 caracteres, el campo ocupará 5 caracteres en memoria, los 5 del dato.

<br/>

Si utilizamos:

```sql
VARCHAR(150)
```

* **Uso correcto:**

```sql
-- datos de longitud variable (máximo 150 caracteres)
"Any tipe of string with variable sizes"
```

* **Mal uso:**

```sql
5555555555      -- faltan las comillas ""
-- datos de longitud fija (siempre 10 caracteres)
"5555555555"
"9999999999"
```

> Si los datos que se van a guardar son siempre de longitud fija (como un número de telefono), se debe usar el tipo de dato `CHAR`.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## BOOLEAN

* True or False values

**Explicación:** son tipos de datos que solo pueden tener dos valores: `TRUE` o `FALSE`.

<br/>

Si utilizamos:

```sql
BOOLEAN
```

* **Uso correcto:**

```sql
TRUE
FALSE
true
false
```

* **Mal uso:**

```
0, 1
T, F
Yes, No
'Anything besides true or false'
```

> Para que el tipo de dato `BOOLEAN` funcione correctamente, se debe usar `TRUE` o `FALSE` escrito tanto en mayúscula como en minúscula.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## SMALLINT

* Integers ranging from -32768 to 32767
* Decimals are truncated

**Explicación:** son tipos de datos que solo pueden tener valores enteros, sin decimales, y que van desde -32768 hasta 32767.

<br/>

Si utilizamos:

```sql
SMALLINT
```

* **Uso correcto:**

```sql
-32768
32768
42.5    -- se trunca a 42
```

* **Mal uso:**

```sql
32769           -- fuera de rango
"any string"    -- tipo de dato incorrecto
```

> Si se necesita guardar un número entero que supere el rango de `SMALLINT`, se debe usar el tipo de dato `INTEGER`.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## INTEGER

* Integers ranging from -2147483647 to 2147483647
* Decimals are truncated

<br/>

Si utilizamos:

```sql
INTEGER     -- o INT
```

* **Uso correcto:**

```sql
-2147483647
2147483647
42.5    -- se trunca a 42
```

* **Mal uso:**

```sql
2147483648      -- fuera de rango
"any string"    -- tipo de dato incorrecto
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>


## DECIMAL

* Allows for decimal based values
* Works with precision and scale
* No more than 38 digits

**Explicación:**

* `PRECISION`: cantidad de dígitos que puede tener el número
* `SCALE`: cantidad de dígitos que puede tener la parte decimal

<br/>

Si utilizamos:

```sql
DECIMAL
DECIMAL(precision, scale)
```

* **Uso correcto:**

```sql
DECIMAL(4, 3)   -- 4 dígitos (total), 3 decimales -> 9.812
DECIMAL(7, 2)   -- 7 dígitos (total), 2 decimales -> 12345.67
```

* **Mal uso:**

```sql
"any string"                                -- tipo de dato incorrecto
384930248593987234990.923847234093842341    -- más de 38 dígitos
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## FLOAT

* Large numeric values
* 179 followed by 306 zeros
* Doesn't require explicit precision/scale
* Poor for comparison

**Explicación:** son tipos de datos que permiten guardar números muy grandes, de hasta 179 dígitos seguidos de 306 ceros.

<br/>

Si utilizamos:

```sql
FLOAT
```

* **Uso correcto:**

```sql
9.834
23423422242215.85232
```

* **Mal uso:**

```sql
"any string"    -- tipo de dato incorrecto
9.5 = 9.5       -- pueden no ser iguales
```

> A veces, un número `FLOAT` puede guardarse como `9.4999999...` en lugar de `9.5`, por lo que no se deben comparar números de este tipo.


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## DATETIME

* Date/Time values
* January 1, 1753 through December 31, 9999

<br/>

Si utilizamos:

```sql
DATETIME
```

* **Uso correcto:**

```sql
1968-10-23 1:45:37.123
1972-11-05 00:00:00.000
```

* **Mal uso:**

```sql
"any string"                -- tipo de dato incorrecto
10-23-1968 1:45:37.123      -- wrong format
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## CLOB

* Very large character based data
* Up to 2GB
* Character large object

<br/>

Si utilizamos:

```sql
CLOB
```

* **Uso correcto:**

```sql
"Very very large strings"
```

* **Mal uso:**

```sql
"any small string"      -- no necesario para strings pequeños
934                     -- tipo de dato incorrecto
```


<br/><hr/>
<hr/><br/>


<div align='right'>
    <a href='#index'>Volver arriba</a>
</div>
## BLOB

* Very large binary based data
* Up to 2GB
* Binary large object

<br/>

Si utilizamos:

```sql
BLOB
```

* **Uso correcto:**

```
Binary based image file
```

* **Mal uso:**

```sql
"any small string"      -- no necesario para strings pequeños
934                     -- tipo de dato incorrecto
```


<br/><hr/>
<hr/><br/>


[<< PRIMEROS PASOS](./00_first_steps.md#sql) | [HOME](../../README.md#devcamp) | [SQL QUERIES >>](./02_basic_queries.md#sql-queries)
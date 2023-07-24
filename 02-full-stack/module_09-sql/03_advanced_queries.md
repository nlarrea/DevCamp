# Consultas avanzadas

<div id='index'></div>

*   [Rangos](#rangos)

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


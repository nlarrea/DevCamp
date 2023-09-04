# Proyecto

[<< CONCEPTOS AVANZADOS](./07_advanced_topics.md#conceptos-avanzados) | [HOME](../../README.md#devcamp) | [REDIS >>](./09_redis.md#redis)

<br/>

<hr/><hr/><br/>

## Resumen del proyecto

Construye una base de datos SQL para una universidad que maneje alumnos, cursos, profesorado y notas.

<br/>

## Requisitos técnicos del proyecto

El proyecto necesita contener las siguientes características técnicas:

* Crea una base de datos con las siguientes tablas: `Students`, `Courses`, `Professors`, `Grades`.
* Crea claves foráneas para relacionar las tablas entre sí.
* Crea un *script* que rellene todas las tablas con datos de ejemplo.
* Crea *scripts* de consulta SQL para:
    * La nota media que da cada profesor.
    * Las mejores notas de cada estudiante.
    * Ordenar a los estudiantes por los cursos en los que están matriculados.
    * Crear un informe resumido de los cursos y sus notas medias, ordenados desde el curso más difícil (*curso con la nota media más baja*) hasta el curso más fácil.
    * Encontrar qué estudiante y profesor tienen más cursos en común.

<br/>

<hr/><hr/><br/>

## Mis soluciones

Evidentemente, existen diversas formas de solucionar estos ejercicios. A continuación, mostraré la forma en la que yo he decidido resolverlos.

### Crea una base de datos con las siguientes tablas

* Tabla `Students`:

| Nombre de columna | Tipo de dato   | Características                               |
| ----------------- | -------------- | --------------------------------------------- |
| `students_id`     | `INT`          | Primary Key, Not Null, Unique, Auto Increment |
| `students_name`   | `VARCHAR(45)`  | Not Null                                      |
| `students_email`  | ` VARCHAR(80)` | Not Null, Unique                              |

<br/>

* Tabla `Courses`:

| Nombre de columna | Tipo de dato  | Características                               |
| ----------------- | ------------- | --------------------------------------------- |
| `courses_id`      | `INT`         | Primary Key, Not Null, Unique, Auto Increment |
| `courses_name`    | `VARCHAR(80)` | Not Null                                      |

<br/>

* Tabla `Professors`:

| Nombre de columna  | Tipo de dato  | Características                               |
| ------------------ | ------------- | --------------------------------------------- |
| `professors_id`    | `INT`         | Primary Key, Not Null, Unique, Auto Increment |
| `professors_name`  | `VARCHAR(45)` | Not Null                                      |
| `professors_email` | `VARCHAR(80)` | Not Null, Unique                              |

<br/>

* Tabla `Grades`:

| Nombre de columna      | Tipo de dato    | Características                               |
| ---------------------- | --------------- | --------------------------------------------- |
| `grades_id`            | `INT`           | Primary Key, Not Null, Unique, Auto Increment |
| `grades_students_id`   | `INT`           | Not Null                                      |
| `grades_professors_id` | `INT`           | Not Null                                      |
| `grades_courses_id`    | `INT`           | Not Null                                      |
| `grades_grade`         | `DECIMAL(4, 2)` | Not Null                                      |

<br/>

### Crea claves foráneas para relacionar las tablas entre sí

Teniendo en cuenta la distribución realizada en las tablas, las claves foráneas se encontrarán todas en la tabla `Grades`:

* `grades_students_id` estará relacionada con `students_id` de la tabla `Students`.
* `grades_courses_id` estará relacionada con `courses_id` de la tabla `Courses`.
* `grades_professors_id` estará relacionada con `professors_id` de la tabla `Professors`.

<br/>

### Crea un script que rellene todas las tablas con datos de ejemplo

```sql
USE university_project_schema;

INSERT INTO courses(courses_name)
VALUES
	('Analog Electronics'),
    ('Digital Electronics'),
    ('Industrial Computing'),
    ('Automatic Regulation'),
    ('Electronic Technology');


INSERT INTO students(students_name, students_email)
VALUES
	('Student1', 'student1@test.com'),
    ('Student2', 'student2@test.com'),
    ('Student3', 'student3@test.com'),
    ('Student4', 'student4@test.com'),
    ('Student5', 'student5@test.com'),
    ('Student6', 'student6@test.com'),
    ('Student7', 'student7@test.com'),
    ('Student8', 'student8@test.com'),
    ('Student9', 'student9@test.com'),
    ('Student10', 'student10@test.com');
    

INSERT INTO professors(professors_name, professors_email)
VALUES
	('Professor1', 'professor1@test.com'),
    ('Professor2', 'professor2@test.com'),
    ('Professor3', 'professor3@test.com');


INSERT INTO grades(grades_courses_id, grades_students_id, grades_professors_id, grades_grade)
VALUES
	(1, 1, 1, 5.0),
    (1, 4, 1, 4.9),
    (1, 5, 1, 5.5),
    (1, 7, 1, 9.0),
    (1, 8, 1, 3.2),
    (1, 9, 1, 7.8),
    (2, 1, 2, 9.0),
    (2, 3, 2, 6.7),
    (2, 4, 2, 8.6),
    (2, 7, 2, 5.0),
    (2, 8, 2, 7.3),
    (3, 3, 3, 10.0),
    (3, 6, 3, 9.8),
    (3, 10, 3, 8.4),
    (4, 2, 2, 5.2),
    (4, 6, 2, 7.6),
    (4, 10, 2, 7.7),
    (5, 2, 1, 4.3),
    (5, 5, 1, 5.6),
    (5, 9, 1, 7.7);
```

<br/>

### Crea *scripts* de consulta SQL

* **Para la nota media que da cada profesor:**

```sql
USE university_project_schema;

SELECT
p.professors_name,
AVG(g.grades_grade) AS 'Given average grade'
FROM grades g
JOIN professors p ON g.grades_professors_id = p.professors_id
GROUP BY g.grades_professors_id;
```

> Resultado:
>
> | professors_name | Given average grade |
> | --------------- | ------------------- |
> | Professor1      | 5.888889            |
> | Professor2      | 7.137500            |
> | Professor3      | 9.400000            |

<br/>

* **Para las mejores notas de cada estudiante:**

```sql
USE university_project_schema;

SELECT
s.students_name,
MAX(g.grades_grade) AS top_grade
FROM grades g
JOIN students s ON g.grades_students_id = s.students_id
GROUP BY g.grades_students_id;
```

> Resultado:
>
> | students_name | top_grade |
> | ------------- | --------- |
> | Student1      | 9.00      |
> | Student2      | 5.20      |
> | Student3      | 10.00     |
> | Student4      | 8.60      |
> | Student5      | 5.60      |
> | Student6      | 9.80      |
> | Student7      | 9.00      |
> | Student8      | 7.30      |
> | Student9      | 7.80      |
> | Student10     | 8.40      |

<br/>

* **Para ordenar a los estudiantes por los cursos en los que están matriculados:**

```sql
USE university_project_schema;

SELECT
s.students_name,
c.courses_id,
c.courses_name
FROM grades g
JOIN students s ON g.grades_students_id = s.students_id
JOIN courses c ON g.grades_courses_id = c.courses_id
ORDER BY g.grades_courses_id ASC;
```

> Resultado:
>
> | students_name | courses_id | courses_name          |
> | ------------- | ---------- | --------------------- |
> | Student1      | 1          | Analog Electronics    |
> | Student4      | 1          | Analog Electronics    |
> | Student5      | 1          | Analog Electronics    |
> | Student7      | 1          | Analog Electronics    |
> | Student8      | 1          | Analog Electronics    |
> | Student9      | 1          | Analog Electronics    |
> | Student1      | 2          | Digital Electronics   |
> | Student3      | 2          | Digital Electronics   |
> | Student4      | 2          | Digital Electronics   |
> | Student7      | 2          | Digital Electronics   |
> | Student8      | 2          | Digital Electronics   |
> | Student3      | 3          | Industrial Computing  |
> | Student6      | 3          | Industrial Computing  |
> | Student10     | 3          | Industrial Computing  |
> | Student2      | 4          | Automatic Regulation  |
> | Student6      | 4          | Automatic Regulation  |
> | Student10     | 4          | Automatic Regulation  |
> | Student2      | 5          | Electronic Technology |
> | Student5      | 5          | Electronic Technology |
> | Student9      | 5          | Electronic Technology |

<br/>

* **Para crear un informe resumido de los cursos y sus notas medias, ordenados desde el curso más difícil (*curso con la nota media más baja*) hasta el curso más fácil:**

```sql
USE university_project_schema;

SELECT
c.courses_name,
AVG(g.grades_grade) AS grade_average
FROM grades g
JOIN courses c ON g.grades_courses_id = c.courses_id
GROUP BY g.grades_courses_id
ORDER BY grade_average ASC;
```

> Resultado:
>
> | courses_name          | grade_average |
> | --------------------- | ------------- |
> | Electronic Technology | 5.866667      |
> | Analog Electronics    | 5.900000      |
> | Automatic Regulation  | 6.833333      |
> | Digital Electronics   | 7.320000      |
> | Industrial Computing  | 9.400000      |

<br/>

* **Encontrar qué estudiante y profesor tienen más cursos en común:**

```sql
USE university_project_schema;

SELECT
s.students_name,
p.professors_name,
COUNT(DISTINCT c.courses_id) AS courses_in_common
FROM grades g
JOIN students s ON g.grades_students_id = s.students_id
JOIN professors p ON g.grades_professors_id = p.professors_id
JOIN courses c ON g.grades_courses_id = c.courses_id
GROUP BY s.students_name, p.professors_name
ORDER BY courses_in_common DESC
LIMIT 5;	-- Select the first 5 from the returned list
```

> Como se puede observar, se limita el resultado a 5 elementos, sin embargo, podría limitarse a `1` y obtener el que más encaja con la descripción del apartado, o al número que se desee.
>
> Este es el resultado:
>
> | students_name | professors_name | courses_in_common |
> | ------------- | --------------- | ----------------- |
> | Student9      | Professor1      | 2                 |
> | Student5      | Professor1      | 2                 |
> | Student1      | Professor1      | 1                 |
> | Student1      | Professor2      | 1                 |
> | Student10     | Professor2      | 1                 |

<br/>

Otra forma de realizar este ejercicio podría haber sido la siguiente:

```sql
USE university_project_schema;

WITH cte AS (
	SELECT
	s.students_name,
	p.professors_name,
	COUNT(DISTINCT c.courses_id) counter
	FROM grades g
	JOIN students s ON g.grades_students_id = s.students_id
	JOIN professors p ON g.grades_professors_id = p.professors_id
	JOIN courses c ON g.grades_courses_id = c.courses_id
	GROUP BY s.students_name, p.professors_name
)

SELECT * FROM cte
WHERE cte.counter = (
	SELECT MAX(counter) FROM cte
);
```

> Resultado:
>
> | students_name | professors_name | counter |
> | ------------- | --------------- | ------- |
> | Student5      | Professor1      | 2       |
> | Student9      | Professor1      | 2       |

<br/>

<hr/><hr/><br/>

[<< CONCEPTOS AVANZADOS](./07_advanced_topics.md#conceptos-avanzados) | [HOME](../../README.md#devcamp) | [REDIS >>](./09_redis.md#redis)
# Diagramas de clase

* [Elementos](#elementos)
* [Ejemplo](#ejemplo-de-un-diagrama-de-clase)
* [Asociaciones](#asociaciones)


<br><hr>
<hr><br>


## Elementos

Como recordatorio, decir que los elementos que crean un `class diagram` son:

* Nombre
* Atributos
* Métodos u operaciones

<br>

### Nombre de la clase

El primer cuadrado del diagrama contiene el nombre de la clase. Es decir, cómo se llamará la clase en el código.

<br>

### Atributos

El segundo bloque del diagrama lo conforman los atributos de la clase. Estos son los datos que la clase va a manejar.

Los tributos deben tener al menos 3 partes obligatorias:

1. **Visibilidad** del atributo, donde puede ser:
    * Público: `+`
    * Protegido: `#`
    * Privado: `-`

2. El título o **nombre** del atributo. Si estos fueran a usarse en bases de datos, la forma de llamarlos en la base de datos sería el título descrito aquí.

3. El **tipo de dato** del atributo. Se coloca detrás del título del atributo, separado por dos puntos `:`.

<br>

**Por ejemplo:**

```plantuml
+ title:string
# slug:string
- created_at:datetime
- updated_at:datetime
```

<br>

### Métodos u operaciones

El tercer y último bloque del diagrama lo conforman los métodos u operaciones de la clase. Estos son las acciones que la clase va a realizar.

De nuevo, hay que indicar la visibilidad del método, y añadirle los `( )` para indicar que es un método después del nombre del método.

<br>

**Por ejemplo:**

```plantuml
+ get_title()
```


<br><hr>
<hr><br>


## Ejemplo de un diagrama de clase

<div align="center">

![class-diagram](./media/structural-diagrams/class-diagram.png)

</div>


<br><hr>
<hr><br>


## Asociaciones

Las asociaciones son las relaciones que existen entre las clases. Para poder definir una asociación, se debe indicar:

* Asociación
* Multiplicidad
* Navegabilidad


<style>
    img {
        width: 75%;
        max-width: 600px;
    }
</style>

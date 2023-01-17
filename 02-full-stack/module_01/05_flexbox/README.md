# Flexbox

<div id="indice"></div>

* [flex-direction](#flex-direction)
* [justify-content](#justify-content)
* [flex-basis](#flex-basis)


<br><hr>
<hr><br>


## flex-direction

<sub>[Volver al índice](#indice) | [justify-content >>](#justify-content)</sub>

Esta propiedad permite seleccionar el eje principal de un ***flex container***.

Para crear un ***flex container***, utilizamos la propiedad `display: flex;` en un elemento. Esto nos permite utilizar las propiedades de ***flexbox*** en ese elemento.

<br>

Las opciones posibles para esta propiedad son las siguientes:

* `flex-direction: row;` (default)
* `flex-direction: row-reverse;`
* `flex-direction: column;`
* `flex-direction: column-reverse;`

<br>

Si tenemos un ***flex container*** dentro de otro ***flex container***, uno debe tener dirección `row` y el otro `column`.

Si utilizamos `display: flex;` en un elemento, por defecto, su dirección es `row`.


<br><hr>
<hr><br>


## justify-content

<sub>[<< flex-direction](#flex-direction) | [Volver al índice](#indice) | [flex-basis >>](#flex-basis)</sub>

La propiedad `justify-content` nos permite alinear los elementos de un ***flex container*** en el eje principal.

Por recordar, el eje principal se define utilizando la propiedad `flex-direction`. Si la dirección es `row`, el eje principal es horizontal y si es `column`, el eje principal es vertical.

<br>

Las posibilidades al utilizar esta propiedad son las siguientes:

* `justify-content: flex-start;` (default) → los elementos se alinean al inicio del ***flex container***.
* `justify-content: flex-end;` → los elementos se alinean al final del ***flex container***.
* `justify-content: center;` → los elementos se alinean al centro del ***flex container***.
* `justify-content: space-between;` → los elementos se distribuyen en el ***flex container***, dejando un espacio entre ellos.
* `justify-content: space-around;` → los elementos se distribuyen en el ***flex container***, dejando un espacio entre ellos y alrededor de los elementos.
* `justify-content: space-evenly;` → los elementos se distribuyen en el ***flex container***, dejando espacios iguales entre ellos y alrededor de los elementos.


<br><hr>
<hr><br>


## flex-basis


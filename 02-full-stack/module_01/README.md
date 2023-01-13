# Introducción a SCSS

* [¿Qué es SCSS?](#¿qué-es-scss)
* [Diferencia entre SASS y SCSS](#diferencia-entre-sass-y-scss)
* [Variables y estructura SCSS](#variables-y-estructura-scss)
    * [Valores por defecto](#default-values)
    * [Anidación](#anidación-en-scss)
* [Mixins](#mixins)
    * [Mixins con argumentos](#mixins-con-argumentos)
    * [Mixins con condicionales](#mixins-con-condicionales)
* [Crear clases dinámicas](#crear-clases-dinámicas)
    * [Listas](#listas)
    * [Directiva each](#directiva-each)
    * [Interpolación de Strings](#interpolación-de-strings)
* [Import](#import)

<br><hr>
<hr><br>


## ¿Qué es SCSS?

SCSS son las siglas de Sassy Cascading Style Sheets. Fue creado hace aproximadamente 10 años por Hampton Catlin.

¿Dónde se puede usar SCSS? A día de hoy, puede usarse en prácticamente cualquier tipo de framework. No está atado a ningún tipo concreto de elemento.

¿Por qué usar SCSS? SCSS permite agilizar todo el proceso de implementación de un diseño. Escribir únicamente con CSS puro está bien, pero lo que SCSS permite, es agilizar el proceso de implementación de un diseño, ya que permite escribir código CSS de una forma más sencilla y rápida, eliminando cualquier tipo de proceso repetitivo.

Técnicamente, SCSS es un preprocesador, lo que significa que es un tipo de lenguaje que el navegador no entiende. Cuando el preprocesador se ejecuta, lo que hace es convertir todo el código SCSS que escribiste en código CSS, de forma que el navegador sí que lo entienda, construyendo tus propios archivos CSS para ti.


<br><hr>
<hr><br>


## Diferencia entre SASS y SCSS

**SASS** es la versión original de SCSS. No se parece en nada al CSS y se preocupa por cosas como la indentación. No tiene llaves, tiene signos de más y signos de igual por todas partes, etc.

**SCSS** se parece exactamente al CSS, usa llaves y puntos y comas. Es mucho más familiar.

Si quieres escribir código CSS puro, un archivo SCSS lo procesará, mientras que la versión original de SASS lanzaría un error.


<br><hr>
<hr><br>


## Variables y estructura SCSS

Las variables son una especie de contenedor donde se puede almacenar el valor de una propiedad. En este caso, vamos a crear dos variables de colores para aplicarlas a lo largo el programa:

``` scss
$off-white: #f6f6f6;
$master-site-color: darkred;

body {
    background-color: $off-white;
    height: 100vh;
    width: 100vw;
}

.container {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 0.8rem;
}

.page-wrapper {
    padding: 21px;

    .featured {
        color: $master-site-color;
    }

    .page-content{
        background-color: $master-site-color;
        padding: 42px;
        color: $off-white;

        .container {
            font-family: 'Courier New', Courier, monospace;
        }
    }
}
```

<br>

Este sería el resultado:

![00-variables.png](../images/module-01/01-variables/00-variables.png)

<br>

Como se puede ver, las variables son muy útiles para no tener que repetir el mismo valor en diferentes partes del código. Además, si se quiere cambiar el valor de una variable, se puede hacer de forma muy sencilla, sin tener que cambiar el valor en cada parte del código donde se haya usado.

Por ejemplo, si modificamos la variable `$master-site-color` a un color verde, el programa se vería así:

![01.variables-color-changed.png](../images/module-01/01-variables/01-variables-color-changed.png)


<br><hr><br>


### Valores por defecto

Aunque aún no se ha hablado de ellos, en este y el siguiente apartado se van a usar los ***mixins***. Los mixins son una especie de funciones que se pueden usar en SCSS de las cuales hablaremos más adelante. No es importante saber qué son o cómo funcionan por ahora.

Podemos crear valores por defecto de la siguiente manera:

``` scss
@mixin heading-feature-styling {
    $feature-color: DarkRed !default;
    color: $feature-color;
}

@mixin section-feature-styling {
    $feature-color: DarkRed !default;
    background-color: $feature-color;
    padding: 42px;
    color: $off-white;
}
```

<br>

Así es como se vería:

![00-variables.png](../images/module-01/01-variables/00-variables.png)

<br>

Si la variable `$feature-color` no se define (como si fuera una variable más), se usará el valor especificado antes de `!default`. Pero si se crea una variable con ese nombre, se usará ese valor de la variable:

``` scss
/* VARIABLES */
$feature-color: darkgreen;

/* MIXINS */
@mixin heading-feature-styling {
    $feature-color: DarkRed !default;
    color: $feature-color;
}

@mixin section-feature-styling {
    $feature-color: DarkRed !default;
    background-color: $feature-color;
    padding: 42px;
    color: $off-white;
}
```

<br>

En este caso, así es como quedaría:

![01-variables-color-changed.png](../images/module-01/01-variables/01-variables-color-changed.png)


<br><hr><br>


### Anidación en SCSS

Para anidar elementos en CSS se podía utilizar `<` para indicar que un elemento se encontraba dentro de otro.

Con SCSS se vuelve todo mucho más sencillo. Ya se ha visto en los ejemplos anteriores la sintáxis para anidar elementos, o indicar que uno se encuentra dentro del otro. Para ello, basta con escribir y dar estilo al elemento dentro de su contenedor:

``` scss
.page-wrapper {
    padding: 21px;

    .featured {
        @include heading-feature-styling;
    }

    .page-content{
        @include section-feature-styling;

        .container {
            font-family: 'Courier New', Courier, monospace;
        }
    }
}
```

<br>

En este ejemplo, podemos entender que el elemento `.container` se encuentra dentro del elemento `.page-content`, que a su vez se encuentra dentro del elemento `.page-wrapper`.

`.page-content` está dentro de `.page-wrapper`, pero `.featured` también, lo que significa que estos dos elementos se encuentran dentro de un mismo contenedor: `.page-wrapper`.

<br>

* **Anidación con pseudoclase**

De nuevo, en CSS la forma de dar estilo a un elemento con una pseudoclase era la de volver a definir el elemento en otro bloque de código, pero con la pseudoclase añadida.

Ahora, con SCSS, se puede anidar el elemento con la pseudoclase, de la siguiente manera:

``` scss
.subheading a {
    color: cornflowerblue;
    text-decoration: none;

    &:hover {
        color: darkolivegreen;
        text-decoration: underline;
    }
}
```

<br>

El equivalente CSS sería el siguiente:

``` css
.subheading a {
    color: cornflowerblue;
    text-decoration: none;
}

.subheading a:hover {
    color: darkolivegreen;
    text-decoration: underline;
}
```

<br>

En este caso, refetir la referencia al elemento dos veces no es muy tedioso porque no ha habido que especificar sus contenedores, pero sigue siendo una forma de repetirse de forma innecesaria. Es mucho más rápido aplicar SCSS.


<br><hr>
<hr><br>


## Mixins

Son una especie de funciones que pueden ser "llamadas". Son muy útiles para aplicar los mismos estilos en diferentes elementos, o simplemente para ayudar a organizar los estilos. Para definir un *"mixin"*, se usa la sintaxis `@mixin`.

En este ejemplo, vamos a crear los siguientes:

``` scss
@mixin heading-feature-styling {
    color: $master-site-color;
}

@mixin section-feature-styling {
    background-color: $master-site-color;
    padding: 42px;
    color: $off-white;
}
```

<br>

Esto haría que el programa se viera modificado, ***¿por qué? ¿Qué es lo que falta?***

Ahora, nos queda indicar qué elementos deben *"coger"* las propiedades definidas en dichos mixins. Para ello, se usa la palabra reservada `@include`:

``` scss
.page-wrapper {
    padding: 21px;

    .featured {
        @include heading-feature-styling;
    }

    .page-content{
        @include section-feature-styling;

        .container {
            font-family: 'Courier New', Courier, monospace;
        }
    }
}
```

<br>

Como se puede observar, el resultado no se vería modificado:

![01-variables-color-changed.png](../images/module-01/01-variables/01-variables-color-changed.png)


<br><hr><br>


### Mixins con argumentos

En el ejemplo de arriba hemos usado ***mixins*** sin argumentos, lo que significa que son *estáticos*, es decir, iguales para todos. Pero, ¿qué pasa si queremos que haya elementos compartiendo estilo con pequeñas diferencias? Para ello, se pueden usar argumentos en los ***mixins***, como si se tratara de funciones:

``` scss
@mixin featured($link-color: black) {
    color: Tomato;
    
    .subheading a {
        color: $link-color;
        text-decoration: none;

        &:hover {
            color: $link-color;
            text-decoration: underline;
        }
    }
}
```

<br>

El ***mixin*** creado tiene una variable, `$link-color`, que por defecto tiene el valor `black`. Si no se le pasa ningún argumento, se usará el valor por defecto. Pero si se le pasa un argumento, se usará ese valor.

No es necesario indicar que `$link-color` tenga un valor concreto al declarar el ***mixin***, podría no ponerse ninguno y enconces habría que especificar siempre un color al llamar al ***mixin***.

<br>

Como en este caso hemos especificado un valor por defecto, podemos realizar lo siguiente:

``` scss
.page-wrapper {
    /* some code */

    .featured {
        @include featured; // no se pasa argumento -> usa el valor por defecto
    }

    .page-content{
        /* some code */

        .container {
            /* some code */

            .sidebar {
                /* some code */
                @include featured(mintcream); // usa el valor "mintcream"
            }
        }
    }
}
```

<br>

El resultado sería el siguiente, donde se puede ver que cada link debajo del "About us" tiene un color distinto:

![00-mixin-with-arguments.png](../images/module-01/02-mixins/00-mixin-with-arguments.png)


<br><hr><br>


### Mixins con condicionales

Se pueden crear sentencias condicionales dentro de los ***mixins***. Las sentencias condicionales (`if`, `else if` y `else`) pueden servir para definir distintos tipos de escenarios. Para definirlas, se debe escribir el caracter `@` antes de cada una de ellas.

He aquí un ejemplo:

``` scss
@mixin featured($bg-color: 'dark') {
    @if $bg-color == 'light' {
        color: Tomato;
    } @else if $bg-color == 'dark' {
        color: blue;
    } @else {
        color: red;
    }
    
    /* some other code */
}
```

<br>

Al igual que en el apartado anterior vimos cómo pasar parámetros a un ***mixin***, en este caso las llamadas al ***mixin*** funcionan de la misma forma:

``` scss
.page-wrapper {
    /* some code */

    .featured {
        @include featured('light');
    }

    .page-content{
        /* some code */

        .container {
            /* some code */

            .sidebar {
                /* some code */

                @include featured('grey');
            }
        }
    }
}
```

<br>

Lo que va a ocurrir es que el `@include` de la clase `.featured` entrará en el primer `@if` tomando el color *tomato*. El `@include` de la clase `.sidebar` entrará en la tercera opción (`@else`) tomando el color *red* porque no encaja con ninguna de las opciones anteriores.

Si no se le hubiera indicado ningún valor, hubiera entrado en la sentencia `@else if` porque tendría ese valor por defecto.

Este es el resultado:

![01-mixin-with-conditional.png](../images/module-01/02-mixins/01-mixin-with-conditional.png)


<br><hr>
<hr><br>


## Crear clases dinámicas

En este apartado se va a hablar de cómo crear clases dinámicas utilizando un ejemplo muy sencillo:

Imagina que se tiene este código HTML:

``` html
<body>
    <div class="car-maserati"></div>
    <div class="car-tesla"></div>
    <div class="car-porsche"></div>
</body>
```

Y se desea utilizar 3 imágenes diferentes para cada uno de los `div`. El estilo de cada elemento va a ser el mismo, siendo la imagen de fondo la única diferencia.

***¿Qué se puede hacer?***

Vamos a aprender a crear clases dinámicas para escribir únicamente un bloque de código que se aplique a los tres elementos gracias a modificar su clase.

Para ello, vamos a seguir los siguientes pasos:

1. Crear una lisa con el nombre (sin extensión) de cada imagen que se va a utilizar.
2. Utilizar la directiva `each` para recorrer la lista y crear una clase dinámica para cada elemento.

Para crear las clases dinámicas, se va a utilizar la interpolación de strings. Esto permite crear una cadena de texto que se modifique utilizando variables.


<br><hr><br>


### Listas

Para crear una lista en SCSS, se realiza lo siguiente:

``` scss
$cars: 'maserati', 'tesla', 'porsche';
```

<br>

Como se puede ver, es una variable, cuya sintaxis es la misma que la de cualquier otra variable. La diferencia es que en lugar de contener un valor, contiene una lista de valores.


<br><hr><br>


### Directiva each

La directiva `each` permite recorrer una lista y ejecutar un bloque de código para cada uno de los elementos de la lista.

La sintaxis es la siguiente:

``` scss
@each $item in $list {
    /* some code */
}
```

<br>

En nuestro ejemplo, vamor a realizar lo siguiente:

``` scss
@each $car-name in $cars {
    .car-#{$car-name} {
        /* some code */
    }
}
```

<br>

Con estas líneas de código, se creará una clase dinámica para cada elemento de la lista. El nombre de la clase será el nombre del elemento de la lista precedido por la palabra `car-`. Lo que daría como resultado las mismas clases que las que hemos visto en el [código HTML](#crear-clases-dinámicas).

Dentro de este bloque utilizaremos la interpolación de strings para crear las clases dinámicas.


<br><hr><br>


### Interpolación de Strings

La interpolación de strings permite crear una cadena de texto que se modifique utilizando variables.

Para introducir una variable dentro de un string se utiliza el caracter `#` seguido del nombre de la variable.

``` scss
#{$variable}
```

<br>

Siguiendo nuestro ejemplo, el código sería el siguiente:

``` scss
.car-#{$car-name} {
    background-image: url('../../images/module-01/03/#{$car-name}.jpg');
    background-repeat: no-repeat;
    height: 300px;
    width: 500px;
    object-fit: fill;
    float: left;
}
```

<br>

Con la línea de código mostrada aquí:

``` scss
background-image: url('../../images/module-01/03/#{$car-name}.jpg');
```

<br>

Se está creando una cadena de texto que contiene la ruta de la imagen. El nombre de la imagen se obtiene de la variable `$car-name` que se está interpolando en el string.

<br>

El código final completo sería el siguiente:

``` scss
$cars: 'maserati', 'tesla', 'porsche';

@each $car-name in $cars {
    .car-#{$car-name} {
        background-image: url('../../images/module-01/03/#{$car-name}.jpg');
        background-repeat: no-repeat;
        height: 300px;
        width: 500px;
        object-fit: fill;
        float: left;
    }
}
```

<br>

El resultado sería el siguiente:

![00_resultado.png](../images/module-01/03-dinamizar/00_resultado.png)


<br><hr>
<hr><br>


## Import

La directiva `@import` permite importar archivos SCSS dentro de otros archivos SCSS. Esto permite dividir el código en archivos más pequeños y reutilizar código.

Por lo general, se usa un archivo principal que importa todos los demás archivos.

Esto requiere **tener cuidado con el orden de importación** de los archivos. Como recordatorio, SCSS viene de Sassy Cascading Style Sheets, lo que significa que el orden de importación de los archivos es importante, ya que unos elementos podrían modificar a otros.

<br>

Se ha de saber también, que `@import` es una directiva un poco antigua. En la actualidad, se recomienda utilizar `@use` para importar archivos SCSS.
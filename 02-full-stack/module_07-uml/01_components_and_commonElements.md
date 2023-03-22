# COMPONENTES Y ELEMENTOS COMUNES

<div id="indice"></div>

* [Frames](#frames)
* [Classifiers](#classifiers)
* [Comments](#comments)
* [Dependencies](#dependencies)
* [Features or Properties](#features-or-properties)

<br>

[<< INTRODUCCIÓN](./00_intro.md#introducción-a-uml) | [STRUCTURAL DIAGRAMS >>](./02_structuralDiagrams.md#structural-diagrams)

<br><hr>
<hr><br>


## Frames

<sub>[Volver al índice](#indice) | [Classifiers >>](#classifiers)</sub>

### Qué es un Frame

Los `frames` son elementos que ayudan a encapsular los `view components`, principalmente, se encargan de ofrecer el contexto de los elementos que se encuentran dentro de ellos.


<br>


### Cómo se representa

Para representar los `frames` se utilizan `headings`, donde hay una notación descriptiva sobre cuál es el modelo.


<br>


### Por qué se usa

Se usa para entender de froma rápida y sencilla el modelo que se está representando.


<br><hr><br>


### Diagram mapping

* **act** = activity diagram
* **class** = class diagram
* **cmp** = component diagram
* **dep** = deployment diagram
* **sd** = interaction (*sequence*) diagram
* **pkg** = package diagram
* **stm** = state machine diagram
* **uc** = use case diagram

<br>

Ejemplo de un diagrama de `use case` con un `frame`:

<div align="center">

![uc-diagram](./media/basics/uc-diagram.png)

</div>

<br>

Sabemos que se trata de ese tipo de diagrama debido a la notación que se encuentra en la esquina superior izquierda de la imagen, donde además, hay un pequeño `heading` descriptivo.


<br><hr>
<hr><br>


## Classifiers

<sub>[<< Frames](#frames) | [Volver al índice](#indice) | [Stereotypes >>](#stereotypes)</sub>

### Qué es un Classifier

Nos permiten identificar los componentes. Son bastante abstractos, donde se clasifican los componentes.


<br><hr><br>


### Usado por

Son usados por prácticamente todos los elementos de UML:

* **Class**
* **Interface**
* **Association**
* **Data Type**
* **Actor**
* **Use Case**
* **Artifact**
* **Component**
* **Signal**

<br>

Ejemplo de un diagrama de `use case` con un `classifier`:

<div align="center">

![uc-diagram](./media/structural-diagrams/class-diagram.png)

</div>

<br>

En este caso, el `Topic` es el nombre del `classifier`, que es de una clase.


<br><hr>
<hr><br>


## Comments

<sub>[<< Stereotypes](#stereotypes) | [Volver al índice](#indice) | [Dependencies >>](#dependencies)</sub>

También conocidos como `notes`, son elementos que nos permiten agregar información adicional a los diagramas. Se pueden agregar en cualquier parte del diagrama, y se pueden agregar varios.


<br>


### Cómo se representa

Se representan con un rectángulo con una línea punteada.


<br>


### Por qué se usa

Se usa para agregar información adicional a los diagramas.


<br><hr><br>


### Ejemplo de comentarios

Si volvemos a usar la imagen vista en el apartado de [classifiers](#usado-por), veremos que hay varios `comments` que nos permiten agregar información adicional a los diagramas.

Los comentarios, como ya hemos mencionado, son esos rectángulos con una línea punteada, y se pueden agregar varios.

<div align="center">

![uc-diagram](./media/structural-diagrams/class-diagram.png)

</div>

<br>


<br><hr>
<hr><br>


## Dependencies

<sub>[<< Comments](#comments) | [Volver al índice](#indice) | [Features or Properties >>](#features-or-properties)</sub>

### Qué es una Dependency

Sirven para explicar cómo de necesario es un elemento para otro. Son muy útiles para explicar la relación entre los elementos.


<br>


### Cómo se representa

Se representan con una línea punteada con una flecha.


<br>


### Por qué se usa

Se usa para explicar la relación entre los elementos. Ayudan a prevenir errores.


<br><hr><br>


### Ejemplo de dependencias

En esta imagen se ve que hay una dependencia llamada `SongRequest` y que necesita de `SpotifyAPI` para funcionar.

Si se elimina `SpotifyAPI`, `SongRequest` dejará de funcionar.

<div align="center">

![uc-diagram](./media/basics/dependency-diagram.png)

</div>

<br>


<br><hr>
<hr><br>


## Features or Properties

<sub>[<< Dependencies](#dependencies) | [Volver al índice](#indice)</sub>

### Qué es una Feature o Property

Son elementos que nos permiten agregar información adicional a los elementos.

Ayudan a describir los elementos. Siguen una sintaxis específica (*naming convention*).

<div align="center">

![feature-diagram](./media/basics/features-diagram.png)

</div>

<br>


<br><hr>
<hr><br>

[<< INTRODUCCIÓN](./00_intro.md#introducción-a-uml) | [STRUCTURAL DIAGRAMS >>](./02_structuralDiagrams.md#structural-diagrams)

<style>
    /* formatear cualquier imagen que en el 'alt' tenga el valor
    de '-diagram' */
    img[alt$="-diagram"] {
        width: 75%;
        max-width: 600px;
    }
</style>
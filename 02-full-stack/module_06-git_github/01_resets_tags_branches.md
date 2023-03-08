# Conceptos de flujo de trabajo

En la sesión anterior se habló por encima de algunos comandos de git. En esta sesión se profundizará en algunos de ellos, y se verán otros nuevos.

<p id="indice">He aquí un pequeño índice de lo que se va hablando durante el curso:</p>

* [Resets](#resets)
* [Tags](#tags)
* [Branches](#branches)
    * [Merge](#merge)
    * [Merche con conflicto](#merge-con-conflicto)
* [Stash](#stash)

<br>

[<< #00 - MANUAL BÁSICO](./00_git_basics.md#manual-básico-de-git) | [#02 - GITHUB >>](./02_github.md)


<br><hr>
<hr><br>


## Resets

Hay ocasiones en las que se quiere retroceder en los cambios que se han realizado a lo largo de las versiones del programa, eliminando definitivamente aquellos cambios que se han realizado.

Si se desea volver a alguna versión anterior, pero no se quiere perder el trabajo realizado en las versiones intermedias, se puede utilizar el comando `git reset`, o `git reset --soft` (que es lo mismo que `git reset`). Con esto, se borrarían los commit no deseados, pero podríamos abrir los archivos y ver que ahí sí están esos cambios realizados, lo que permitiría guardarlos, modificarlos, eliminarlos, etc.

Si, por el contrario, se quiere eliminar el registro de commits intermedios desde donde estamos hasta la versión deseada, y también eliminar los cambios realizados en los archivos, se puede utilizar `git reset --hard`.

<br>

Esto es una gran idea pero, ***¿qué ocurre si se hace un `git reset --hard` por error?***

Para ello, se debe saber que **git guarda un registro completo de las interacciones** que se han realizado, y que se puede acceder a ellos mediante el comando `git reflog`.

Si conocemos el ID del commit al que queremos volver, se puede volver a dicho commit repitiendo el comando `git reset --hard` y añadiendo el ID del commit al que se quiere volver.

<br><hr><br>

**Ejemplo:**

```bash
git reset --hard 033654f
```

<br>

Con esta línea, se vuelve al commit con ID `033654f`. Se elimina el registro de commits desde el commit en el que estábamos hasta este, y se eliminan los cambios realizados en los archivos. Es como si nunca hubiéramos hecho esos commits ni esos cambios.

<br>

Si ahora queremos retroceder y volver a recuperar los commit que se acaban de eliminar, se usa:

```bash
git reflog
```

<br>

Aquí se muestra una lista con el registro completo de commits. Copiamos el hash (ID) del commit al que queremos volver, y ejecutamos:

```bash
git reset --hard fab087b
```

<br>

Con esto, se vuelve al commit con ID `fab087b`, y se recuperan los commits eliminados. Estamos de nuevo en el mismo punto que antes de hacer el primer `git reset --hard`.


<br><hr>
<hr><br>


## Tags

Los tags son etiquetas que se pueden añadir a los commits. Se pueden añadir tags a commits antiguos, o a commits nuevos. Se pueden añadir tags tanto a commits que no son el último, como a commits que sí lo son.

Habitualmente los tags se utilizan en puntos importantes. Aquellos de los cuales se desea guardar una referencia. Por ejemplo, cuando se lanza una versión estable del programa, se puede añadir un tag a ese commit, para poder volver a él en el futuro.

Sirven para poder verlos visualmente en el historial de commits, y también para poder acceder a ellos mediante el comando `git checkout`.

<br>

Por buena práctica, los tags deben escribirse en minúsculas, y separando palabras con guiones bajos.

<br>

Para añadir un tag al commit actual, se usa:

```bash
git tag <nombre_del_tag>
```

<br>

Podemos ver todos los tags que hay en el repositorio con:

```bash
git tag
```

<br>

Ahora que tenemos un tag, podemos movernos a él con:

```bash
git checkout <nombre_del_tag>
```


<br><hr>
<hr><br>


## Branches

Los branches son ramas de desarrollo. Se pueden crear tantas ramas como se quiera, y se pueden crear tantos commits como se quiera en cada rama.

Son muy útiles para trabajar en paralelo en distintas partes del programa. O también para solucionar bugs en el programa sin tener que modificar el código principal.


* **Ver las ramas que hay en el repositorio:**

```bash
git branch
```

<br>

* **Para crear una rama se usa:**

```bash
git branch <nombre_de_la_rama>
```

<br>

* Podemos **crear una rama y movernos** directamente a ella con:

```bash
git checkout -b <nombre_de_la_rama>
```

<br>

* **Para movernos a una rama existente** se usa:

```bash
git switch <nombre_de_la_rama>
```

O bien:

```bash
git checkout <nombre_de_la_rama>
```


<br><hr><br>


### Merge

Si en la rama ***main*** se realiza algún cambio, y luego se vuelve a la rama ***rama1***, se verá que los cambios realizados en ***main*** no se han realizado en ***rama1***. Esto es porque ***rama1*** es una rama independiente de ***main***.

Para obtener de vuelta los cambios realizados en ***main*** dentro de ***rama1***, se debe hacer un ***merge***:

```bash
git merge main
```

<br><hr><br>


### Merge con conflicto

En ocasiones, en ambas ramas se toca la misma línea de código, y git no sabe qué cambios se deben conservar. En este caso, se dice que hay un ***conflicto***, y se debe resolver manualmente.

Una vez resuelto el conflicto, se deben añadir los cambios y realizar el respectivo commit:

```bash
git add .
git commit -m "Mensaje del commit"
```


<br><hr>
<hr><br>


## Stash

Habrá veces en las que necesitemos guardar los cambios que hemos realizado en el repositorio, pero que no queremos realizar un commit.

> Por ejemplo, si estamos trabajando en una rama, y nos encontramos con un bug en la rama ***main***, y queremos solucionarlo sin perder los cambios que hemos realizado en la rama en la que estamos trabajando.

<br>

**Siempre que queramos guardar los cambios sin realizar commits**, bien sea porque nuestro programa tiene errores, para poder regresar más tarde, o el motivo que sea, podemos guardar los cambios sin hacer commit con:

```bash
git stash
```

<br>

Si hemos guardado con `stash`, podemos ver los cambios guardados con:

```bash
git stash list
```

<br>

Para recuperar los cambios guardados, se usa:

```bash
git stash pop
```

<br>

Si no queremos recuperar los cambios guardados en la última ejecución de `git stash`, se puede eliminar lo guardado con:

```bash
git stash drop
```
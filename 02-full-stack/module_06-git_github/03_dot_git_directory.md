# Directorio .git

## Explicación general

### hooks

Los hooks son scripts que se ejecutan en momentos específicos del ciclo de vida de un repositorio. Por ejemplo, se puede ejecutar un script antes de que se haga un commit, o antes de que se haga un push.

Pueden ser útiles para automatizar tareas, como por ejemplo, ejecutar tests antes de hacer un commit, o dar permisos de escritura a un archivo antes de hacer un push.


<br><hr><br>


### logs

Es el directorio en el que se guardan los logs de los commits. Cada vez que se hace un commit, se guarda la información del commit en un archivo dentro de este directorio.


<br><hr><br>


### refs

En este directorio se guardan tanto el commit actual como los tags y branches que hay en el repositorio.


<br><hr><br>


### COMMIT_EDITMSG

Es un archivo que se crea o actualiza cuando se hace un commit. Guarda el último mensaje de commit que se escribió. Puede editarse para cambiar el mensaje de commit.
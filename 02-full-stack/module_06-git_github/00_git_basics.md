# Manual básico de Git

Para saber más acerca de Git, lo primero que se debe hacer es acceder a la [página oficial de Git](https://git-scm.com/), que es el mejor lugar para documentarse sobre su uso, instalación, etc.

En la página se encuentran varios recursos:

* [Pro Git](https://git-scm.com/book/en/v2): libro totalmente gratuito con todo lo que hay que saber sobre trabajar con Git.
* [Información](https://git-scm.com/about) y [documentación](https://git-scm.com/doc) sobre Git.
* [Descargas](https://git-scm.com/downloads) para todos los sistemas operativos, donde se puede descargar la versión más actualizada o versiones anteriores.
* Link de la [comunidad](https://git-scm.com/community) para mantener el contacto o informar de cualquier problema.


<br><hr><br>


<p id="indice">A continuación, se muestra una guía de los temas a tratar:<p>

* [Instalar Git](#instalar-git)
    * [Comprobar las versiones](#comprobar-las-versiones)
* [Comandos básicos de la terminal](#comandos-básicos-de-la-terminal)
* [Configurar Git](#configurar-git)
* [Crear un repositorio](#crear-un-repositorio)
    * [Añadir archivos al repositorio](#añadir-archivos-al-repositorio)
    * [Añadir archivos nuevos](#añadir-archivos-nuevos)
    * [Deshacer cambios](#deshacer-cambios)
* [Ver los commits](#ver-los-commits)
    * [Ver diferencias](#ver-diferencias)
* [Alias](#alias)
* [Ignorar archivos](#ignorar-archivos)
* [Moverse entre commits](#moverse-entre-commits)

<br>

[#01 - RESETS, TAGS Y BRANCHES >>](./01_resets_tags_branches.md#conceptos-de-flujo-de-trabajo)


<br><hr>
<hr><br>


## Instalar Git

<sub>[Volver al índice](#indice) | [Comprobar versiones >>](#comprobar-las-versiones)</sub>

Git es un sistema de control de versiones.

Para instalarlo accederemos a la parte de [descargas](https://git-scm.com/downloads) de la página oficial de Git y se seguirán los pasos para el sistema operativo que se esté utilizando.

En mi caso, estoy utilizando Windows, por lo que para realizar la instalación, podría descargar el instalador de Git desde [aquí](https://git-scm.com/download/win), o escribir en la terminal el comando mostrado:

```
winget install --id Git.Git -e --source winget
```


<br><hr><br>


### Comprobar las versiones

<sub>[<< Instalar Git](#instalar-git) | [Volver al índice](#indice) | [Comandos de terminal >>](#comandos-básicos-de-la-terminal)</sub>

Una vez instalado Git, independientemente del sistema operativo con el que se trabaje, se puede comprobar que se ha instalado correctamente escribiendo en la terminal el comando:

``` bash
git --version
```

O bien su forma reducida:

``` bash
git -v
```


<br><hr>
<hr><br>


## Comandos básicos de la terminal

<sub>[<< Instalar Git](#instalar-git) | [Volver al ínidce](#indice) | [Configurar Git >>](#configurar-git)</sub>

Aunque aprender a usar la terminal no es parte del estudio de Git, es muy recomendable conocer al menos unos comandos básicos para facilitar el trabajo.

* **Mostrar un listado de los archivos y carpetas de la carpeta actual:**

``` bash
ls
```

<br>

* **Moverse a otro directorio:** (se puede utilizar el *tabulador* para autocompletar)

``` bash
cd <nombre_carpeta>
```

<br>

* **Volver al directorio anterior:**

``` bash
cd ..
```

<br>

* **Saber en qué directorio nos encontramos:**

``` bash
pwd
```

<br>

* **Crear una carpeta:** (la carpeta se crea en el directorio actual)[^1]

``` bash
mkdir <nombre_carpeta>
```

<br>

* **Crear un archivo vacío:** (el archivo se crea en el directorio actual)

``` bash
touch <nombre_archivo>
```

<br>

* **Abrir Visual Studio Code:** (si se ha instalado en el sistema)

``` bash
code .
```

<br>

* **Limpiar la consola:**

``` bash
clear
```

O bien:

``` bash
cls
```


<br><hr>
<hr><br>


## Configurar Git

<sub>[<< Comandos de terminal](#comandos-básicos-de-la-terminal) | [Volver al índice](#indice) | [Crear repositorios >>](#crear-un-repositorio)</sub>

Para usar Git será necesario configurar el nombre y el correo electrónico que se utilizarán para identificar al usuario que realiza los cambios en el repositorio. Estos dos son datos mínimos para la configuración.

Para realizar la configuración:

``` bash
git config --global user.name "nombre_usuario"
git config --global user.email "correo_electronico"
```

<br>

Al indicar que es una configuración global, se aplicará a todos los repositorios que se creen en el sistema. Es decir, cualquier persona que accediera al equipo con mi usuario, usaría Git con mi nombre y mi correo electrónico.

<br>

Todos los datos de configuración se encuentran en el archivo `.gitconfig` que se encuentra en el directorio `C:\Users\<nombre_usuario>`.

Desde ahí se pueden ver y modificar los valores de confirguración.


<br><hr>
<hr><br>


## Crear un repositorio

<sub>[<< Configurar Git](#configurar-git) | [Volver al índice](#indice) | [Añadir archivos >>](#añadir-archivos-al-repositorio)</sub>

Para trabajar con Git, se debe crear un repositorio local, que es una carpeta que contiene todos los archivos y carpetas del proyecto, y que se encuentra controlada por Git.

Para crear dicho repositorio, accedemos al directorio donde se quiere guardar todo lo relacionado al proyecto, y se escribe lo siguiente:

``` bash
git init
```

<br>

El lugar donde se encuentre el archivo oculto `.git` significa que se trabaja con Git.

Tras ejecutar el comando mostrado arriba y crearse el repositorio, se verá que el directorio, además de indicar la ruta en la que nos encontramos, muestra la palabra "master". Esto significa que estamos en la rama principal del repositorio.

Se puede cambiar el nombre de la rama principal con el siguiente comando:

``` bash
git branch -m <name>
```

<br>

Incluso se puede modificar el valor por defecto para que siempre cree los repositorios con un nombre de rama principal específico:

``` bash
git config --global init.defaultBranch <name>
```

<br>

Al igual que el resto de configuraciones, este valor se puede ver y modificar en el archivo `.gitconfig`.


<br><hr><br>


### Añadir archivos al repositorio

<sub>[<< Crear un repositorio](#crear-un-repositorio) | [Volver al índice](#indice) | [Añadir nuevos >>](#añadir-archivos-nuevos)</sub>

La forma de entender el modo de trabajar de Git es imaginarse que realiza fotografías de cómo se encuentran todos los archivos del directorio actualmente. Estas fotografías se llaman ***commits***, pero antes, vamos a ver cómo saber en qué estado nos encontramos.

Para comprobar el estado del repositorio, se puede utilizar el comando:

``` bash
git status
```

<br>

Este comando nos mostrará el estado de los archivos del repositorio, si están siendo rastreados por Git o no, si han sido modificados, si se han creado nuevos archivos, si han sido eliminados, etc.

Al crear un archivo, este se encuentra en un estado de ***untracked***, es decir, no está siendo rastreado por Git. Para que Git empiece a rastrearlo, se debe añadir al ***staging area***, que es un área intermedia donde se almacenan los cambios que se van a realizar en el repositorio.

Para añadir un archivo al ***staging area***, se utiliza el comando:

``` bash
git add <nombre_archivo>
```

Si se tienen varios archivos y quieren añadirse todos al ***staging area***, se puede utilizar el comando mostrado a continuación:

``` bash
git add .
```

<br>

Si se vuelve a usar el comando `git status`, se verá que el archivo ya no está en estado de ***untracked***, sino que está en estado de ***staged***, es decir, que está listo para ser añadido al repositorio.

Ahora tenemos los archivos deseados para realizar una fotografía del estado actual del repositorio. Para hacer la fotografía, se utiliza el comando:

``` bash
git commit -m "mensaje"
```

<br>

Ahora, tenemos la primera "fotografía" del repositorio, y se encuentra en la rama en la que estábamos. Si se vuelve a escribir `git status`, se verá que no hay nada que añadir al ***staging area***, ya que todos los archivos están en estado de ***committed***, es decir, que ya están en el repositorio.


<br><hr><br>


### Añadir archivos nuevos

<sub>[<< Crear repositorio](#crear-un-repositorio) | [Volver al índice](#indice) | [Deshacer cambios >>](#deshacer-cambios)</sub>

Si se crea un archivo nuevo, se encuentra en estado de ***untracked***, y para añadirlo al repositorio, se debe añadir al ***staging area*** y realizar un commit.

Es decir, se deberían repetir los pasos descritos desde el punto [Añadir archivos al repositorio](#añadir-archivos-al-repositorio).


<br><hr><br>


### Deshacer cambios

<sub>[<< Crear un repositorio](#crear-un-repositorio) | [Volver al índice](#indice) | [Ver commits >>](#ver-los-commits)</sub>

En ocasiones se puede cometer un error y se quieren deshacer los cambios realizados en uno o varios archivos.

Si, dentro de un archivo creado donde tenemos todo al día, modificáramos algo, hubiéramos ido guardando (sin hacer `git add` ni `git commit`) y quisiéramos volver atrás a donde teníamos todo antes de modificar nada, se puede utilizar el comando:

``` bash
git checkout <nombre_archivo>
```

<br>

`git checkout` es un comando que se utiliza para moverse entre ramas, pero también se puede utilizar para deshacer cambios en archivos.[^2]

Lo que ha ocurrido es que se han deshecho las modificaciones en ese archivo, y ahora está igual que como estaba en el último commit.

<br>

Si se hubiera añadido el archivo previamente al ***staging area*** y se quisiera *deshacer* el `git add`, podría usarse lo siguiente:

``` bash
git restore --staged <nombre_archivo>
```

O bien:

``` bash
git reset HEAD
```


<br><hr>
<hr><br>


## Ver los commits

<sub>[<< Crear repositorio](#crear-un-repositorio) | [Volver al índice](#indice) | [Ver diferencias >>](#ver-diferencias)</sub>

Para ver los commits que se han realizado, existen muchísimas opciones. Para hacerlo de la forma más simple, se puede utilizar el comando:

``` bash
git log
```

<br>

Este comando muestra todos los commits que se han realizado, con su identificador (hash), autor, fecha, mensaje, etc.

Se pueden ver los commits de otras muchas formas, he aquí unos ejemplos:

* **Mostrar los commits más recientes:** (mostraríamos los últimos 3 commits)

``` bash
git log -3
```

<br>

* **Filtrar por autor o *committer*:**

``` bash
git log --author <name>
git log --committer <name>
```

<br>

* **Filtrar por fechas:**

``` bash
git log --before <date>
git log --after <date>
```

Si se quisiera usar un **rango de fechas**:

``` bash
git log --after <date> --before <date>
```

<br>

* **Ver las diferencias en cada commit:**

``` bash
git log -p
```

Se puede ver también un resumen de las diferencias:

``` bash
git log --stat
```

<br>

* **Mostrar los commits en una sola línea:**

``` bash
git log --oneline
```

<br>

* **Mostrar los commits en un gráfico:**

``` bash
git log --graph
```

<br>

* **Dar formato a la salida:**

``` bash
git log --pretty=format:"<options>"
```


<br><hr><br>


### Ver diferencias

<sub>[<< Ver commits](#ver-los-commits) | [Volver al índice](#indice) | [Alias >>](#alias)</sub>

Se pueden ver también únicamente las diferencias entre el commit que queramos y lo que tenemos ahora mismo. O entre lo que se encuentra en el ***staging area*** y lo que tenemos ahora.

Para ello, podemos usar:

``` bash
git diff
```

O bien:

``` bash
git diff --staged
```

<br>

* Si únicamente se escribe `git diff`, se compara el último commit con lo que quiera que tengamos modificado actualmente.
* Si hacemos `git diff --staged`, se compara lo que está en el ***staging area*** con lo que tenemos actualmente.


<br><hr>
<hr><br>


## Alias

<sub>[<< Ver commits](#ver-los-commits) | [Volver al índice](#indice) | [Ignorar archivos >>](#ignorar-archivos)</sub>

Ya hemos visto como mostrar los commits, sin embargo, en ocasiones se puede querer mostrar los commits de una forma más personalizada, lo que puede suponer tener que escribir una línea de código relativamente larga una y otra vez.

Para evitar esto, se dispone de los alias.

Vamos a explicarlos con un ejemplo. Supongamos que queremos visualizar los commits de la siguiente manera:

``` bash
git log --graph --pretty=format:'%C(yellow)%h%Creset - %s %Cgreen(%cd)%Creset %Cred%d%Creset %C(bold blue)<%cn>%Creset' --date=format:'%d/%m/%Y - %H:%M'
```

<br>

La mostrada, no es una forma muy cómoda de escribir el formato de visualización de los commits, sobre todo si se desea utilizar a menudo. Para solucionarlo, creamos un ***alias*** que *guarde* dicho log en una especie de variable muy fácil de escribir y recordar.

Para crear un alias, se utiliza el comando:

``` bash
git config --global alias.<nombre_alias> "<comando>"
```

<br>

En nuestro caso, el alias podría ser:

``` bash
git config --global alias.mylog "log --graph --pretty=format:'%C(yellow)%h%Creset - %s %Cgreen(%cd)%Creset %Cred%d%Creset %C(bold blue)<%cn>%Creset' --date=format:'%d/%m/%Y - %H:%M'"
```

<br>

Ahora, para mostrar los commits con el mismo formato, bastaría con escribir:

``` bash
git mylog
```

<br>

Al igual que el resto de configuraciones, los alias también se encuentran dentro del archivo `.gitconfig`.


<br><hr>
<hr><br>


## Ignorar archivos

<sub>[<< Alias](#alias) | [Volver al índice](#indice) | [Moverse entre commits >>](#moverse-entre-commits)</sub>

En ocasiones, se puede querer ignorar algunos archivos, ya sea porque no se quieren subir al repositorio, porque son archivos generados automáticamente, o el motivo que sea.

Para ello, se puede crear un archivo `.gitignore` en el directorio raíz del repositorio, y dentro de él, se pueden especificar los archivos que se quieran ignorar.

Una vez creado el archivo y haber añadido dichos documentos a ignorar teniendo en cuenta la [sintaxis de Git para .gitignore](https://git-scm.com/docs/gitignore), se debe añadir el archivo al ***staging area*** y hacer un commit.

``` bash
git add .gitignore
git commit -m "Added .gitignore"
```


<br><hr>
<hr><br>


## Moverse entre commits

<sub>[<< Ignorar archivos](#ignorar-archivos) | [Volver al índice](#indice)</sub>

Podemos movernos entre diferentes commits utilizando los ***hash*** de los mismos.

Ya hemos visto cómo ver y filtrar los commits que queramos. Haciendo uso de ello, podemos copiar el ***hash*** del commit que queramos y usarlo para movernos a dicho commit.[^3]

``` bash
git checkout <hash>
```

<br>

Al hacer esto, nuestro directorio de trabajo se verá modificado (siempre que el cambio de commit implique algún cambio en los archivos). Es decir, veremos nuestro entorno como exactamente como estaba en el commit al que nos hemos movido.

Si hicieramos `git log` ahora, veríamos que no están los commits que han tenido lugar después de ese.

Además, en lugar de indicar que nos encontramos en la rama ***main***, aparecerá el ***hash*** del commit al que nos hemos movido.

<br>

* **Para volver a donde estábamos antes de movernos a otro commit:**

``` bash
git checkout main
```

<br>

Ahora estaremos de nuevo en el mismo lugar en el que nos encontrábamos antes de movernos a otro commit.


<br><hr>


[^1]: Si se quiere crear una carpeta con espacios en el nombre, se debe crear escribiendo el nombre entre comillas (ejemplo: `mkdir "nombre carpeta"`).

[^2]: De la misma forma que se ha usado `git checkout <nombre_archivo>`, se puede usar `git checkout .` para deshacer los cambios en **todos** los archivos, y también `git restore <nombre_archivo>`.

[^3]: Para poder cambiar a otro commit no podemos tener elementos modificados sin guardar. Deberíamos descartar los cambios, o crear un nuevo commit con los cambios realizados.
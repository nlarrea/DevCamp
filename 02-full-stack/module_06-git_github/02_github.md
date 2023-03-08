# GitHub

<div id="indice"></div>

* [Git y GitHub, ¿son lo mismo?](#git-y-github--son-lo-mismo-)
    * [¿Qué es un repositorio?](#¿qué-es-un-repositorio)
* [Sincronizar Git y GitHub - Autenticación](#sincronizar-git-y-github---autenticación)
* [Crear un repositorio en GitHub](#crear-un-repositorio-en-github)
* [Clonar un repositorio de GitHub](#clonar-un-repositorio-de-github)
* [Realizar cambios de forma local](#realizar-cambios-de-forma-local---flujo-de-trabajo-con-git)
* [Realizar cambios de forma remota](#realizar-cambios-de-forma-remota---descargar-cambios-de-github)
* [Trabajar de forma colaborativa](#trabajar-de-forma-colaborativa---forks-y-pull-requests)

<br>

[<< #01 - RESETS, TAGS Y BRANCHES](./01_resets_tags_branches.md#conceptos-de-flujo-de-trabajo)


<br><hr>
<hr><br>


## Git y GitHub, ¿son lo mismo?

<sub>[Volver al índice](#indice) | [¿Qué es un repositorio? >>](#¿qué-es-un-repositorio)</sub>

Git es un sistema de control de versiones, mientras que GitHub es una plataforma de desarrollo colaborativo que permite a los desarrolladores trabajar juntos en proyectos de software.

Git nos permite tener los repositorios de forma local, mientras que GitHub nos permite tener los repositorios de forma remota.

* **Url interesantes:**
    * [Git](https://training.github.com/downloads/es_ES/github-git-cheat-sheet/)
    * [GitHub](https://docs.github.com/es/get-started)


<br><hr><br>


### ¿Qué es un repositorio?

<sub>[<< Git y GitHub](#git-y-github-¿son-lo-mismo) | [Volver al índice](#indice) | [Suncronizar Git y GitHub >>](#sincronizar-git-y-github---autenticación)</sub>

Un repositorio es un espacio donde se almacenan los archivos de un proyecto. En GitHub, los repositorios se almacenan en la nube, por lo que podemos acceder a ellos desde cualquier lugar.


<br><hr>
<hr><br>


## Sincronizar Git y GitHub - Autenticación

<sub>[<< Git y GitHub](#git-y-github-¿son-lo-mismo) | [Volver al índice](#indice) | [Repositorio en GitHub >>](#crear-un-repositorio-en-github)</sub>

En esta sección vamos a ver cómo autenticarnos en GitHub para poder sincronizar nuestros repositorios.

Se va a utilizar SSH. Para ello, vamos a seguir los siguientes pasos:

* Ir al directorio donde se guardarán las claves SSH. (En mi caso, es el directorio `~/.ssh`). Si no existe, crearlo.

* Generar la clave SSH. Para ello, ejecutar el siguiente comando:

```bash
ssh-keygen -t ed25519 -C "tu_correo_electronico@example.com"
```

<br>

* A continuación, se pedirá introducir el nombre del fichero. Uno de los más comunes es `id_rsa`.

* Después, se pedirá introducir una contraseña (*passphrase*). Si no se quiere introducir ninguna, se puede pulsar simplemente la tecla `Enter`. Se pedirá repetir la contraseña, si no se ha metido ninguna, volver a pulsar la tecla `Enter`.

<br>

En el fichero `~/.ssh` se habrán creado dos ficheros:

* `id_rsa`: Contiene la clave privada.
* `id_rsa.pub`: Contiene la clave pública.

<sub>* Para utilizar GitHub, ahora necesitaremos el archivo `id_rsa.pub`.</sub>

<br>

Ahora, debemos agregar la clave SSH al ssh-agent. Para ello, vamos a seguir los siguientes pasos:

* Iniciar el ssh-agent en segundo plano. Para ello, ejecutar el siguiente comando:

```bash
eval "$(ssh-agent -s)"
```

<sub>* Nos devuelve un *Agent pid*, lo que indica que ha funcionado.</sub>

<br>

* Añadir la clave SSH al ssh-agent:

```bash
ssh-add ~/.ssh/id_rsa
```

<br>

* Añadir la clave SSH a la cuenta de GitHub. Para ello, copiar el contenido del fichero `id_rsa.pub` y pegarlo en la sección `SSH and GPG keys` de la cuenta de GitHub.

<br>

* Comprobar que la conexión SSH funciona correctamente. Para ello, ejecutar el siguiente comando:

```bash
ssh -T git@github.com
```

Este código mostrará lo siguiente en pantalla:

```bash
The authenticity of host ...
... other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
Debemos escribir `yes` y pulsar la tecla `Enter`.


<br><hr>
<hr><br>


## Crear un repositorio en GitHub

<sub>[<< Sincronizar Git y GitHub](#sincronizar-git-y-github---autenticación) | [Volver al índice](#indice) | [Clonar repositorio de GitHub >>](#clonar-un-repositorio-de-github)</sub>

Crear un repositorio en GitHub es muy sencillo. Para ello, vamos a seguir los siguientes pasos:

* Ir a la página de GitHub y acceder al apartado de repositorios, una vez ahí, pulsar en el botón `New`.

<br>

* Introducir el nombre del repositorio, se nos preguntarán las siguientes opciones:

    * **Public or private**: Si queremos que el repositorio sea público o privado.

    * **Add a README file**: Si queremos que se cree un fichero `README.md` en el repositorio.

    * **Add .gitignore**: Si queremos que se cree un fichero `.gitignore` en el repositorio.

    * **Add a license**: Si queremos que se cree un fichero `LICENSE` en el repositorio.

* Pulsar en el botón `Create repository`.

<br>

* En la siguiente pantalla, se puede ver la URL del repositorio. Esta URL se utilizará para clonar el repositorio en local si se desea.


<br><hr>
<hr><br>


## Clonar un repositorio de GitHub

<sub>[<< Repositorio en GitHub](#crear-un-repositorio-en-github) | [Volver al índice](#indice) | [Cambios locales >>](#realizar-cambios-de-forma-local---flujo-de-trabajo-con-git)</sub>

Una vez creado el repositorio en GitHub, esté vacío o no, podemos clonarlo para trabajar con él de forma local.
Para ello, vamos a seguir los siguientes pasos:

* Acceder a la página del repositorio de GitHub.

<br>

Justo encima de la lista de ficheros, a la derecha, se encuentra el botón `Code`.

* Pulsar en el botón `Code` y copiar la URL del repositorio. Hemos realizado todo el proceso de SSH, por lo que la URL copiada será la de SSH.

<br>

* Abriremos una terminal, iremos al directorio de trabajo donde queremos tener el repositorio guardado, y ejecutaremos el siguiente comando:

```bash
git clone <url_copiada>
```
<sub>* `<url_copiada>` es la URL del repositorio que hemos copiado en el paso anterior.</sub>

<br>

Una vez ejecutado el comando, se creará una carpeta con el nombre del repositorio y se descargará el contenido del repositorio en local para poder trabajar con él.


<br><hr>
<hr><br>


## Realizar cambios de forma local - flujo de trabajo con Git

<sub>[<< Clonar repositorio](#clonar-un-repositorio-de-github) | [Volver al índice](#indice) | [Cambios remotos >>](#realizar-cambios-de-forma-remota---descargar-cambios-de-github)</sub>

Una vez clonado el repositorio, podemos realizar cambios en el mismo de forma local.

Lo haremos de la misma forma que la vista en el [manual básico de Git](./00_git_basics.md#añadir-archivos-al-repositorio).


<br><hr>
<hr><br>


## Realizar cambios de forma remota - descargar cambios de GitHub

<sub>[<< Cambios locales](#realizar-cambios-de-forma-local---flujo-de-trabajo-con-git) | [Volver al índice](#indice) | [Trabajo colaborativo >>](#trabajar-de-forma-colaborativa---forks-y-pull-requests)</sub>

Al igual que se puede trabajar de forma local, también se puede trabajar de forma remota, es decir, desde el propio repositorio de GitHub.

No solo se puede editar un archivo existente desde GitHub, sino que también se puede crear un nuevo archivo.

En ambos casos, lo primero que hay que hacer es acceder a la página del repositorio de GitHub. Una vez ahí, se puede realizar lo siguiente:

* **Añadir un archivo nuevo:** para ello, pulsar en el botón `Add file` situado arriba a la derecha (sobre los directorios del repositorio), y seleccionar la opción `Create new file`.

* **Editar un archivo existente:** para ello, pulsar en el nombre del archivo que queremos editar, se abrirá el archivo, y desde arriba a la derecha, podemos clicar en un botón con un *lápiz* dibujado. Ahora nos permitirá editar el archivo.


<br><hr><br>


### Volver a sincronizar el repositorio local con el remoto

Si hemos editado el repositorio de forma remota, es evidente pensar que los cambios no se verán reflejados en el repositorio local. Y así es.

Para volver a sincronizar el repositorio local con el remoto, debemos seguir los siguientes pasos:

* Abrir una terminal, y situarnos en el directorio del repositorio local.

* Ejecutar los siguientes comandos:

```bash
git fetch <nombre_remoto>
git merge <nombre_remoto> <rama>
```

Esta opción es equivalente a ejecutar el siguiente comando, pero es más recomendable ejecutar los dos comandos anteriores[^1]:

```bash
git pull <nombre_remoto> <rama>
# ejemplo:
# git pull origin main
```


<br><hr>
<hr><br>


## Trabajar de forma colaborativa - forks y pull requests

<sub>[<< Cambios remotos](#realizar-cambios-de-forma-remota---descargar-cambios-de-github) | [Volver al índice](#indice)</sub>

Se puede trabajar de forma colaborativa en un repositorio de GitHub, pero para ello, es necesario que el repositorio sea público, o que el usuario que lo ha creado de los permisos para poder trabajar en él.

Tamién es posible descargar o clonar cualquier repositorio público de GitHub, y trabajar en él de forma local como si se tratara de nuestro propio repositorio.

<br>

Para ello, se debe seguir el siguiente proceso:

* Acceder a la página del repositorio de GitHub.

* Pulsar en el botón `Fork` situado arriba a la derecha.

* Una vez hecho esto, se creará una copia del repositorio en nuestro perfil de GitHub.

* Ahora, podemos clonar el repositorio en local, y trabajar en él de forma local como si se tratara de nuestro propio repositorio.

<br>

Si las modificaciones que hemos realizado en el repositorio clonado son interesantes, podemos solicitar que se integren en el repositorio original.

Para ello, debemos seguir los siguientes pasos:

* Acceder a la página del repositorio de GitHub.

* Pulsar en el botón `Pull requests` situado arriba a la derecha.

* Pulsar en el botón `New pull request`.

* Pulsar en el botón `Create pull request`.

<br>

Una vez hecho esto, el propietario del repositorio original recibirá una notificación, y podrá revisar los cambios que se han realizado, y decidir si los integra en el repositorio original o no.

<br>

De todas formas, también es posible que la propia página de GitHub indique mediante un mensaje que el repositorio contiene datos añadidos por nosotros, y nos permita realizar la solicitud de integración (`pull request`) de forma automática.

Además, si el propietario del repositorio original ha modificado el repositorio, también se nos mostrará un mensaje para poder actualizar nuestro repositorio clonado y obtener todas las modificaciones realizadas en el original.


<br><hr>


[^1]: Si se usa el comando `git pull`, se ejecutan los comandos `git fetch` y `git merge` de forma automática, lo que significa que no podemos ver los cambios que se han realizado en el repositorio remoto antes de realizar el `merge`.

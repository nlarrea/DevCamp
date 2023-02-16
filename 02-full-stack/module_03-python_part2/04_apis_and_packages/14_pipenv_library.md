# PIPENV

<div id="indice"></div>

* [Introducción](#introducción)
* [Instalar Pipenv](#instalar-pipenv)
    * [Versión de Python](#instalar-la-versión-de-python-deseada)
* [Instalar librerías](#instalar-librerías)
* [Salir del entorno viertual](#salir-del-entorno-virtual)


<br><hr>
<hr><br>


## Introducción

<sub>[Volver al índice](#indice) | [Instalación >>](#instalar-pipenv)</sub>

> It allows you to wrap your entire projects dependencies into a single environment

Imaginar que tenemos Python 3.6.3 y usamos:
    
- requests - 1.2

Después creamos otro projecto y usamos:

- requests -2.0

<br>

El primer projecto ya no funciona porque tenemos una librería de requests que no nos sirve con ese proyecto.

> Para solucionar esto: `pipenv`

Sreará una especie de entorno virtual donde podemos tener las versiones que necesitemos para cada proyecto sin '*romper*' otros proyectos.


<br><hr>
<hr><br>


## Instalar Pipenv

<sub>[<< Introducción](#introducción) | [Volver al índice](#indice) | [Instalar librerías >>](#instalar-librerías)</sub>

Para instalar `Pipenv` abriremos la terminal y escribiremos lo siguiente:

```bash	
pip install pipenv
```

<br>

### Instalar la versión de Python deseada

Ahora, para trabajar con ello, vamos desde la terminal al directorio donde vamos a tener el proyecto y si queremos trabajar con la versión 3 de python (*por ejemplo*), escribimos:

```bash
pipenv --python 3
```

<br>

Esto creará un entorno de trabajo de Python 3 en el directorio en el que nos encontrábamos.

También se crea un `Pipfile`, si entramos en él, veremos que tenemos los siguientes datos:
- **url:** normalmente se dejará la que esté por defecto, que será la de pip
- **verify_ssl:** para asegurar la encriptación de las peticiones
- **[packages]:** aquí veremos una lista de todos los paquetes que hayamos instalado (son paquetes '*universales*', aquellos que son necesarios para que la aplicación funcione)
- **[dev-packages]:** son paquetes también, pero no son necesarios en la producción, por ejemplo, alguno de linting o testing, son aquellos que solo queremos en nuestra máquina
- **[requires]:** las versiones necesarias de python, etc. para que funcione


<br><hr>
<hr><br>


## Instalar librerías

<sub>[<< Instalación](#instalar-pipenv) | [Volver al índice](#indice) | [Salir del entorno >>](#salir-del-entorno-virtual)</sub>

Ahora para trabajar, escribimos:

```bash
pipenv install numpy
```

<br>

Se instalarán todas las dependencias de la librería, pero no de forma local en mi ordenador, sino en el directorio de pipenv, dentro de `[packages]`.

Dentro de `Pipfile.lock` podemos ver la información de la librería instalada.

Si se ha instalado la versión `1.14` de numpy y más adelante instalo numpy en mi ordenador en cualquier otra parte (la versión `1.2`, por ejemplo), mi aplicación no se verá afectada porque en ese directorio estará instalada la versión `1.14`.

<br>

Si escribimos:

```bash
which python
```

Nos dirá que está apuntando a un directorio.

<br>

Si escribimos:

```bash
pipenv shell
```

Comenzará a usar el entorno virtual y estará apuntando a otro directorio se verá también una nueva línea que nos indica que no estamos usando la versión
de python de nuestro sistema, sino la del entorno virtual.

<br>

Si volvemos a escribir:

```bash
which python
```

Nos mostrará el mismo directorio que cuando escribimos `pipenv`.


<br><hr>
<hr><br>


## Salir del entorno virtual

<sub>[<< Instalar librerías](#instalar-librerías) | [Volver al índice](#indice) | [Eliminar el entorno virtual >>](#eliminar-un-entorno-virtual)</sub>

Cuando terminemos de realizar el trabajo propuesto, desearemos cerrar el entorno virtual.

Para ello, basta con cerrar la consola o escribir un simple comando y permanecer aún en ella:

```bash
exit()
```


<br><hr>
<hr><br>


## Eliminar un entorno virtual

<sub>[<< Salir del entorno](#salir-del-entorno-virtual) | [Volver al índice](#indice)</sub>

Puede que en algún momento queramos eliminar el entorno virtual. En estos casos, el comando a ejecutar es el siguiente:

```bash
# desde el directorio donde habíamos instalado pipenv
pipenv --rm
```
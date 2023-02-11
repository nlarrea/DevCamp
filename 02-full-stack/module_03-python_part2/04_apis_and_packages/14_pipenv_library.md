# PIPENV

> it allows you to wrap your entire projects dependencies into a single environment

Imaginar que tenemos Python 3.6.3 y usamos:
    
- requests - 1.2

Después creamos otro projecto y usamos:

- requests -2.0

<br>

El primer projecto ya no funciona porque tenemos una librería de requests que no nos sirve con ese proyecto.


> Para solucionar esto: `pipenv`

Sreará una especie de entorno virtual donde podemos tener las versiones que necesitemos para cada proyecto sin '*romper*' otros proyectos.

<br>

Para instalarlos:

```bash	
pip install pipenv
```

<br>

Ahora, para trabajar con ello, vamos desde la terminal al directorio donde vamos a tener el proyecto y si queremos trabajar con python3 (por ejemplo) escribimos:

```bash
pipenv --three      # a mi no me funciona con esto

# pero si con esto:
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

<br>

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


Nos dirá que está apuntando a un directorio

Si escribimos:

```bash
pipenv shell
```

Comenzará a usar el entorno virtual y estará apuntando a otro directorio se verá también una nueva línea que nos indica que no estamos usando la versión
de python de nuestro sistema, sino la del entorno virtual.

Si volvemos a escribir:

```bash
which python
```

Nos mostrará el mismo directorio que cuando escribimos `pipenv`.
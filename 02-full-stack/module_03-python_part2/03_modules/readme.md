# Módulos

A lo largo del curso hemos utilizado métodos y funciones propias del lenguaje Python, como puede ser el `.format()` o el `len()`. Estos métodos y funciones son parte de los módulos que vienen por defecto con el lenguaje.

También hemos importado otros módulos, como `random` o `math`, que nos han permitido utilizar sus métodos y funciones. Estos módulos son parte de la librería estándar de Python.

Sin embargo, habrá ocasiones en las que deseemos trabajar con librerías de terceros, que no vienen por defecto con el lenguaje. Para ello, Python nos permite importar módulos de terceros y almacenarlos en **Python Package Index**, comúnmente llamado **Pypi**. La herramienta que se va a usar para instalar estos módulos es ***pip***.


<br><hr>
<hr><br>


## Crear un módulo e importarlo

Si abrimos la terminal y escribimos `python` en ella, podemos ver que nos abre el intérprete de Python. Si escribimos `import math`, podremos importar una librería del propio lenguaje.

Si queremos crear un módulo propio, podemos crear un archivo con extensión `.py` y escribir dentro de él las funciones que queramos. Por ejemplo, podemos crear un archivo llamado `helper.py` y escribir dentro de él una función cualquiera:

```python
def greeting(first, last):
    return f"Hi {first} {last}"
```

<br>

Si queremos importar esta función en otro archivo, podemos hacerlo de la siguiente manera:

```python
import helper
```

<br>

Si queremos utilizar la función que hemos importado, podemos hacerlo de la siguiente manera:

```python
print(helper.greeting("John", "Doe"))

# Output: Hi John Doe
```


<br><hr><br>


### Importar módulos desde otros directorios

En ocasiones, querremos tener un módulo en un archivo dentro de un directorio diferente al que se encuentra el archivo que lo importa. Para ello, vamos a comenzar guardando el archivo que contiene el módulo a importar en el directorio `libs`, una carpeta diferente al archivo que lo importa.

Ahora, escribiremos lo siguiente en el archivo que importa el módulo:

```python
import sys                      # acceder a las funciones del sistema
sys.path.insert(0, './libs')    # (0, <directorio>)

import helper                   # importar el módulo
```


<br><hr>
<hr><br>


## Importar funciones específicas de un módulo

Si queremos importar una función específica de un módulo, podemos hacerlo de la siguiente manera:

```python
from math import pi

print(pi)
```

<br><hr>
<hr><br>


## Importar módulos con alias

Si queremos importar un módulo con un alias, podemos hacerlo de la siguiente manera:

```python
import math as m

print(m.pi)
```


<br><hr>
<hr><br>


# PIP

Lo primero que haremos será comprobar si tenemos ya una versión de pip instalada en nuestro sistema. Para ello, abriremos la terminal y escribiremos lo siguiente:

```bash
py --version            # comprobar la versión de Python
>> Python 3.N.N
py -m pip --version     # comprobar la versión de pip
>> pip X.Y.Z from ... (python 3.N.N)
```

<br>

Si no tenemos instalada una versión de pip, podemos instalarla de diferentes maneras, ambas descritas en la [documentación oficial](https://pip.pypa.io/en/stable/installation/).


<br><hr><br>


### Instalar un módulo

Se pueden encontrar módulos disponibles en [Pypi](https://pypi.python.org/pypi). Para instalar un módulo, podemos escribir lo siguiente en la terminal:

```bash
pip install <nombre del módulo>
```

<br>

En este caso, vamos a utilizar la librería `numpy`, que nos permite trabajar con matrices y vectores. Para instalarla, escribiremos lo siguiente en la terminal:

```bash
pip install numpy
```

<br>

Una vez instalado numpy, podemos importarlo en nuestro archivo y utilizarlo:

```python
import numpy as np

num_range = np.arange(16)               # crear un array de 16 elementos
print(num_range)
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

num_range = num_range.reshape(4, 4)     # convertir el array en una matriz de 4x4
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15]])
```
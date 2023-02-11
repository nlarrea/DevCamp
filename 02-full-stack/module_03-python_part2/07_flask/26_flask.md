# Flask

Los requisitos para trabajar con Flask en este curso son:

* Tener pipvenv instalado
* Tener un elemento como Postman para poder comprobar las peticiones

<br>

A continucaión, vamos a ver cómo crear un proyecto con Flask. Para ello, abriremos la terminal y ejecutaremos los siguientes comandos:

```bash
# crear un directorio para el proyecto
# hay que poner todo el url del directorio, no como tengo aquí de ejemplo
mkdir 00_hello-flask

# entrar en el directorio
cd 00_hello-flask

# crear el entorno virtual
pipenv --python 3   # versión 3 de python

# instalar flask
pipenv install flask
```

<br>

En el directorio del proyecto veremos que tenemos los archivos `Pipfile` y `Pipfile.lock`. En el primero de ellos, veremos que ahora indica que en el apartado `[packages]` tenemos instalado `flask = "*"`.

<br>

Creamos el archivo `app.py` y escribimos las siguientes líneas de código:

```python
from flask import Flask

# crea una nueva instancia de flask y lo guarda dentro de la variable 'app'
app = Flask(__name__)

# creamos una 'route'
@app.route('/')
def hello():
    return "Hey Flask"


if __name__ == "__main__":
    app.run(debug=True)
```

<br>

Ahora, volveremos a la terminal y ejecutaremos los siguientes comandos:

```bash
pipenv shell    # activa el entorno virtual

python app.py   # ejecuta el archivo app.py
```

<br>

Al ejecutarlo, nos saldrán los siguientes mensajes:

```bash
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1.5000      # url de la app -> podría ser distinta en otro caso
* Restarting with stat
* Debugger is active!
* Debugger PIN: 123-456-789             # pin para poder debuggear
```

<br>

Nos indica que está ejecutándose en la url indicada, que es lo mismo que decir que está en `localhost:5000`. Si abrimos el navegador y ponemos `localhost:5000`, veremos que nos sale el mensaje `Hey Flask`.

Si miramos en la terminal, veremos que aún se está ejecutando el servidor. Si queremos pararlo, tendremos que pulsar `Ctrl + C`.

Si lo paramos y volvemos a la página de `localhost:5000` y refrescamos, veremos que ya no funciona.


<br><hr>
<hr><br>


## Dependencias de Flask

En este apartado, vamos a ver cómo instalar dependencias que prodrían ser necesarias para nuestro proyecto.

<br>

La primera que vamos a instalar es `flask-sqlalchemy`. Lo que hace es permitirnos comunicarnos con una base de datos sin necesitar escribir código SQL como tal. Para ello, ejecutaremos los siguientes comandos:

```bash
# desde el directorio del proyecto
pipenv install Flask-SQLAlchemy
```

<br>

La siguiente que vamos a instalar es `flask-marshmallow`. Lo que nos permite es renderizar los datos JSON de una forma muchísimo más sencilla. Para ello, ejecutaremos los siguientes comandos:

```bash
# desde el directorio del proyecto
pipenv install flask-marshmallow
```

<br>

La última que vamos a instalar es una que combina las dos anteriores: `marshmallow-sqlalchemy`. Lo que nos permite es combinar las dos dependencias anteriores. Para ello, ejecutaremos los siguientes comandos:

```bash
# desde el directorio del proyecto
pipenv install marshmallow-sqlalchemy
```

<br>

Si miramos en el archivo `Pipfile`, veremos que ahora tenemos las tres dependencias instaladas:

```python
[packages]
flask = "*"
flask-sqlalchemy = "*"
flask-marshmallow = "*"
marshmallow-sqlalchemy = "*"
```

<br>

Ahora vamos a comprobar que los elementos instalados funcionan. Para ello, entraremos en el archivo ya creado, `app.py`, e importaremos las dependencias, el archivo quedaría así:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# crea una nueva instancia de flask y lo guarda dentro de la variable 'app'
app = Flask(__name__)

# creamos una 'route'
@app.route('/')
def hello():
    return "Hey Flask"


if __name__ == "__main__":
    app.run(debug=True)
```

<br>

Volvemos a la terminal y ejecutamos el archivo `app.py`:

```bash
python app.py
```

<br>

Veremos que nos salen los mismos mensajes que antes y no hay errores, por lo que se han importado correctamente todas las dependencias.
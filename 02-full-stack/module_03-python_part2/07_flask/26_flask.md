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


<br><hr>
<hr><br>


## Crear una base de datos SQLite con SQLAlchemy

Vamos a crear una base de datos SQLite, por lo que no vamos a usar código SQL puro, sino que vamos a usar SQLAlchemy. Vamos a crear el esquema (tabla) con la que vamos a trabajar, y vamos a permitir al código generar esa tabla por nosotros.

<br>

En primer lugar, vamos a acceder al archivo `app.py` y vamos a eliminar las siguientes líneas de código:

```python
@app.route('/')
def hello():
    return "Hey Flask"
```

<br>

A continución, vamos a integrarlo con nuestro sistema de base de datos. Habíamos llamado anteriormente a la librería `os`, ahora vamos a utilizarla para crear un directorio para la base de datos. Este directorio es necesario porque sin él, flask no podrá saber dónde guardar la tabla SQLite.

El código, tras realizar todas las modificaciones, queda de la siguiente manera:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# le decimos a flask dónde está la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
# le pasamos el directorio al que queremos que vaya, y le decimos que se llama 'app.sqlite'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
# creamos un objeto de base de datos
db = SQLAlchemy(app)        # instanciar objeto de SQLAlchemy
ma = Marshmallow(app)       # instanciar objeto de Marshmallow

# creamos el esquema de la tabla (heredera de db.Model)
class Guide(db.Model):
    # añadimos una columna de tipo integer, y decirmos que es una primary key
    # primary_key=True -> hará que cada Guide tenga su propio ID, y cada ID incrementa automáticamente
    id = db.Column(db.Integer, primary_key=True)
    # creamos 2 columnas más de tipo string y limitamos su cantidad de chars a 100 y 144
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class GuideSchema(ma.Schema):
    class Meta:
        # indicamos los 'fields' a los que queremos acceder dentro de una tupla
        fields = ("title", "content")


guide_schema = GuideSchema()            # para trabajar con 'single guide'
guides_schema = GuideSchema(many=True)  # para trabajar con 'multiple guides'


if __name__ == "__main__":
    app.run(debug=True)
```

<br>

Por último, desde la terminal, vamos a ejecutar el archivo `app.py`:

```bash
# si no está activado el entorno virtual, activarlo, si ya está activado, saltar este paso:
pipenv shell


python
>>> from app import app, db
# podría dar un warning, pero no pasa nada

>>> app.app_context().push()
>>> db.create_all()
```

<br>

Los pasos que he seguido yo desde la terminal y los de la clase no son los mismos, esto se debe a las actualizaciones de Flask.
# MongoDB

<div id="indice"></div>

* [Instalar MongoDB](#instalar-mongodb)
* [Usar MongoDB](#usar-mongodb)
    * [Crear un usuario](#crear-un-usuario)
    * [Crear una colección](#crear-una-colección)

## Instalar MongoDB

<sub>[Volver al índice](#indice) | [Usar MongoDB >>](#usar-mongodb)</sub>

Se puede acceder a la página de descargas de MongoDB desde [este link](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/). En ella aparecen los pasos a seguir para instalar MongoDB en Linux, macOS y Windows.

<br>

Además de instalar MongoDB, también se debe instalar la terminal de MongoDB, `mongosh`. Para ello, se deben seguir las instrucciones de [este enlace](https://www.mongodb.com/docs/mongodb-shell/install/).

* En Windows, si la forma de instalar la terminal es a través de un archivo `.zip`, hay que añadir la ruta de instalación de `mongosh` a la variable de entorno `PATH` para poder ejecutarlo desde cualquier directorio.

> Para ello, accedemos a `panel de control > sistema y seguridad > sistema > configuración avanzada del sistema > variables de entorno > variables de entorno` y añadimos la ruta de la carpeta `bin` de `mongosh` a la variable `PATH`.


<br><hr>
<hr><br>


## Usar MongoDB

<sub>[<< Instalar MongoDB](#instalar-mongodb) | [Volver al índice](#indice) | [Crear usuario >>](#crear-un-usuario)</sub>

Lo primero que debemos hacer es **acceder a la terminal** de MongoDB, `mongosh`. Para ello, abrimos una terminal y ejecutamos el comando `mongosh`.

Veremos que se nos ha conectado a la base de datos `test` por defecto.

<br>

Para **ver todas las bases de datos** que tenemos, ejecutamos el comando:

```mongo
show dbs
```

<br>

Para crear una **nueva base de datos**, ejecutamos el comando `use <nombre de la base de datos>`. Por ejemplo, para crear una base de datos llamada `mongoCourse`, ejecutamos el comando `use mongoCourse`.

Si volvemos a escribir el comando `show dbs`, veremos que no se ha añadido la base de datos `mongoCourse` a la lista anterior.

```mongo
use mongoCourse
# switched to db mongoCourse

show dbs
```

<br>

Esto se debe a que el simple hecho de crear una base de datos llamada `mongoCourse` (*en este caso*), no hace que se añada a la lista. Para que se añada, debemos comenzar a añadir elementos a la base de datos.

<br>

**Tras haber escrito `use mongoCourse`** veremos que ya no aparece `test` cada vez que escribimos un comando, sino que aparece `mongoCourse`. Esto se debe a que, al crear una base de datos, se nos conecta a ella automáticamente. Además, se nos indica mediante el mensaje `switched to db mongoCourse`.

Si escribimos `db`, veremos que nos devuelve `mongoCourse`. Ese `db` es el objeto que se crea y a través del cual podemos interactuar con la base de datosm, porque hace referencia siempre a la base de datos con la que se está trabajando.


<br><hr><br>


### Crear un usuario

<sub>[<< Usar MongoDB](#usar-mongodb) | [Volver al índice](#indice) | [Crear colección >>](#crear-una-colección)</sub>

Escribir en Mongo es bastante similar a escribir código JavaScript. Por ello, se tiende a alternan bastante entre escribir código en la terminal de `mongosh` y escribir en un editor de texto como puede ser *Visual Studio Code*.

<br>

Ahora, vamos a crear un usuario para nuestra base de datos (para almacenarlo en ella). Para ello, crearemos un archivo al que (en mi caso) llamaré `mongo.js` y escribiremos el siguiente código:

```js
db.createUser({
    user: "naia",
    pwd: "password",
    customData: {startDate: new Date()},
    roles: [
        {role: "clusterAdmin", db: "admin"},
        {role: "readAnyDatabase", db: "admin"},
        "readWrite"
    ]
})
```

<br>

Las claves de este objeto son claves concretas de MongoDB.

Una vez creado el código, lo copiamos, volvemos a la `mongo shell` y lo pegamos. Si todo ha ido bien, veremos que se nos ha creado el usuario.

![mongo-createuser](./media/mongo-createuser.png)

<br>

Para crear más usuarios, simplemente volveríamos a escribir el código anterior, pero cambiando los valores de las claves `user` y `pwd`:

> Al ser un ejemplo, sólo he modificado el nombre de usuario.

```js
db.createUser({
    user: "cris",
    pwd: "password",
    customData: {startDate: new Date()},
    roles: [
        {role: "clusterAdmin", db: "admin"},
        {role: "readAnyDatabase", db: "admin"},
        "readWrite"
    ]
})
```

<br>

Para **ver todos los usuarios** que tenemos en la base de datos, ejecutamos el comando `db.getUsers()`:

```mongo
db.getUsers()
```

<br>

Esta sería la respuesta del comando:

![mongo-getusers](./media/mongo-getusers.png)

<br>

Como se puede observar, nos devuelve ambos usuarios.

Podemos eliminar un usuario escribiendo el siguiente comando directamente en la terminal:

```mongo
db.dropUser("cris")
```

<br>

Si volvemos a ejecutar el comando `db.getUsers()`, veremos que ya no aparece el usuario `cris`:

![mongo-dropuser](./media/mongo-dropuser.png)


<br><hr><br>


### Crear una colección

<sub>[<< Crear usuario](#crear-un-usuario) | [Volver al índice](#indice) | [Añadir documentos >>](#añadir-documentos-a-una-colección)</sub>

Al escuchar las palabras `base de datos` podríamos pensar en una especie de tabla con información. En el caso de MongoDB, una base de datos es un conjunto de colecciones en vez de una tabla.

En esas colecciones, se almacenan los documentos, pero antes de comenzar a guardar documentos, debemos crear una colección.

<br>

A lo largo de este curso, vamos a crear una base de datos para almacenar libros, por ello, lo primero que debemos hacer ahora es crear una colección a la que llamaremos `books`.

Para realizar esto, vamos a ir a la terminal de `mongosh` y escribiremos el siguiente comando:

```mongo
db.createCollection("books")
```

<br>

Tras hacer esto, la terminal devolverá un `{ ok: 1 }`, lo que significa que se ha creado la colección correctamente.

<br>

Para **ver todas las colecciones** que tenemos en la base de datos, ejecutamos el comando:

```mongo
show collections
```

<br>

Y veremos que se nos ha creado la colección `books`.


<br><hr><br>


### Añadir documentos a una colección

<sub>[<< Crear colección](#crear-una-colección) | [Volver al índice](#indice)</sub>


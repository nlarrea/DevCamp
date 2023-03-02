# Instalación de npm

Para saber si tenemos instalado `npm` en nuestro sistema, podemos ejecutar el siguiente comando en la terminal:

```bash
npm -v
```

<br>

Si lo tenemos instalado, nos devolverá la versión de `npm` que tenemos instalada en nuestro sistema. Si no lo tenemos instalado, nos devolverá un error.

En este último caso, podemos ir a la página de [Node.js](https://nodejs.org/es/) y descargar la versión LTS de `Node.js` para nuestro sistema operativo.


<br><hr>
<hr><br>


# Generación de proyectos

Una vez nos aseguramos de tenerlo todo instalado, ejecutamos el siguiente comando en la terminal:

```bash
npm install devcamp-js-project-generator -g
```

<br>

Este comando instalará el paquete `devcamp-js-project-generator` de forma **global** en nuestro sistema.

<br>

Una vez instalado, accederemos al directorio donde queramos crear nuestro proyecto y ejecutaremos el siguiente comando:

```bash
js-generate
```

<br>

Nos pedirá que indiquemos el tipo de proyecto que queremos crear mostrando el siguiente mensaje:

```bash
? What type of project do you want to create?
> es6-starter
  react-bootstrap
  react-redux
  react-skeleton
```

<br>

Podremos mover el cursor de arriba a abajo haciendo uso de las teclas `↑` y `↓` y seleccionar el proyecto que queramos crear con la tecla `enter`.

<br>

A continuación, nos pedirá que indiquemos el nombre del proyecto que queremos crear, así que le daremos el nombre:

```bash
? Project name: ModuleSection
```

<br>

Se habrá creado una carpeta con ese nombre y varios archivos en su interior.

El archivo en el que camos a trabajar se encuentra dentro de la carpeta `src` y se llama `boostrap.js`.

<br>

Ahora, desde dentro de la carpeta `ModuleSection`, escribiremos en la terminal el siguiente comando:

```bash
npm install
```

<br>

Esto lo que hace es ir a nuestro `package.json` y descargar todas las dependencias que necesitamos para nuestro proyecto, es decir, aquellas que están indicadas en ese archivo.

Se habrá creado la carpeta `node_modules` y se habrán descargado todas las dependencias que necesitamos.


<br><hr>
<hr><br>


# Ejecución del proyecto

A partir de ahora, vamos a ejecutar nuestro código en nuestro propio servidor local.

Para ello, y para asegurarnos de que todo está funcionando correctamente, vamos a ejecutar el siguiente comando:

```bash
npm start
```

<br>

Esto lo que hace es ejecutar el script `start` que está indicado en nuestro `package.json`.

Dentro de los mensajes especificados por la terminal tras ejecutar el comando anterior, se mostrará el siguiente mensaje:

```bash
Project is running at http://localhost:3000/
```

<br>

Si accedemos a esa dirección en nuestro navegador, veremos el mensaje impreso en el archivo `boostrap.js`.

<br>

Para detener el servidor, simplemente tendremos que pulsar `ctrl + c` en la terminal.
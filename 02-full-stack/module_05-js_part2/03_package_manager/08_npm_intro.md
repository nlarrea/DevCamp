# npm

<div id="indice"></div>

* [Introducción](#introducción)
* [Package.json](#packagejson)


<br><hr>
<hr><br>


## Introducción

`npm` es el gestor de paquetes de Node.js. Es un programa que se instala en tu computadora y que te permite tanto instalar paquetes de Node.js, como otros paquetes de terceros.

Ya hemos hablado de él en la sección anterior, pero vamos a profundizar un poco más en él.

Para ver qué paquetes tenemos instalados ya, debemos ejecutar el siguiente comando:

```bash
npm list -g
```


<br><hr>
<hr><br>


## Package.json

El archivo `package.json` es un archivo de texto que contiene información sobre el proyecto. Es un archivo que se crea automáticamente cuando ejecutamos el comando `npm init` y que nos permite configurar el proyecto.

Tiene una sección llamada `dependencies` que contiene la lista de paquetes que nuestro proyecto necesita para funcionar.
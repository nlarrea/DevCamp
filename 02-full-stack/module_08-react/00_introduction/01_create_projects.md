# Generar un proyecto de React

Existen diferentes formas de generar un proyecto de React. Esto puede ser un poco confuso al principio, debido a la cantidad de dependencias que se necesitan o se deben instalar, y a la cantidad de configuraciones que se deben realizar.

Por ello, con la intención de facilitar el proceso, se va a hacer uso de una herramienta llamada **devcamp-js-builder**. Este es un paquete de NPM que nos permite generar un proyecto de React con todas las dependencias necesarias y con la configuración inicial.

<br>

Para instalar esta herramienta, ejecutamos el siguiente comando en la terminal:

```bash
npm install devcamp-js-builder -g
```

<br>

Si queremos ver qué paquetes tenemos instalados de forma global, podemos ejecutar el siguiente comando en la terminal:

```bash
npm list -g
```

<br>

Para generar un proyecto de React, ejecutamos el siguiente comando en la terminal:

```bash
js-generate

# this program will ask you the next question
? What project template would you like to generate?
# use the arrow keys to select the one you want
> react-bootstrap
  react-redux
  react-skeleton

# then, it will ask you the next question
? Project name: MyProject # you can use any name you want
```

<br>

Ahora, tendremos una carpeta con diferentes archivos en su interior. Vamos a movernos dentro de la carpeta del proyecto y vamos a ejecutar el siguiente comando en la terminal:

```bash
# move to the project folder
cd MyProject

# install the dependencies
npm install
```

<br>

Con el segundo comando, vamos a instalar las dependencias señaladas en el archivo **package.json** y las instala en este proyecto.

<br>

Una vez termine la instalación, vamos a comprobar que todo funciona correctamente. Para ello, vamos a ejecutar el siguiente comando en la terminal:

```bash
npm start
```

<br>

Este comando hace que se ejecute el proyecto. Para comprobar que funciona, vamos a abrir el navegador y vamos a acceder a la siguiente dirección:

```bash
i ｢wds｣: Project is running at http://localhost:3000/
```

<br>

Si clicamos en el enlace mostrado en la terminal, o escribimos la dirección en el navegador (`localhost:3000`), veremos que se nos muestra una página con el texto **DevCamp React Starter**.

Esto significará que todo funciona correctamente y que la aplicación se está ejecutando perfectamente.
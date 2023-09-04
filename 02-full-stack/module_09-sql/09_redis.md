# Redis

<div id='index'></div>

* [Instalar Redis en Mac](#instalar-redis-en-mac)
* [Primeros pasos](#primeros-pasos)
* [SET y GET](#set-y-get)

<br/>

[<< PROYECTO](./08_project.md#proyecto) | [HOME](../../README.md#devcamp)

<br/>

<hr/><hr/><br/>

## Instalar Redis en Mac

Para realizar la instalación de Redis en Mac, en primer lugar, instalaremos [Hombrew](https://brew.sh/) desde su página principal a través de este comando:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

<br/>

Hecho esto, se habrá instalado y ya podremos proceder a instalar Redis con el siguiente comando:

```bash
brew install redis
```

> Puede tomar unos minutos dependiendo del equipo de cada uno.

<br/>

<hr/><hr/><br/>

## Primeros pasos

Ahora que se ha instalado Redis, comenzaremos escribiendo lo siguiente en la terminal:

```bash
redis-server
```

<br/>

Se verá cierta información en la pantalla, lo que indicará que todo funciona correctamente.

En la última línea de la terminal, se podrá ver que el puerto es el `6379` (*número situado al final de la última línea: `The server is now ready to accept connections on port 6379`*).

Para comenzar un servidor Redis, se debe escribir lo siguiente:

```bash
redis-cli
```

<br/>

Como resultado se obtiene lo siguiente:

```bash
127.0.0.1:6379>
```

<br/>

Lo que significa que todo está funcionando y que podemos proseguir utilizando el servidor.

<br/>

<hr/><hr/><br/>

## SET y GET

* `SET`:

    * Sintaxis:

    ```bash
    SET key value [EX seconds] [PX milliseconds] [NX|XX]
    ```

    > Si el parámetro está entre '[]', es opcional, sino, es obligatorio.

    * Ejemplo:

    ```bash
    127.0.0.1:6379> SET page_name 'About us'
    OK
    ```

    > La primera línea representa lo que el usuario introduce en la terminal: `SET key value`.
    >
    > La segunda línea muestra lo que la terminal devuelve: `OK`, que todo ha salido correctamente.

* `GET`:

    * Sintaxis:

    ```bash
    GET key
    ```

    * Ejemplos:

    ```bash
    # Ejemplo 1
    127.0.0.1:6379> GET wrong_key
    (nil)
    
    # Ejemplo 2
    127.0.0.1:6379> GET page_name
    "About us"
    ```

    > En el primer ejemplo se intenta obtener el valor de una clave que no existe. Sin embargo, esto no es problema, puesto que cuando esto sucede, Redis simplemente devuelve un `(nil)`.
    >
    > Finalmente, intentamos acceder a la clave correcta, lo que da como resultado el valor esperado.
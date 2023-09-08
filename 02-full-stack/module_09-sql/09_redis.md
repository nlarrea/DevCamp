# Redis

<div id='index'></div>

* [Instalar Redis en Mac](#instalar-redis-en-mac)
* [Primeros pasos](#primeros-pasos)
* [SET y GET](#set-y-get)
* [Estructurar las claves](#estructurar-las-claves)
* [Eliminar ítems](#eliminar-ítems)
* [Comprobar si una clave existe](#comprobar-si-una-clave-existe)

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

<br/>

<hr/><hr/><br/>

## Estructurar las claves

En SQL se suele disponer (*o por lo menos es buena práctica hacerlo*) de una variable de tipo **ID**, con un valor único para saber a qué elemento se está haciendo referencia.

En Redis, esto no ocurre. No existe un **ID** para los registros, sino que los datos se almacenan en pares clave-valor. Entonces, ***¿cómo se puede saber a qué registro está haciendo referencia una clave?***

Un ***truco*** muy habitual para solucionar esto suele ser escribir una especie de **ID**, seguido de un `:` y finalmente el nombre de la clave que se quiere usar. Por ejemplo:

```bash
127.0.0.1:6379> SET 105:guide_like_count 0
OK
127.0.0.1:6379> GET 105:guide_like_count
"0"
```

<br/>

De esta forma se podría conseguir saber a qué elemento se está haciendo referencia.

<br/>

<hr/><hr/><br/>

## Incrementar y decrementar valores

Vamos a comenzar creando un *post*:

```bash
127.0.0.6379> SET post_like_count:42 0
OK
```




* **Incrementar valores:**

```bash
# Incrementar de 1 en 1
127.0.0.6379> INCR post_like_count:42
(integer) 1
127.0.0.6379> INCR post_like_count:42
(integer) 2
127.0.0.6379> GET post_like_count:42
"2"

# Incrementar en cantidades concretas
127.0.0.6379> INCRBY post_like_count:42 100
(integer) 102
127.0.0.6379> GET post_like_count:42
"102"
```


* **Decrementar valores:** funciona de la misma manera que las funciones `INCR` e `INCRBY`.

```bash
# Decrementar de 1 en 1
127.0.0.6379> DECR post_like_count:42
(integer) 101
127.0.0.6379> GET post_like_count:42
"101"

# Decrementar en cantidades concretas
127.0.0.6379> DECRBY post_like_count:42 21
(integer) 80
```

<br/>

<hr/><hr/><br/>

## Eliminar ítems

Para eliminar ítems, se hace uso de la función `DEL`:

```bash
# Creamos varios ítems
127.0.0.6379> SET first_name "Jordan"
OK
127.0.0.6379> SET last_name "Hudgens"
OK
127.0.0.6379> SET middle_name "David"
OK

# Se pueden eliminar varios a la vez
127.0.0.6379> DEL first_name last_name
(integer) 2		# cuántos ítems se han eliminado
127.0.0.6379> GET first_name
(nil)			# si no encuentra algo, no da error, devuelve (nil)
127.0.0.6379> 
```

<br/>

<hr/><hr/><br/>

## Comprobar si una clave existe

Técnicamente, se puede usar el comando `GET` para saber si una clave existe o no, sin embargo, ésta se considera una práctica pobre.

La mejor forma de comprobar si existe o no una clave, es hacer uso de `EXISTS`. Veámoslo con un ejemplo:

```bash
127.0.0.1:6379> SET title "My post"
OK
127.0.0.1:6379> EXISTS title
(integer) 1
127.0.0.1:6379> EXISTS a_key_that_has_not_been_created
(integer) 0
127.0.0.1:6379> GET a_key_that_has_not_been_created
(nil)
```

<br/>

Puede que estés pensando: ***¿por qué usar `EXISTS` y no un simple `GET`?***

La respuesta es más sencilla de lo que parece. Si se usa `EXISTS` y el ítem existe, se recibe un `1`, sin embargo, cuando éste no existe, se obtiene un `0`. Estos valores pueden ser muy útiles para usarlos en condicionales. Sin embargo, usando `GET`, no se obtiene un valor que pueda usarse para comparar o para decidir si una condición se cumple o no.

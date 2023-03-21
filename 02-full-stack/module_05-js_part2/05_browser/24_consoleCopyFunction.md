# Console's Copy Function to Scrape a Website

Entramos en la página de [DailySmarty](https://dailysmarty.com/) y abrimos la consola de Chrome. Ahora, vamos a intentar copiar todos los 'topics' que aparecen en los enlaces de la página.

Si se hiciera a mano, sería terrible, por lo que vamos a intentar usar la función 'copy' de la consola:

```js
const allTopics = document.querySelectorAll('.topics');

// si vemos lo que ha guardado en la constante:
// nos devuelve un NodeList con todos los elementos que tienen la clase 'topics'
allTopics

// intentamos copiar su contenido
copy(allTopics)
```

<br>

Puede parecer que es así de sencillo, pero si pegamos lo que se ha copiado, obtenemos lo siguiente:

```js
{
    "0": {},
    "1": {},
    "2": {},
    "3": {},
    "4": {},
    "5": {},
    "6": {},
    "7": {}
}
```

<br>

Desde luego, esto no es lo que queremos. Lo que queremos es un array con los topics. Para ello, vamos a convertir ese NodeList en un array:

```js
const topicsToArray = Array.prototype.slice.call(allTopics);

// ahora probamos a copiar esto
copy(topicsToArray)
```

<br>

En este caso, esto es lo que tenemos como resultado:

```js
[
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {}
]
```

<br>

Sigue sin ser lo que queremos, pero se parece más, puesto que ahora se trata de una lista de objetos, algo que podemos manejar mejor desde JavaScript.

Si hacemos lo siguiente:

```js
topicsToArray[0]
```

<br>

Obtenemos el primer `<div>`, por lo que podemos acceder a su contenido:

```js
topicsToArray[0].textContent

// esto nos devuelve:
GAME DEVELOPMENT COMPANIESBLOCKCHAIN GAME DEVELOPMENTBC GAME CLONE SCRIPTBETFURY CLONE SCRIPT
```

<br>

Ahora, si queremos obtener todos los topics, podemos hacer un *bucle* usando `map`:

```js
const topicList = topicsToArray.map(topic => topic.textContent);
```

<br>

Esto guarda todos los `textContent` de los `<div>` en un array. Si copiamos esto:

```js
[
    "GAME DEVELOPMENT COMPANIESBLOCKCHAIN GAME DEVELOPMENTBC GAME CLONE SCRIPTBETFURY CLONE SCRIPT",
    "BUSINESSGITHUBTOKEN BASED AUTHENTICATION",
    "PATIENCE",
    "GAMBLINGCASINO ",
    "BC.GAME CLONE SCRIPT",
    "PROGRAMMING",
    "TOKEN DEVELOPMENTCREATE BEP20 TOKENSBEP20 TOKEN DEVELOPMENT",
    "APP DEVELOPMENTML DEVELOPMENT COMPANYMOBILE APPS"
]
```

<br>

Ahora sí que tenemos lo que queríamos. Podemos copiar esto y pegarlo en un archivo de texto, por ejemplo, para tener una lista de los topics.
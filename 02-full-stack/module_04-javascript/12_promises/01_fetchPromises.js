// USAR FETCH PARA COMUNICARSE CON APIs

/* 
este tipo de funciones se utilizan muchísimo para realizar la comunicación con
APIs, así que son unos pasos a seguir que vamos a acabar usando, sí o sí para
comunicarnos con servicios externos

en esta sección vamos a comunicarnos con la API de DailySmarty
*/

/* FETCH
devuelve una promesa, por lo que nos podemos ahorrar el tener que escribir el
'new Promise'

es una buena practica añadir la palabra 'promise' al nombre de la variable que
guarde el valor de 'fetch' para que recordemos siempre que es del tipo Promise

recibe un único argumento -> la llamada al API
se podrían añadir también o
*/

console.log("Starting fetch call");
const postPromise = fetch('https://api.dailysmarty.com/posts')
console.log("After fetch call");
console.log(postPromise);
console.log("After program has run");

/* 
como fetch devuelve una promesa, tenemos que hacer algo con ella

las promesas no se pueden mostrar en pantalla de la misma forma que lo haríamos
con el resto de elementos, debemos indicar qué queremos hacer si el resultado
ha sido X ó Y
*/

postPromise
    /* si hacemos: .then(data => console.log(data))
    veremos que seguimos sin tener la información que queremos (los posts del
    API DailySmarty), esto se debe a que hay que decirle a JS que esa respuesta
    está en formato JSON
       
    hay que hacer lo siguiente
    */
    // le decimos a JS que 'data' es de tipo JSON y hace return de esa 'conversión'
    .then(data => data.json())   // esto es como hacer 'return data.json()'
    .then(data => { // recibe el 'data.json()' del .then() anterior
        console.log(data);
        /* ahora tenemos un objeto llamado 'posts' con los posts de la API, y
        cada uno de esos post es un objeto */
        
        data.posts.forEach(item => {    // parse json data
            console.log(item.title);
        });
    })
    // si no funciona algo bien y recibimos un error -> catch
    .catch(err => {
        console.error(err);
    });
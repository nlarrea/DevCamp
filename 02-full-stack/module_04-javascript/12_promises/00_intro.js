// PROMESAS

/* 
se utilizan mucho para trabajar con APIs

EJEMPLO:
quiero trabajar con la APP de twitter -> haces petición y tienes que esperar a
que llegue la información

JS permite trabajar de forma asíncrona con promesas:
- permite realizar la petición a la API y seguir realizando otras tareas, para,
cuando se obtuviera la información de la misma, entonces trabajar con ella

JS permite escoger qué elementos cargan antes y cuáles lo harán más tarde
*/

/* 
las promesas toman 2 argumentos, y se les llama así por convenio:
- resolve: successful-type response
- reject: failure-type response

con ello, le estamos diciendo a la API y a la función que queremos que se nos
devuelva algún tipo de dato o información, y que si no la consigue, lo que nos
debe devolver ese error, y nosotros podremos trabajar con él

las funciones normales no hacen que tengamos que pensar cómo trabajar si lo que
recibimos es un error, pero las promesas nos obligan a trabajar con ellos
*/

let sleepyGreeting = new Promise((resolve, reject) => {
    // para simular la petición correct a la API
    setTimeout(() => {
        // cualquier cosa dentro de resolve es lo que se ejecuta si todo va bien
        resolve("Hello...");
    }, 2000);

    // para simular una petición errónea a la API
    setTimeout(() => {
        reject(Error("Something went wrong"));
    }, 2000);
})

/* 
para obtener la información (comenzar la simulación de la llamada al API),
habrá que llamar a la función de la siguiente manera (abajo)

se utilizan 'then' y 'catch', donde 'then' está mapeada a 'resolve', es decir,
se ejecuta siempre que la respuesta es 'resolve', mientras que 'catch' lo hará
cuando se devuelva el 'reject'
*/

sleepyGreeting
    .then((data) => {
        console.log(data);
    })
    .catch((err) => {
        console.error(err);
    });

/* CÓMO FUNCIONA?
después de darle al RUN, se tardan 2 segundos hasta que se obtienen los datos
de la función que simula el API

si dejamos la función como está, se ejecutará SIEMPRE el 'resolve', entonces se
ejecuta la parte de 'then' asociada a la respuesta

si comentamos el primer setTimeout (el de 'resolve'), se ejecutará el reject(),
por lo que obtendremos el error
*/
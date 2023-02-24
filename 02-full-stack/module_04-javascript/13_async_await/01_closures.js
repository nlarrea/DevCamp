// CLOSURES

/* 
en el apartado anterior, hemos visto cómo devolver uno a uno los resultados de
cada una de las peticiones pero, qué pasa si queremos realizar las peticiones
en ese orden y queremos que devuelva toda la información de las mismas a la vez?

para eso existen las closures -> funciones que pueden almacenarse en variables,
y entonces puede ser pasada a otras funciones

vamos a partir del código del ejercicio anterior, y modificarlo de tal forma
que los mensajes de cada una de las llamadas (login y updateAccount) se vean
una vez se hayan ejeutado las dos, y no a medida que se va ejecutando cada una
*/

// simulación de llamada a login() -> obtener credenciales de usuario
const login = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("User logged in")
        }, 4000);
    });
}

// simulación de llamada a updateAccount() -> actualizaría el estado a 'logged'
const updateAccount = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Updating last login...");
        }, 2000);
    });
}

// pasamos unos parámetros -> pueden tener cualquier nombre
async function loginActivities(login, updateAccount){
    // quitamos las llamadas a las funciones -> llamamos a los parámetros
    const returnedLogin = await login;
    console.log(returnedLogin);

    const returnedUpdateAccount = await updateAccount;
    console.log(returnedUpdateAccount);
}

// pasamos las funciones como argumentos
loginActivities(login(), updateAccount());
/* los 'await' siguen devolviendo promesas, así que podemos seguir tratándolas
de esa forma

la función 'async loginActivities' lo que va a hacer es 'encapsular' y en vez
de esperar 2 segundos y devolver lo de la primera llamada y después de otros 2
lo de la segunda, lo que hace es esperar a que todos los procesos terminen para
mostrar los resultados en la consola

realmente está haciendo lo mismo que en el apartado 00_intro.js, pero esperando
a que todos los procesos terminen para mostrar los resultados
*/

/* SE SIGUE REALIZANDO EL ASYNC-AWAIT?
para comprobar si se sigue cumplienco el async-await (esperar a que termine la
llamada al login antes de ejecutarse el 'updateAccount'), modificamos lo que va
a tardar login(), lo pasamos de 2 segundos a 4. Sin el asyn-await, login()
debería ejecutarse 2 segundos más tarde que updateAccount(), pero como tenemos
el async-await, se ejecutarán en el orden de llamada dentro de loginActivities
*/
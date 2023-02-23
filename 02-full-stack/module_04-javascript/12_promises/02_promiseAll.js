// PROMISE ALL -> agrupar promesas y tratarlas como un grupo de promesas

/* 
imaginar que tenemos estas dos promesas que se ejecutan cada vez que un usuario
hace login en una app

son dos promesas muy similares -> pueden agruparse como si fueran la misma
*/

const greeting = new Promise((resolve, reject) => {
    resolve("Hi there");
    reject("Oops, bad greeting");
});

const updateAccount = new Promise((resolve, reject) => {
    resolve("Updating login...");
    reject("Error updating account with login");
});

// agrupamiento de Promises:
// Promise.all() -> como parámetro: un array de las promesas a agrupar
const loginActivities = Promise.all([greeting, updateAccount]);

// console.log(loginActivities);
// devuelve una promesa, pero tiene más promesas dentro que hay que recorrer

loginActivities.then(res => {
    // console.log(res);   // ["Hi there", "Updating login..."]
    // muestra los 'resolve' o 'reject' (depende de lo que responda) de las promesas agrupadas

    // como queremos tratar cada Promise de forma independiente:
    res.forEach(activity => {
        console.log(activity);
    });
})
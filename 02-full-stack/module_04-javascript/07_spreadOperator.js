// SPREAD OPERATOR

/*
sintaxis -> ...word

se utiliza para muchísimas cosas, entre ellas:
*/

// COMBINAR ARRAYS

let shoppingCart = [345, 375, 765, 123];
let newItems = [98, 123];

// forma lógica de creer que se puede hacer
shoppingCart.push(newItems);
console.log(shoppingCart);      // [345, 375, 765, 123, [98, 123]] -> no es lo que queremos


// cómo se hace
shoppingCart = [345, 375, 765, 123];

shoppingCart.push(...newItems);
console.log(shoppingCart);      // [345, 375, 765, 123, 98, 123] -> ahora sí



// COPIAR ARRAYS

const shoppingCart2 = [345, 375, 765, 123];
const updatedCart = shoppingCart2;

updatedCart.push(5);
console.log(updatedCart);       // [345, 375, 765, 123, 5]
console.log(shoppingCart2);     // [345, 375, 765, 123, 5] -> también ha cambiado
// esto no es lo que queríamos hacer -> cómo deberíamos hacerlo? copiando la lista

// forma correcta
const shoppingCart3 = [345, 375, 765, 123];
const updatedCart2 = shoppingCart2.slice();

updatedCart2.push(5);

console.log(updatedCart2);      // [345, 375, 765, 123, 5]
console.log(shoppingCart3);     // [345, 375, 765, 123]
// ahora funciona bien


// cómo hacerlo con 'spread operator'
const updatedCart3 = [...shoppingCart3];

updatedCart3.push(5)

console.log(updatedCart3);      // [345, 375, 765, 123, 5]
console.log(shoppingCart3);     // [345, 375, 765, 123]
// también funciona



// PASAR ARRAYS A FUNCIONES QUE REQUIEREN VARIOS PARÁMETROS

console.log(Math.max(1, 5, 1, 10, 2, 3));   // devuelve el valor más alto) -> 10

// pero si le pasamos un array a .max():
const orderTotals = [1, 5, 1, 10, 2, 3];
console.log(Math.max(orderTotals));         // NaN
/* esto ocurre porque 'max' necesita varios parámetros para funcionar y según
JS, solo le hemos pasado un argumento, que ni siquiera es un número -> array */

// para arreglarlo:
console.log(Math.max(...orderTotals));      // 10
/* cómo funciona
1. -> [1, 5, 1, 10, 2, 3] -> tenemos este array
2. -> ...[1, 5, 1, 10, 2, 3] -> usamos el spread operator
3. -> 1, 5, 1, 10, 2, 3 -> hace que a cada elemento del array se le trate como
un elemento por 'separado', por lo que JS entiende que le estamos pasando más
de un elemento y ahora sí, devuelve el mayor de todos los valores
*/



// OBJECT DECONSTRUCTION

const {starter, closer, ...relievers} = {
    starter: "Verlander",
    closer: "Giles",
    relief_1: "Morton",
    relief_2: "Gregerson"
}

console.log(starter);       // Verlander
console.log(closer);        // Giles
console.log(relievers)      // { relief_1: 'Morton', relief_2: 'Gregerson' }

/* 
en este ejemplo, tenemos un objeto con varios elementos. Sabemos que el objeto
tiene un 'starter' y un 'closer', pero no sabemos cuántos 'relief' va a tener.

En estos casos, lo mejor es usar un 'object deconstruction', donde podemos
obtener los datos de aquellos elementos que sabemos que están presentes, y
después guardar todos los demás en otra constante para acceder a ella más tarde
*/
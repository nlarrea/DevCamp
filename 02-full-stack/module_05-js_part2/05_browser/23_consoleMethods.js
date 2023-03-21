// console acepta cualquier cantidad de parámetro y todo puede ser impreso
/*
const someObj = {
    name: 'Naia'
}
console.log('Hi', someObj, 'After object');
*/

// pero existen varias formas diferentes de mostrar estos mensajes por consola

// CONSOLE TABLE
const playerNames = [
    {name: 'Altuve', pos: '2b'},
    {name: 'Correa', pos: 'ss'},
    {name: 'Bregman', pos: '3b'},
];

console.table(playerNames);



// CONSOLE ERROR
// muy útil cuando se crean paquetes en npm
console.error('Oops!');



// WARN
// usarlo para advertir al usuario de algo
console.warn('Something is about to go wrong');
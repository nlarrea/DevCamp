const userOne = {
    firstName: "Naia",
    lastName: "Larrea"
}

const userTwo = {
    firstName: "Kristine",
    lastName: "Hudgens"
}

const fullName = function(){
    return `${this.lastName}, ${this.firstName}`;
}

const naia = fullName.bind(userOne);
const kristine = fullName.bind(userTwo);

console.log(naia());            // Larrea, Naia
console.log(kristine());        // Hudgens, Kristine

/* QUÉ ES LO QUE OCURRE
en lugar de tener que pasar el firstName y lastName de cada objeto como
argumento a la función, 'bind' nos permite 'unir' los objetos a la función, por
lo que no es necesario tener que pasar los argumentos, basta con usar 'this'
para acceder a las propiedades del objeto

esto es algo que se utiliza mucho en React
*/

/* NO USAR NUNCA ARROW FUNCTIONS PARA ESTO
arrow function cambia la forma en la que la palabra 'this' trabaja, por lo que
no se pueden utilizar arrow functions para realizar este tipo de ejercicios
*/
/* 
hasta ahora hemos visto que para crear una variable se usa la palabra clave
'var', pero esto puede llevarnos a errores en el código porque una variable
declarada con 'var' puede ser declarada nuevamente y sobreescribir la variable
anterior

para evitar esto -> utilizar 'let'
*/

let city = "Scottsdale";
console.log(city);      // Scottsdale



/* nueva forma de declarar variables -> CONST
las buenas prácticas dicen que cuanto más se use 'const', mejor
*/

city = "Phoenix";       // se cambia el valor de la variable -> puede que no queramos
console.log(city);      // Phoenix

// si queremos proteger el valor de una variable -> usar const

const city2 = "Scottsdale";
console.log(city2)      // Scottsdale

//city2 = "Phoenix";    // TypeError -> no podemos redefinir una constante



// STRING INTERPOLATION => formatear los strings

// forma antigua:
const lyrics = "Never gonna give you up";
console.log("I'm " + lyrics);   // I'm Never gonna give you up

// forma nueva:
console.log(`I'm ${lyrics}`);   // I'm Never gonna give you up

console.log(`${2 + 2}`);        // 4



// TERNARY OPERATORS -> if-else

/*
los ternary operators solo funcionan con sentencias if-else

SINTAXIS:

<condición> ? <qué ocurre si la condición es TRUE> : <qué ocurre si la condición es FALSE>
*/

const page = "Home";
console.log(`class=${page === 'Home' ? 'master-layout' : 'secondary-layout'}`);
// se imprime: class=master-layout
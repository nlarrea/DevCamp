// ES6 code goes here

// IMPORTAR UNA VARIABLE

/*
// importamos la constante 'greeting' del archivo 'helper'
import { greeting } from "./helper";
console.log(greeting);      // vemos que funciona correctamente
*/


// IMPORTAR UNA FUNCIÓN

/*
import { multiply } from "./helper";
console.log(multiply(2, 5));    // se imprime 10 en la consola -> funciona
*/


// IMPORTAR VARIOS ELEMENTOS A LA VEZ

/*
import { multiply, greeting } from "./helper";
console.log(greeting);
console.log(multiply(2, 8));
*/



// IMPORTAR TODO DE UN ARCHIVO A LA VEZ

import * as helper from "./helper";
console.log(helper.greeting);
console.log(helper.multiply(3, 4));
/* usando este método, tenemos que guardar todo lo importado en algun tipo de
variable-objeto -> le indicamos que 'importe todo como X' y llamamos a esa 'X'
para acceder a todo lo que se ha importado */
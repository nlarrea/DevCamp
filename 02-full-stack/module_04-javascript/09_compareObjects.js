// COMPROBAR SI LOS VALORES DE DOS OBJETOS SON IGUALES

const obj1 = {
    name: "Naia",
    age: 24
}

const obj2 = {
    name: "Naia",
    age: 24
}

// se ve que son dos objetos idénticos, pero si los comparamos:
console.log(obj1 === obj2);     // false
console.log(obj1 == obj2);      // false
/* esto se debe a que JS lo que hace es coger los dos objetos y sin tener en
cuenta sus valores, comparar desde dónde están guardados en la memoria, como
tienen diferentes nombres de variable, nos dice que no son iguales */



// CÓMO SABER SI TIENEN O NO LOS MISMOS VALORES?


const isEqual = (obj1, obj2) => {
    const obj1Keys = Object.keys(obj1);
    const obj2Keys = Object.keys(obj2);

    // comparar si tenemos la misma cantidad de 'keys'
    if(obj1Keys.length !== obj2Keys.length) return false;

    // comprobar que los valores son iguales
    for(let objKey of obj1Keys){
        if(obj1[objKey] !== obj2[objKey]) return false;
    }

    // si no ha devuelto 'false', es porque es true
    return true;
}

console.log(isEqual(obj1, obj2));

/*
esta solución funciona perfectamente para objetos de este tipo, pero si los
objetos tuvieran otros objetos en su interior, no funcionaría, volveríamos a
tener el mismo problema que teníamos al principio comparando 2 objetos

una forma de darle solución a esto, es usar una librería que permita comparar
objetos aunque tengan otros anidados

una librería que podría ser útil para esto es la librería 'Lodash'
*/
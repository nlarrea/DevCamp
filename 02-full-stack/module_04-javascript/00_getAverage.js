/* ENUNCIADO
queremos obtener el valor medio de una lista

[1, 2, 3] -> (1 + 2 + 3) / 3
*/

// MY SOLUTION

function myGetAverage(array){
    let total = array.reduce((acum, current) => acum + current);
    
    return total / array.length;
}

let array = [1, 2, 3];
console.log(myGetAverage(array));           // 2



// JORDAN'S SOLUTION

const getAverage = arr => {
    // sum the values from the array
    const reducer = (total, currentValue) => total + currentValue;      // function called reducer
    const sum = arr.reduce(reducer);
    
    // get the length of the array
    // divide the array sum by the length
    return sum / arr.length;
}

console.log(getAverage([1, 2, 3]));         // 2

/* 
ha hecho lo mismo que yo, pero creando una función llamada 'reducer' que es
pasada como argumento del método 'reduce'. Es lo mismo que he hecho yo, pero en
2 pasos porque dice que se lee más fácil así, y usando una 'arrow function'
*/
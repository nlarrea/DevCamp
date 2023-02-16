/* ENUNCIADO
Eliminar el primer y último elemento de un array
*/

const removeFirstAndLast = arr => {
    if(arr.length >= 3){
        return arr.slice(1, -1);
    } else{
        throw new Error("You need at least three element in the array");
    }
}

let array = ["ughhh", "good", "another good one", "uugggg"];
console.log(removeFirstAndLast(array));

// con este método, no se ve afectada la lista original
console.log(array);      // ["ughhh", "good", "another good one", "uugggg"]
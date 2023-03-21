/* ENUNCIADO
Teniendo este array:
[1, 2, 3, 4, 5]

El resultado debería ser el siguiente:
1
5
2
4
3
*/

class ArrayPopper {
    constructor(array) {
        this.arr = array;
        this.atBegginning = true;   // para saber si queremos el primer o último valor
    }

    togglePopper() {
        // cambia el valor de 'atBegginning' a justo el contrario
        this.atBegginning = !this.atBegginning;

        // si estamos al inicio, devuelve el primer elemento, sino, el último
        return this.atBegginning ? this.arr.pop() : this.arr.shift();
    }
}

const ap = new ArrayPopper([1, 2, 3, 4, 5]);
console.log(ap.togglePopper());     // 1
console.log(ap.togglePopper());     // 5
console.log(ap.togglePopper());     // 2
console.log(ap.togglePopper());     // 4
console.log(ap.togglePopper());     // 3
// console.log(ap.togglePopper());  // undefined


// funciona con cualquier lista -> es una clase
const strAp = new ArrayPopper(['Hi', 'there', 'from', 'JS']);
console.log(strAp.togglePopper());  // Hi
console.log(strAp.togglePopper());  // JS
console.log(strAp.togglePopper());  // there
console.log(strAp.togglePopper());  // from
console.log(strAp.arr);             // [] -> la lista se ha quedado vacía
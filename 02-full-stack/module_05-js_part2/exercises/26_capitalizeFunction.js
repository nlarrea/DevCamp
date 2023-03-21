/* ENUNCIADO
"Hi there" -> "Hi There"
"the quick brown fox jumped over the lazy dog" -> "The Quick Brown Fox Jumped Over The Lazy Dog"
*/

const toCapital = str => {
    const words = str.split(' ');
    return words.map(word => word[0].toUpperCase() + word.slice(1)).join(" ");
}

const shortStr = "Hi there";
const longStr = "the quick brown fox jumped over the lazy dog";

console.log(toCapital(shortStr));
/* imprime:
Hi There
*/

console.log(toCapital(longStr));
/* imprime:
The Quick Brown Fox Jumped Over The Lazy Dog
*/
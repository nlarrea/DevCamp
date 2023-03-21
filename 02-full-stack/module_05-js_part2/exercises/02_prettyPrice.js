/* ENUNCIADO
prettyPrice(3.50, 0.95) -> 3.95
prettyPrice(3.32, 0.95) -> 3.95
prettyPrice(3.32, 95) -> 3.95
prettyPrice(100, 0.95) -> 100.95
*/

const prettyPrice = (grossPrice, extension) => {
    if(Number.isInteger(extension)){
        extension /= 100;
    }

    return Math.floor(grossPrice) + extension;
}

console.log(prettyPrice(3.50, 0.95));       // 3.95
console.log(prettyPrice(3.32, 0.95));       // 3.95
console.log(prettyPrice(3.32, 95));         // 3.95
console.log(prettyPrice(100, 0.95));        // 100.95
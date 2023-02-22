/* ENUNCIADO
vamos a crear una función que tome dos argumentos y devuelva el exponente

toThePowerOf(2, 3) => 8

utilizar la función 'reduce'
*/

const toThePowerOf = (num, exp) => {
    // creamos una lista de 'exp' elementos y la rellenamos de 'num'
    const items = Array(exp).fill(num);

    return items.reduce((total, current) => total * current);
}

console.log(toThePowerOf(2, 3));        // 8
console.log(toThePowerOf(3, 3));        // 27

/*
si:
    - num = 2
    - exp = 3
entonces: items = [2, 2, 2]

por qué?
1. vuelta:
    total = 2
    current = 2
    devuelve un 2 * 2 = 4

2. vuelta:
    total = 4
    current = 2
    devuelve un 4 * 2 = 8

y acaba -> resultado = 8
*/
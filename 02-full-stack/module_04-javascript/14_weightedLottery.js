/* ENUNCIADO
imaginar que queremos crear un sistema que genere números aleatorios, pero no
queremos que esos números sean 100% aleatorios, queremos que algunos tengan más
probabilidad de aparecer que otros

TENIENDO ALGO ASÍ:
const weights = {
    winning: 1,
    losing: 1000
}

weightedLottery(weights)

si se llamara 1001 veces a la función, 1 vez debería salir 'winning' y 1000
veces 'losing'


o bien:
const weights = {
    green: 1,
    yellow: 2,
    red: 3
}

el objeto 'weights' debe ser variable


HINTS:
- Object.keys
- bitwise operators
*/

// MY SOLUTION

const weights = {
    green: 1,
    yellow: 2,
    red: 3
};

function weightedLottery(weights){
    // generar un index random entre 0 (incluido) y maxValue (no incluido)
    const getRandom = (maxValue) => Math.floor(Math.random() * maxValue);
    
    let containerArray = [];

    Object.keys(weights).forEach(key => {
        for(let i=0; i<weights[key]; i++){
            containerArray.push(key);
        }
    })

    return containerArray[getRandom(containerArray.length)];
}

console.log(weightedLottery(weights));



// JORDAN'S SOLUTION

const weightsJordan = {
    green: 1,
    yellow: 2,
    red: 3
};

const weightedLotteryJordan = weights => {
    let containerArray = [];

    Object.keys(weights).forEach(key => {
        for(let i = 0; i < weights[key]; i++){
            containerArray.push(key);
        }
    });

    // si el index no fuera correcto, tomaría el index = 0
    return containerArray[(Math.random() * containerArray.length) | 0];
}

console.log(weightedLotteryJordan(weightsJordan));
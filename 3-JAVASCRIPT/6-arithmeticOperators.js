// OPERATIONS WITH NUMBERS
console.log(2 + 2); // 4
console.log(2 - 3); // -1
console.log(10 / 2); // 5
console.log(2 * 10); // 20
console.log(2 ** 10); // 1024
console.log(5 % 2); // 1 -> useful to check if a number is even or odd

// INCREMENT AND DECREMENT
var num = 2;
console.log(num++); // 2 -> number has been printed and later incremented to 3
console.log(++num); // 4 -> number incremented to 4 and then has been printed
console.log(num--); // 4 -> number has been printed and later decremented to 3
console.log(--num); // 2 -> number decremented to 2 and then has been printed
//console.log(2++); // this returns an error -> to increment or decrement a number, it must be stored in a variable

// FLIP VALUES
var someNum = 10;
var someOtherNum = - someNum;
console.log(someOtherNum); // -10

var stringNum = '100';
var convertedNum = + stringNum;
console.log(convertedNum); // 100
console.log(typeof stringNum); // string
console.log(typeof convertedNum); // number
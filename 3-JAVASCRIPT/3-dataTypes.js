// BOOLEAN -> only two options
var truthy = true;
var notTruthy = false;

console.log(truthy); // true
console.log(notTruthy); // false



// NULL -> one possible value = null -> null = empty
var nully = null;

console.log(null); // null



// UNDEFINED -> it's what you get when something is simply declared and it's not given a value
/* undefined is good to check if something has been defined, but null is used to say that something is empty */
var notDefined;

console.log(notDefined); // undefined



// NUMBER
var age = 12;

console.log(age); // 12



// STRING
// both of these will work
var name = "Naia";
var nameTwo = 'Naia';

console.log(name); // Naia
console.log(nameTwo); // Naia



// SYMBOL -> new in ECMA 6 -> used to work with objects
var mySym = Symbol("foo");

console.log(mySym); // Symbol(foo)



// CHECK THE TYPE OF A DATA -> typeof
console.log(typeof truthy); // boolean
console.log(typeof nully); // object
console.log(typeof notDefined); // undefined
console.log(typeof age); // number
console.log(typeof nameTwo); // string
console.log(typeof mySym); // symbol



// TYPECASTING
console.log('100' - 42); // 58

console.log(100 + null); // 100 -> it's like 100 + empty

// this won't work as a mathematical operation
console.log('100' + 42); // 10042
console.log(42 + '100'); // 42100
// this is how it should be done
console.log(Number('100') + 42); // 142

var ageOne = 12;
// CONVERT NUMBER INTO STRING -> this two makes the same
String(ageOne); // '12'
ageOne.toString(); // '12'

// STRING INTO NUMBER
var numberTwo = '33.5';
console.log(Number(numberTwo)); // 33.5
console.log(parseInt(numberTwo)); // 33
console.log(parseFloat(numberTwo)); // 33.5

console.log(parseInt('55555555 is my phone number')); // 55555555
console.log(parseInt('foo 55555555 is my phone number')); // NaN -> Not a Number
// we need to have something that can be converted into a number at the beggining of the string

console.log(typeof numberTwo); // string
console.log(+ numberTwo); // 33.5 -> converts the string into a number
console.log(typeof + numberTwo); // number

console.log(Number(true)); // 1
console.log(Number(false)); // 0
// HOW TO CREATE ARRAYS - SYNTAX
var generatedArray = new Array(3); // array with 3 elements
console.log(generatedArray.length); // 3
console.log(generatedArray); // [ , , ]

var generatedArray = new Array('Altuve', 'Correa', 'Spring');
console.log(generatedArray.length); // 3
console.log(generatedArray); // ['Altuve', 'Correa', 'Spring']

// the more common way to create an array
var literalArray = [1,2,3];
console.log(literalArray.length); // 3
console.log(literalArray); // [1, 2, 3]

// we can combine any type of data -> strings, numbers, other lists, objects, functions, etc.
var mixedArray = ['Hi', 1, ["a", "b", "c"], {name: "Cris"}, function greeting(){console.log("Hello World!")}];



// CALL ELEMENTS
console.log(generatedArray[0]); // Altuve
var playerName = generatedArray[1]; // we can store this data in variables
console.log(playerName); // Correa

console.log(mixedArray[0]); // Hi
console.log(mixedArray[1]); // 1
console.log(mixedArray[2]); // ['a','b','c']
console.log(mixedArray[2][1]); // b
console.log(mixedArray[3]); // {name: 'Cris'}
console.log(mixedArray[3].name); // Cris
console.log(mixedArray[4]()); // prints: Hello World!



// ADD AND REMOVE ELEMENTS FROM AN ARRAY -> .pop(), .push(), .shift() and .unshift()
var arr = ['Altuve', 'Bregman', 'Correa', 'Springer'];
console.log(arr.length); // 4

// remove item
console.log(arr.pop()); // Springer
console.log(arr); // [ 'Altuve', 'Bregman', 'Correa' ]
/* when we remove an item using .pop(), the item is removed but also, it is "taken" from the array,
so we can console.log() it and see if it's been removed */

// add item
console.log(arr.push('Baggwell')); // 4 -> the new length of the array
console.log(arr); // [ 'Altuve', 'Bregman', 'Correa', 'Baggwell' ]

var elementPopped = arr.pop();
console.log(elementPopped); // Baggwell

// remove item from the beggining of the array -> .shift()
console.log(arr.shift()); // Altuve
console.log(arr); // [ 'Bregman', 'Correa' ]

// add item at the beggining -> .unshift()
console.log(arr.unshift("Kyle")); // 3 -> the new length of the array
console.log(arr); // [ 'Kyle', 'Bregnan', 'Correa' ]



// REMOVE SPECIFIC ARRAY ELEMENTS -> .splice()
var arr = ['Altuve', 'Bregman', 'Correa', 'Springer'];
console.log(arr.splice(2, 1)); // [ 'Correa' ]
/* the first number is the index and the second is the quantity of elements you wanna remove */

var arr = ['Altuve', 'Bregman', 'Correa', 'Springer'];
var foundElement = arr.indexOf('Correa');
console.log(arr.splice(foundElement, 1)); // [ 'Correa' ]
/* splice removes the indicated elements, but also it returns an array with those elements */

// we can remove more than one items at a time
console.log(arr.splice(1, 2)); // [ 'Bregman', 'Springer' ]
console.log(arr); // [ 'Altuve' ]
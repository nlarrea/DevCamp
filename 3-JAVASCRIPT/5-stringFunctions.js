// CREATE A STRING VARIABLE
var str = 'The quick brown fox jumped over the lazy dog';

// LENGTH ATRIBUTE
console.log(str.length); // 44 -> this is an atribute, not a function

// HOW TO GET THE CHARACTER AT A SPECIFIC POSITION
console.log(str.charAt(2)); // e
console.log(str.charAt(200)); // [empty string] -> ""

// CONCAT STRINGS
console.log(str.concat(' again and again')); // The quick brown fox jumped over the lazy dog again and again
console.log(str); // The quick brown fox jumped over the lazy dog
// .concat() doesn't change the value of str, if we want maintain the value, it should be saved in a variable
var newStr = str.concat(' again and again');
console.log(newStr); // The quick brown fox jumped over the lazy dog again and again

// CHECK IF A STRING INCLUDES ANOTHER STRING / CHAR
console.log(str.includes('quick')); // true
console.log(str.includes('foo')); // false

// CHECK IF A STRING STARTS OR ENDS WITH ANOTHER STRING / CHAR
console.log(str.startsWith('The')); // true
console.log(str.startsWith('THe')); // false -> it's case sensitive
console.log(str.endsWith('g')); // true
console.log(str.endsWith('lazy dog')); //true
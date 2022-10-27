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

// REPEAT A STRING
console.log(str.repeat(5)); // repeats the string 5 times -> doesn't change the original string
console.log(str); // The quick brown fox jumped over the lazy dog

// REGULAR EXPRESSIONS -> a pattern-matching system
// takes a regular expression and returns if there is a match
console.log(str.match(/((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}/)); // null -> makes sense because str is not a phone number
console.log('(555)555-5555'.match(/((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}/)); // returns a match
/* imagine we have an email field and wanna be shure that the user has typed in an email correctly, then we could use
a regular expression and check if the email pattern is correct */

// REPLACE -> doesn't change the original string
console.log(str.replace('fox', 'wolf')); // The quick brown wolf jumped over the lazy dog
console.log(str); // The quick brown fox jumped over the lazy dog

// SEARCH
console.log('555-555-5555 is my phone number'.search(/((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}/)); // 0
/* this returns the index -> 0 means that .search() has found the pattern and its index starts at 0.
If it doesn't find the pattern, it returns a negative value */
console.log('foo'.search(/((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}/)); // -1 -> doesn't find it
console.log('foo 555-555-5555 is my phone number'.search(/((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}/)); // 4 -> finds it, starts at index 4

// FIND THE INDEX OF SOMETHING
console.log(str.indexOf('jumped')); // 20 -> returns the index of the FIRST element that it finds
var str2 = str.concat(' again and again');
console.log(str2.indexOf('again')); // 45 -> doesn't return the index of the second 'again'
console.log(str2.lastIndexOf('again')); // 55

// SLICE
console.log(str); // The quick brown fox jumped over the lazy dog
console.log(str.charAt(10)); // b -> just to know where what char will be at that position
console.log(str.slice(10)); // brown fox jumped over the lazy dog -> grabs everything from the index=10 to the end
// we can work from right to left by using negative numbers
console.log(str.slice(-8)); // lazy dog -> returns the last 8 chars
// if we want part of the middle of the string -> use 2 arguments
console.log(str.slice(4, 9)); // quick -> starts at index=4 and finish at index=8 (doesn't take the char at 9)

// TRIM -> quits spaces from start or end of the string
var messyStr = '       foo       ';
console.log(messyStr.trim()); // 'foo'
console.log(str.slice(4, 10).trim()); // quick
/* str.slice(4,10) returns 'quick ', but using .trim() deletes the space char at the end */

// UPPERCASE OR LOWERCASE
console.log(str.toUpperCase()); // THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG
console.log(str.toLowerCase()); // the quick brown fox jumped over the lazy dog
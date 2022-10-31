// WHAT IS HOISTING
/* is a way that JavaScript reads variables */

name = "Naia";
console.log("Naia"); // this works -> Naia
var name;

/* this only work with declarations, this wouldn't work: */

console.log(age); // this prints an "undefined"
var age = 15;

/* even if the declarations can be written at the end of the page, the best practise is to
always declare things before using them */
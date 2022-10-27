// VAR AND LET

var name = "Naia";
name; // Naia
console.log(name); // Naia

// alert(name); // makes an alert in the browser, but doesn't work in VSCode with Quokka

var age2 = 28;
let name2 = "Cristina";
console.log(name2); // Cristina
console.log(age2); // 28


// DECLARE MORE THAN ONE VARIABLES AT A TIME
var name3, city, age3;
name3 = "June";
city = "Bilbao";
age3 = 24;
console.log(name3); // June
console.log(city); // Bilbao
console.log(age3); // 24


// DIFFERENCE BETWEEN VAR AND LET
var number = 12;
console.log(number); // it works -> 12

var number = 15;
console.log(number); // still works -> 15

// let's do it with LET

let numberLet = 12;
console.log(numberLet); // 12

//let numberLet = 15; // this gives an error saying that 'numberLet' has already been declared
//console.log(numberLet); // 12

/* whenever we wanna have some type of variable that we don't wanna have accidentally overriden, is better
to use LET than VAR */
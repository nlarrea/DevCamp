// SYNTAX

// void function -> doesn't return anything
function greets(){
	console.log("Hello world!");
}
greets(); // the 'Hello world!' prints inside the function

function greetsTwo(){
	return 'Hello world!';
}
greetsTwo(); // nothing will be printed

var storedText = greetsTwo();
console.log(storedText); // Hello world!



// VARIABLE SCOPE
var userOutside = {
	email: 'outside@devcamp.com',
	fullName: 'Outside User'
}
function outsideVar(){
	console.log('Hi there, '.concat(userOutside.fullName));
}
outsideVar(); // prints: Hi there, Outside User -> works perfectly
console.log(userOutside.email); // outside@devcamp.com

// if the var is declared inside the function, it won't be accessible from outside
function insideVar(){
	var userInside = {
		email: 'inside@devcamp.com',
		fullName: 'Inside User'
	}
	console.log('Hi there, '.concat(userInside.fullName));
}
insideVar(); // prints: Hi there, Inside User -> works because the log is inside the function
// if we try to console.log the var out of the function, it won't work:
//console.log(userInside.email); // an error appears saying that userInside variable is not defined

function example(){
	exampleVar = true; // this doesn't seem to be declared, but we have create a new global variable
	return exampleVar;
}
console.log(example()); // true
console.log(exampleVar); // true -> the same as declaring a 'var' type variable outside the function



// DIFFERENCES BETWEEN FUNCTION EXPRESSIONS AND DECLARATIONS
// this is a function declaration
function greeting(){
	return 'Hi there!';
}

// this is a function expression -> function that is stored inside a variable
var greetingExp = function (){
	return 'Hi there again!';
}; // could add the semicolon at the end
console.log(greeting()); // Hi there!
console.log(greetingExp()); // Hi there again!

// why would we want this?
var age = 3;
if(age <= 10){
	var buildMenu = function (){
		return "Kid's menu";
	};
	/* function buildMenuTwo(){
		return "Another kid's menu";
	} */
	var buildMenuTwo = function (){
		return "Another kid's menu";
	}
	// seems that both are working correctly
	console.log(buildMenu()); // Kid's menu
	console.log(buildMenuTwo()); // Another kid's menu
	/* but actually, the second one is gonna give us an error, because we shouldn't build functions
	inside other blocks, so we should use two function expressions here (changing the second one) */
}



// FUNCTION ARGUMENTS
function fullName(firstName, lastName){
	return lastName.toUpperCase() + ", " + firstName.toUpperCase();
}
// if we don't give two parameters, it will give us an error
console.log(fullName('Naia', 'Larrea')); // LARREA, NAIA

function sample(arg1, arg2){
	console.log(arg1);
	console.log(arg2);
}
// if we don't give two parameters, there's no error, but it won't be working as it should
sample();

function fullNameTwo(firstName, lastName, language){
	// if a language is set, it's gonna use it, but if not, 'English' is printed as language
	var language = language || 'English'; // one way to set default values
	return lastName.toUpperCase() + ", " + firstName.toUpperCase() + " - " + language;
}
console.log(fullNameTwo("Naia", "Larrea")); // LARREA, NAIA - English
console.log(fullNameTwo("Naia", "Larrea", "Spanish")); // LARREA, NAIA - Spanish

// other way to set default values for arguments
function fullNameThree(firstName, lastName, language = 'English'){
	return lastName.toUpperCase() + ", " + firstName.toUpperCase() + " - " + language;
}
console.log(fullNameTwo("Naia", "Larrea")); // LARREA, NAIA - English
console.log(fullNameTwo("Naia", "Larrea", "Spanish")); // LARREA, NAIA - Spanish



// ARGUMENTS: REFERENCE VS VALUE
var someUser = {
	name: "Naia"
}
function nameFormatter(user){
	return user.name = "Oops";
}
console.log(nameFormatter(someUser)); // Oops -> this was expected
console.log(someUser.name); // Oops -> this is not what we wanted -> the value has changed

var someName = "Cris";
function otherNameFormatter(name){
	return name = "Oops";
}
console.log(otherNameFormatter()); // Oops -> expected
console.log(someName); // Cris -> doen't change the value

/* objects are passed using their reference, so its values will change. But other variable types like strings, numbers,
etc. will be passed usign their value, so they're not gonna change */

// what if we need to pass an object then? -> pass the actual value itself
var otherUser = {
	name: "June"
}
function objNameFormatter(someUser){
	return someUser = "Oops";
}
console.log(objNameFormatter(otherUser.name)); // Oops -> expected
console.log(otherUser.name); // June -> now it works right
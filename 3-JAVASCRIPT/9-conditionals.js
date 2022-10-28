// SYNTAX

// EQUALS
var age = 12;
var age2 = '12';
if(age == age2){ // not strict equal -> doesn't check the data type
	console.log("They are equal"); // prints
}
if(age === age2){ // strict equal -> checks the type of the data too
	console.log("They are equal"); // doesn't print
}

// NOT EQUALS
if(age != age2){
	console.log("They're not equal"); // won't print because it thinks they're equals
}
if(age !== age2){
	console.log("They're not equal"); // prints
}

// GREATER - GREATER OR EQUAL
if(age > 10){
	console.log("First is bigger"); // prints
}
if(age >= age2){
	console.log("First is bigger or equal"); // prints
}

// LESS - LESS OR EQUAL
if(age < 15){
	console.log("First is bigger"); // prints
}
if(age <= age2){
	console.log("First is bigger or equal"); // prints
}



// IF - ELSE
var age = 30;
if(age <= 10){
	console.log("You can eat from kid's menu"); // won't be printed
} else {
	console.log("Adult menu time for you!"); // will be printed
}



// IF - ELSE IF - ELSE
var age = 8;
if(age <= 10){
	console.log("You can eat from kid's menu");
	console.log("You're not old enough to drive");
	console.log("You're not old enough to rent a car");
	
} else if (age>10 && age<25){
	console.log("You can not eat from kid's menu");
	console.log("You're old enough to drive");
	console.log("You're not old enough to rent a car");
} else {
	console.log("You can not eat from kid's menu");
	console.log("You're old enough to drive");
	console.log("You're old enough to rent a car");
}



// SWITCH
var dataPoint = "Hi there";
switch(typeof dataPoint){
	case "string":
		console.log("It is a string");
		break;
	case "number":
		console.log("It is a number");
		break;
	case "boolean":
		console.log("It is either true or false");
		break;
	default:
		console.log("No matches");
		// doesn't need a 'break'
}



// TERNARY OPERATORS
function ageVerification(age){
	/*
	if(age > 25){
		console.log("You can rent a car");
	} else {
		console.log("You're not old enough yet")
	}
	*/
	let answer = age > 25 ? "You can rent a car" : "You're not old enough yet";
	console.log(answer);
}
ageVerification(15); // prints: You're not old enough yet
ageVerification(55); // prints: You can rent a car

function adminControls(user){
	/*
	if(user){
		if(user.admin){
			console.log("showing admin controls...");
		} else {
			console.log("you need to be an admin");
		}
	} else {
		console.log("you need to be logged in");
	}
	*/
	let response = user ? (user.admin ? "showing admin controls..." : "you need to be an admin") : "you need to be logged in";
	console.log(response);
}
let user1 = {
	name: 'Naia',
	admin: true
}
adminControls(user1); // prints: showing admin controls...
let user2 = {
	name: 'Cristina',
	admin: false
}
adminControls(user2); // prints: you need to be an admin
let user3 = null;
adminControls(user3); // prints: you need to be logged in
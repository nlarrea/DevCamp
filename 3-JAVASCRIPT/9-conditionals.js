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
	console.log("You're not old enought to drive");
	console.log("You're not old enought to rent a car");
	
} else if (age>10 && age<25){
	console.log("You can not eat from kid's menu");
	console.log("You're old enought to drive");
	console.log("You're not old enought to rent a car");
} else {
	console.log("You can not eat from kid's menu");
	console.log("You're old enought to drive");
	console.log("You're old enought to rent a car");
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
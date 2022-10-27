// OBJECTS WITH ONE ATRIBUTE
var user = {name: "Cristina"};

console.log(user); // {name: 'Cristina'}
console.log(user.name); // Cristina

user.name = "Naia";
console.log(user.name); // Naia



// OBJECTS WITH MORE ATRIBUTES
var user = {
	name: "Cristina",
	age: 28,
	city: "Murcia"
}

console.log(user.age); // 28



// NESTED OBJECTS -> one object inside another
var user = {
	name: "Cristina",
	age: 28,
	city: "Murcia",
	grades: {
		math: 90,
		science: 80,
		languageArts: 100
	}
}

console.log(user.grades.math); // 90



// ADD OR UPDATE DATA FROM AN OBJECT
user.grades.coding = 99; // adds a new key in grades

console.log(user.grades); // { math: 90, science: 80, languageArts: 100, coding: 99 }
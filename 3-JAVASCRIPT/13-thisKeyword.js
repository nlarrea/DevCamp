class Person {
	constructor(name){
		this.name = name;
	}
}

const yourPerson = new Person("Naia");
const secondPerson = new Person("Cris");
console.log(yourPerson); // Person { name: 'Naia' }
console.log(secondPerson); // Person { name: 'Cris' }
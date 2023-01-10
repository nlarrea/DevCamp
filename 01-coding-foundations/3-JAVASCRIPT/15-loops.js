var players = [
	'Altuve',
	'Bregman',
	'Correa',
	'Springer'
];

// FOR -> for(declatarion, condition, incrementer)
for(let i=0; i<players.length; i++){
	console.log(players[i]);
	/* prints:
		Altuve
		Bregman
		Correa
		Springer
	*/
}

// FOR IN
for(var player in players){
	// 'player' represents the index, not the value
	console.log(players[player]);
	/* prints:
		Altuve
		Bregman
		Correa
		Springer
	*/
}

// FOREACH
players.forEach(function(element){
	console.log(element);
	/* prints:
		Altuve
		Bregman
		Correa
		Springer
	*/
});



// FOR IN -> LOOP OVER OBJECTS
var student = {
	name: "Naia",
	age: 24,
	city: "Bilbao"
};

for(var key in student){
	console.log(key + " => " + student[key]);
	/* prints:
		name => Naia
		age => 24
		city => Bilbao
	*/
	/* normally we use 'student.key' syntax, but here wouldn't work. 'key' is not a true key, it's an
	iterator variable, so we have to use those [] -> student[key] */
}



// WHILE
var players = [
	'Altuve',
	'Bregman',
	'Correa',
	'Springer'
];

var i = 0;
while(i < players.length){
	console.log(players[i]);
	i++; // DO NEVER FORGET THIS!
	/* this loop prints:
		Altuve
		Bregman
		Correa
		Springer
	*/
}



// DO - WHILE
var i = 0;
do{
	console.log(players[i]);
	i++; // DO NEVER FORGET THIS!
	/* this loop prints:
		Altuve
		Bregman
		Correa
		Springer
	*/
}while(i < players.length);


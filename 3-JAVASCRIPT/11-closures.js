function battingAverage(){
	// local variables
	var hits = 100;
	var atBats = 300;
	// closures
	return { // returns an object with two methods
		getCurrenAverage: function(){ // this is how methods are made inside objects
			return (hits / atBats);
		},
		updateHitsAndAtBats: function(hit, atBat){
			hits += hit;
			atBats += atBat;
		}
	}
}
var altuve = battingAverage();
console.log(altuve.getCurrenAverage()); // 0.333333333333333 -> it works
altuve.updateHitsAndAtBats(0, 20); // updates the values of 'hits' and 'atBats'
console.log(altuve.getCurrenAverage()); // 0.3125 -> new value because we updated the values
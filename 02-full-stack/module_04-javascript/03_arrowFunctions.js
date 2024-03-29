// FUNCIONES FLECHA

// regular function declaration
function fullName(fName, lName){
    console.log(`${fName} ${lName}`);   // Naia Larrea
}

fullName("Naia", "Larrea");


// function expression -> cuadno la guardamos en una variable
const fullNameExpression = function(fName, lName){
    console.log(`${fName} ${lName}`);   // Naia Larrea
}

fullNameExpression("Naia", "Larrea");


// arrow function
const helloWorld = () => {
    console.log("Hello World!");        // Hello World!
}

helloWorld();



// ARROW FUNCTION WITH SINGLE ARGUMENT

const firsName = fName => {console.log(fName.toUpperCase());}     // NAIA
firsName("Naia");
// si solo usamos 1 argumento, no son necesarios los paréntesis, sino si lo son



// ARROW FUNCTION WITH MORE ARGUMENTS

const fullNameArrow = (fName, lName) => {
    console.log(`${fName} ${lName}`);   // Naia Larrea
}
fullNameArrow("Naia", "Larrea");
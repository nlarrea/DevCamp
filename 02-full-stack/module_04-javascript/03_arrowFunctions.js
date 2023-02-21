// FUNCIONES FLECHA

// regular function declaration
function fullName(fName, lName){
    console.log(`${fName} ${lName}`);   // Naia Larrea
}

fullName("Naia", "Larrea");


// function expression -> cuadno la guardamos en una variable
fullNameExpression = function(fName, lName){
    console.log(`${fName} ${lName}`);   // Naia Larrea
}

fullNameExpression("Naia", "Larrea");


// arrow function
helloWorld = () => {
    console.log("Hello World!");        // Hello World!
}

helloWorld();



// ARROW FUNCTION WITH SINGLE ARGUMENT

firsName = fName => {console.log(fName.toUpperCase());}     // NAIA
firsName("Naia");
// si solo usamos 1 argumento, no son necesarios los paréntesis, sino si lo son



// ARROW FUNCTION WITH MORE ARGUMENTS

fullNameArrow = (fName, lName) => {
    console.log(`${fName} ${lName}`);   // Naia Larrea
}
fullNameArrow("Naia", "Larrea");
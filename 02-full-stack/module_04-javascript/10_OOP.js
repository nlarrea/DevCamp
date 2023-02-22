// INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS

class Instructor {
    // al constructor se le llama cada vez que se crea una instancia
    // siempre que pasemos algo al constructor, lo haremos en forma de objeto
    constructor({name, role = "assistant"}){
        this.name = name;
        this.role = role;
    }

    // INSTANCE METHOD
    renderDetails(){
        console.log(`${this.name}: ${this.role}`);
    }

    // STATIC METHOD
    static helloWorld(){
        console.log("Hi there");
    }

    static canTeach(instructor){
        return (instructor.role === "classroom");
    }
}

/* tenemos que pasar el parámetro del 'name' sí o sí, pero el de 'role' no es
obligatorio, porque tiene un valor por defecto */
const jon = new Instructor({name: "Jon Snow"});
// 'jon' es una instancia de 'Instructor'
const brayden = new Instructor({name: "Brayden", role: "teacher"});
const alice = new Instructor({name: "Alice", role: "classroom"});

console.log(jon);           // Instructor { name: 'Jon Snow', role: 'assistant' }
console.log(jon.name);      // Jon Snow



// INSTANCE METHOD
jon.renderDetails();        // Jon Snow: assistant
brayden.renderDetails();    // Brayden: teacher



// STATIC METHOD
Instructor.helloWorld();    // Hi there
/*
los métodos estáticos no necesitan que haya un objeto instanciado para que
se utilicen, y deben ser llamados SIEMPRE desde la propia clase, no desde una
instancia de la misma

si intentáramos hacer
    jon.helloWorld();
no funcionaría



CUÁNDO VAMOS A QUERER USAR ESTE TIPO DE MÉTODOS?
una clase solo debería tener un trabajo, hay que saber escoger cuándo este tipo
de método debe usarse y cuándo no

vamos a verlo con un ejemplo más abajo, pero principalmente, son métodos de
ayuda, les podemos pasar una instancia entera de la clase y acceder a ella, lo
cual puede ser muy útil en determinadas ocasiones para comprobar ciertos datos
*/
// por ejemplo:
console.log(
    `${jon.name} can teach: ${Instructor.canTeach(jon)}`
);      // Jon Snow can teach: false

console.log(
    `${alice.name} can teach: ${Instructor.canTeach(alice)}`
);      // Alice can teach: true
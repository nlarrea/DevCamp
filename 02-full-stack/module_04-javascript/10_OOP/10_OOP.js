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
}

/* tenemos que pasar el parámetro del 'name' sí o sí, pero el de 'role' no es
obligatorio, porque tiene un valor por defecto */
const jon = new Instructor({name: "Jon Snow"});
// 'jon' es una instancia de 'Instructor'
const brayden = new Instructor({name: "Brayden", role: "teacher"});

console.log(jon);           // Instructor { name: 'Jon Snow', role: 'assistant' }
console.log(jon.name);      // Jon Snow



// INSTANCE METHOD
jon.renderDetails();        // Jon Snow: assistant
brayden.renderDetails();    // Brayden: teacher
// 'THIS' EN LAS ARROW FUNCTIONS

function Invoice(subtotal){
    this.taxRate = 0.06;
    this.subtotal = subtotal;

    /* esto no funciona con funciones normales -> los setInterval no pueden
    acceder a los valores de la función en la que se encuentran (taxRate y subtotal)
    
    this.total = setInterval(function totalNumbers(){
        console.log((this.taxRate * this.subtotal) + this.subtotal);
    }, 2000);
    */

    /* con las arrow function, los setInterval sí tienen acceso a los valores
    de la función en la que se encuentran */
    this.total = setInterval(() => {
        console.log((this.taxRate * this.subtotal) + this.subtotal);
    }, 2000);

}
/* estamos creando la función Invoice como si fuera una clase -> antiguamente
no había forma de realizar programación orientada a objetos con JS */

const inv = new Invoice(200);
console.log(inv);               // Invoice { taxRate: 0.06 }

// con la función normal:
// console.log(inv.total);      // NaN

// con la arrow function:
console.log(inv.total());       // 212
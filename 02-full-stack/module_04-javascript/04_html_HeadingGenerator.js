// HTML HEADING GENERATOR

/* ENUNCIADO
una función flecha que reciba:
    - un título
    - tipo de encabezado
y devuelva el título generado en formato HTML

por ejemplo, enviando esto a la función:
    headingGenerator('Hi there', 1)

que devuelva lo siguiente:
    <h1>Hi there</h1>
*/

headingGenerator = (title, hType) => {
    return `<h${hType}>${title}</h${hType}>`;
}

console.log(headingGenerator('Hi there', 1));       // <h1>Hi there</h1>
console.log(headingGenerator('Greetings', 2));      // <h2>Greetings</h2>
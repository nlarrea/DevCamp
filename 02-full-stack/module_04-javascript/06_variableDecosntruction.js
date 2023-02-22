// DECONSTRUCCIÓN DE VARIABLES

// antes el intercambiar los valores de las variables se hacía así:
let playerOne = "Tiffany";
let playerTwo = "Kristine";

let tempPlayerOne = playerOne;
let tempPlayerTwo = playerTwo;

playerOne = tempPlayerTwo;
playerTwo = tempPlayerOne;

console.log(`
    Player One: ${playerOne}\n
    Player Two: ${playerTwo}
`);

/* se imprime:
Player One: Kristine
Player Two: Tiffany

se intercambian los valores, pero es una forma horrible de hacerlo
*/


// ahora, se puede hacer así:
[playerOne, playerTwo] = [playerTwo, playerOne];

console.log(`
    Player One: ${playerOne}\n
    Player Two: ${playerTwo}
`)



// ARRAY DESTRUCTURING

/* esto nos permite obtener cada uno de los elementos de un array para guardar
cada uno en una variable, por ejemplo */

const apiList = [
    "https://api.dailysmarty.com/posts",
    "https://api.github.com/users/jordanhudgens/repos",
    "https://api.github.com/users/jordanhudgens"
];

/*
const posts = apiList[0];
console.log(posts);         // https://api.dailysmarty.com/posts
// esto funciona, pero es poco eficiente
*/

// así es como se hace

const [posts, repos, profile] = apiList;
console.log(posts);         // https://api.dailysmarty.com/posts
console.log(repos);         // https://api.github.com/users/jordanhudgens/repos
console.log(profile);       // https://api.github.com/users/jordanhudgens



// DECONSTRUCTION IN FUNCTIONS -> objects

const user = {
    name: "Naia",
    email: "myemail@example.com"
}

/* vamos a usar una arrow function -> se le pasa un objeto (usar las llaves), y
los parámetros tienen que tener el mismo nombre que en el objeto */
const renderUser = ({name, email}) => {
    console.log(`${name}: ${email}`);
};

renderUser(user);       // Naia: myemail@example.com



// DEFAULT VALUES IN OBJECTS

const blog = {
    title: "My great post",
    summary: "Summary of the post"
}

const openGraphMetadata = ({title, summary = "A DailySmarty Post"}) => {
    console.log(`
        og-title=${title}
        og-description=${summary}
    `);
};

openGraphMetadata(blog);
/* se imprime:
    og-title=My great post 
    og-description=Summary of the post
*/

// si usamos un objeto sin 'summary':
const anotherBlog = {title: "My title"};
openGraphMetadata(anotherBlog);
/* se imprime:
    og-title=My title 
    og-description=A DailySmarty Post 
*/

// APIs CON ASYNC-AWAIT

/* APIs que vamos a llamar:
- dailysmarty: https://api.dailysmarty.com/posts
- github: https://api.github.com/users/nlarrea/repos
*/

async function queryApis(){
    const postsPromise = fetch("https://api.dailysmarty.com/posts");
    const posts = await postsPromise.then(res => res.json());
    console.log(posts);

    const reposPromise = fetch("https://api.github.com/users/nlarrea/repos");
    const repos = await reposPromise.then(res => res.json());
    console.log(repos);
}

queryApis();

/* 
como hemos usado asyn-await, se realizarán las llamadas al API siguiendo el
orden en el que se han escrito dichas llamadas dentro de la función asíncrona
'quetyApis' sin importar el tiempo que tarde en llegar la respuesta de ninguna
de las dos llamadas
*/
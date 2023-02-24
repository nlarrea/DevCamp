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
// CÓMO TRABAJAR CON LOS ERRORES

/* 
habrá ocasiones en las que llamemos a un API y, por el motivo que sea, se nos
devolverá un error

en este apartado se van a ver 2 formas diferentes de tratar con los errores
- try-catch
- 
*/

/* try-catch
este método tiene un problema: si falla una llamada a un API, no sabemos ni
cuál falla ni por qué

para solucionar eso, deberíamos meter cada llamada a APIs dentro de su propio
bloque try-catch
*/
async function queryApis(){
    try{
        const postsPromise = fetch("https://api.dailysmarty.com/posts");
        const posts = await postsPromise.then(res => res.json());
        console.log(posts);
    } catch(err){
        console.log(err);
        console.log("There was an error with the DailySmarty API");
    }

    try{
        const reposPromise = fetch("https://api.github.com/users/nlarrea/repos");
        const repos = await reposPromise.then(res => res.json());
        console.log(repos);
    } catch(err){
        console.log(err);
        console.log("There was an error with the GitHub API")
    }
}

queryApis();
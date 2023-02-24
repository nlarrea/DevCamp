/* CALLBACK

*/

/* user logins system - steps to follow:
verify credentials
    - si esto sale bien -> redireccionar al dashboard
        - actualizar la DB -> indicar inicio de sesión
            - llamada al API para obtener data
esto puede tardar mucho

async-await permiten hacerlo de forma mucho más sencilla
*/

// simulación de llamada a login() -> obtener credenciales de usuario
const login = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("User logged in")
        }, 2000);
    });
}

// simulación de llamada a updateAccount() -> actualizaría el estado a 'logged'
const updateAccount = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Updating last login...");
        }, 2000);
    });
}

/* si 'updateAccount' ocurre antes que 'login' -> error

primero hay que asegurarse de que el login se ha hecho correctamente

tal y como está el código ahora, lo primero que se va a ejecutar va a ser
aquello que ocurra antes, sin importar cuál queramos que se ejecute primero

para hacer que las cosas se ejecuten en el orden que queremos -> async-await
*/

async function loginActivities(){
    const returnedLogin = await login();
    /* esta función va a llamar al login(), con el 'await' le indicamos que no
    queremos que se ejecute nada más hasta que el login() haya terminado
    
    cuando haya terminado, guardará la respuesta de login() en la constante
    */
    console.log(returnedLogin);
    /* si ejecutamos ahora:
    se esperan 2 segundos (los del setTimeout del login) y login() devuelve el
    string que le hemos dicho que devuelva
    
    se imprime: 'User logged in' */
    // repetimos ahora lo mismo con updateAccount:
    const returnedUpdateAccount = await updateAccount();    // llama y espera respuesta
    console.log(returnedUpdateAccount);
    /* se imprime:
    User logged in
    Updating last login... */
}

loginActivities();


/* ASYNC-AWAIT
permite crear un flujo de trabajo, una especie de lista u orden que queramos
seguir a la hora de ejecutar funciones asíncronas
*/
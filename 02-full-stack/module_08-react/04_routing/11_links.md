# Links

En el apartado anterior se habló de los `NavLink`, en este, sin embargo, se hablará de forma superficial sobre los elementos `Link`.

<br/>

Vamos a ver un ejemplo trabajando dentro del archivo `blog.js`. Vamos a crear un link que nos lleve a la ruta *'/about-me'*:

```jsx
// ...
import { Link } from 'react-router-dom';

export default function() {
    return (
        <div>
            <h2>Blog</h2>

            <div>
                <Link to='/about-me'>Read more about myself'</Link>
            </div>
        </div>
    )
}
```

<br/>

Con estas líneas se consigue que cada vez que el usuario esté en la ruta *'blog'*, le aparezca un link. Si el ususario clica dicho link, será enviado a la ruta *'/about-me'*.

<br/>

**¿Cuál es la diferencia respecto a `NavLink`?**

A priori puede parecer que ambos elementos funcionan de la misma forma, y en cierto modo, así es. Sin embargo, `NavLink` tiene una funcionalidad extra y es que, entre otras cosas, añade la clase `active` al elemento que se está visitando. Esto es muy útil para, por ejemplo, añadir un estilo diferente a la ruta que se está visitando. Por no hablar de que permite modificar el nombre de la clase para que en vez de ser `active` sea el nombre que nosotros queramos.
# Archivos de estilos utilizados

Para estilar la página web se ha hecho uso de SCSS, donde estos son los archivos creados y utilizados en el proyecto:

* [index.scss](#index)
* [_common.scss](#common)
* [_nav.scss](#nav)
* [_buttons.scss](#buttons)
* [_page-container.scss](#page-container)
* [_media-queries.scss](#media-queries)

<br><hr>
<hr><br>

<h2 id="index">index.css</h2>

Como ya se ha mencionado, se ha utilizado SCSS para estilar la página web. En el archivo HTML se ha linkado el archivo *"index.css"* que se crea automáticamente al compilar SCSS a CSS. El archivo index.scss contiene las siguientes líneas de código:

```SCSS
@use "common";
@use "nav";
@use "buttons";
@use "page-container";
@use "media-queries";
```

<br>

Con este código se consigue *"llamar"* a los demás archivos .scss a utilizar a lo largo del proyecto para estilar la web.


<br><hr><br>


<h2 id="common">_common.scss</h2>

En este archivo se encuentra el código que es común para todos los elementos de la página web. Por ello, este es el código escrito en este documento:

```scss
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Lato', sans-serif;
}
```

El selector `*` indica que esos estilos se aplican a todos los elementos de la web.

Con este código se pretende, por un lado, eliminar los márgenes y el padding que añade la web por defecto.

Por otro lado, se indica que el `box-sizing` es del tipo `border-box`. Con esto se pretende que el borde y el padding se incluyan en el ancho y alto del elemento, y no lo *agranden*.

Finalmente, se indica qué fuente debe ser usada por el texto de la página.

Si se quisiera modificar alguno de estos valores, simplemente se modificaría seleccionando el elemento concreto, tal y como se verá más adelante.


<br><hr><br>


<h2 id="nav">_nav.scss</h2>

Este archivo es el encargado de estilar el menú de navegación situado en la cabecera de la página.

Como ya se ha explicado en el archivo [README-html](../html/README-html.md), el panel de navegación cuenta con un `<header>` que incluye el menú de navegación al completo. Este es el código de dicho bloque completo:

```scss
.navigation-wrapper {
    width: 100%;
    height: 80px;
    background-color: black;
    display: flex;
    align-items: center;
    justify-content: space-between;
```

<br>

Con las primeras dos líneas de código se consigue dar un ancho y un alto al menú, y después, se le aplica un color de fondo negro.

Se utiliza **Flexbox** para alinear verticalmente los elementos, así como espaciar al máximo con `justify-content` el bloque correspondiente al logo y los links de navegación, y por otro lado, los botones de sesión de usuario.

Dentro de este bloque, **.navigation-wrapper**, se encuentran dos bloques principales, los cuales se mostrarán con comentarios a continuación para explicar el funcionamiento de cada línea de código:

* Bloque referido al **logo y a los links de navegación**:

```scss
.logo-links-wrapper {
    // se usa Flexbox para alinear los elementos verticalmente
    display: flex;
    align-items: center;
    gap: 30px; // para dar espacio entre el logo y los links de navegación

    .logo-column img {
        // tamaño de la imagen:
        height: 30px; // alto
        width: auto; // ancho
        // margen a los laterales:
        margin: 0 25px;
    }

    .links-column {
        // para dar un ancho a la sección de links:
        width: 450px;
        // se usa Grid para crear una única columna:
        display: grid;
        grid-template-columns: 1fr;
        // espacio entre los links y el texto 'EXPLORE':
        grid-gap: 5px;

        .explore { // estilado del texto 'EXPLORE' sobre los links
            font-weight: 700; // grosor del texto
            color: #f4e187; // color del texto
        }

        .links-wrapper {
            // se usa Flexbox para:
            display: flex;
            align-items: center; // alinear elementos verticalmente
            justify-content: space-between; // separar al máximo los elementos entre sí
		
            .nav-link a {
	            // estilado de los links de navegación
                font-weight: 900; // grosor del texto
                color: white; // color del texto
                text-decoration: none; // se le quita el subrayado al texto
                font-size: 1.15em; // tamaño del texto
                
                &:hover {
                    // al hacer hover, se le cambia el color a los links
                    color: #acacac;
                }
            }
		
            .spark-chevron {
                a { // estilo relacionado al link completo
                    font-weight: 700; // grosor de texto
                    font-size: 1.1em; // tamaño de texto
                    color: #acacac; // color del texto
                    text-decoration: none; // quitar subrayado al link
		
                    &:hover {
                        // al hacer hover, se le cambia el color al link
                        color: #c6c6c6;
                    }
                }
		
                i { // estilo relacionado con el icono de FontAwesome
                    margin-left: 10px; // para dar espacio entre texto e icono
                    font-size: 0.8em; // tamaño del icono
                }
            }
        }
    }
}
```

<br>

* Bloque referido a la parte de **creación, búsqueda, inicio de sesión y registro de usuario**:

```scss
.create-login-signup {
    width: 500px; // se define un ancho para el contenedor
    // se usa Flexbox para:
    display: flex;
    align-items: center; // alinear elementos verticalmente
    justify-content: flex-end; // alinear elementos a la derecha del todo
    gap: 15px; // separación entre elementos
    margin-right: 5px; // margen para dar espacio por la derecha

    .search-icon a { // estilo para el icono de lupa
        color: #7b7e8b; // color del icono
        font-size: 2em; // tamaño del icono
        margin: 0 10px; // añadir margen a los laterales del icono

        &:hover {
            // cuando se hace hover, se le cambia el color al icono
            color: #acacac;
        }
    }
}
```


<br><hr><br>


<h2 id="buttons">_buttons.scss</h2>

Este archivo contiene 3 bloques de código principales:

* Bloque referido a los botones con clase **.grey-btn**:

```scss
.grey-btn {
    background-color: #36383f; // color de fondo del botón
    border: none; // para quitar el borde
    border-radius: 3px; // radio del borde
    color: #f7f5e6; // color de texto
    font-size: 1.15em; // tamaño del texto
    font-weight: 700; // grosor del texto
    padding: 15px 23px; // padding
    // se usa Flexbox para los botones grises con icono
    display: flex;
    align-items: center; // alinea texto e icono
    gap: 10px; // espacio entre texto e icono

    i {
        color: #4bce79; // color del icono
        font-size: 1.2em; // tamaño del icono
    }

    &:hover {
        // al hacer hover sobre el botón:
        background-color: #5a5f73; // se le cambia el color de fondo
        cursor: pointer; // cambia el tipo de cursor
    }
}
```

<br>

* Bloque referido a los botones con clase **.green-btn**:

```scss
.green-btn {
    background-color: #47cf73; // color de fondo
    border: none; // para quitar el borde
    border-radius: 4px; // radio del borde
    color: black; // color del texto
    font-size: 2em; // tamaño del texto
    font-weight: 700; // grosor del texto
    padding: 18px 25px; // padding

    &:hover {
        // al hacer hover:
        background-color: #248c46; // cambio de color de fondo
        color: white; // cambio del color de texto
        cursor: pointer; // cambio del tipo de cursor
    }
}
```

<br>

* Bloque referido a los botones con clase **.black-btn**:

```scss
.black-btn {
    background-color: #111111; // color de fondo
    border: none; // para quitar el borde
    border-radius: 4px; // radio del borde
    color: white; // color del texto
    font-size: 2em; // tamaño del texto
    font-weight: 700; // grosor del texto
    padding: 18px 25px; // padding

    &:hover {
        // al hacer hover:
        background-color: #36383f; // cambio del color de fondo
        cursor: pointer; // cambio del tipo de cursor
    }
}
```


<br><hr><br>


<h2 id="page-container">_page-container.scss</h2>

Este documento está formado por tres bloques de código principales:

* El bloque que contiene el contenido principal de la página de inicio, es decir, una breve descripción con un par de botones, y una imagen con un texto sobre ella:

```scss
.features-section {
    // se le da un tamaño a la sección
    width: 100%; // todo el ancho del bloque
    height: 530px; // altura
    background-color: #40434d; // color de fondo
    // se aplica una sombra visible "al fondo" de la página:
    box-shadow: inset -650px -200px 500px rgba(0, 0, 0, 0.6);
    // se utiliza Flexbox para:
    display: flex;
    align-items: center; // centrar elementos verticalmente
    justify-content: space-between; // espaciar los dos bloques al máximo posible

    .description-section { // bloque izquierdo
        // se define un tamaño:
        width: 700px; // ancho
        height: 100%; // alto
        // se utiliza Flexbox para:
        display: flex;
        flex-direction: column; // usar una disposición vertical
        align-items: flex-start; // alinear textos y botones a la izquierda
        justify-content: flex-start; // alinear textos y botones arriba
        margin-left: 60px; // margen izquierdo para bloque que contiene textos y botones

        .text-content {
            // se usa Grid para:
            display: grid;
            grid-template-columns: 1fr; // crear una única columna
            grid-gap: 20px; // espacio entre ambos textos
            margin: 50px 0 45px; // márgenes del bloque de textos

            .top-header {
                width: 100%; // el texto superior ocupa todo el espacio
                color: #b8b9bd; // color del texto
                font-weight: 300; // grosor del texto
                font-size: 2.5em; // tamaño del texto

                strong {
                    color: white; // color del texto en negrita
                }

                img {
                    // tamaño del emoji (introducido como imagen):
                    height: 40px; // alto
                    width: auto; // ancho
                }
            }

            .bottom-header {
                width: 650px; // el texto inferior tiene ese ancho
                color: #b8b9bd; // color del texto
                font-size: 2em; // tamaño del texto
                font-weight: 400; // grosor del texto
                line-height: 1.5em; // espaciado entre líneas
            }
        }

        .buttons-wrapper {
            // se usa Flexbox para:
            display: flex;
            align-items: center; // centrar botones verticalmente
            gap: 15px; // espacio entre ambos botones
        }
    }

    .projects-section {
        height: 100%; // altura
        // se usa Flexbox para:
        display: flex;
        flex-direction: column; // disposición en columna (vertical)
        align-items: flex-start; // alinear texto e imagen a la izquierda
        justify-content: flex-end; // alinear bloque en la parte inferior
        gap: 8px; // espacio entre texto e imagen

        .img-header { // estilo del encabezado de la foto
            color: white; // color del texto
            font-size: 1.15em; // tamaño del texto
            font-weight: 700; // grosor del texto
            margin-left: 15px; // efecto de pequeña indentación

            a { // estilo del link del encabezado de la foto
                color: #86dfff; // color del tecto
                text-decoration: none; // para quitar el subrayado

                &:hover {
                // al hacer hover, le cambia el color al texto
                color: #86ffff;
                }
            }
        }

        img { // estilo para la imagen
            // tamaño
            width: 550px; // ancho
            height: auto; // alto
            box-shadow: 0 0 50px rgba(0, 0, 0, 0.7); // sombras
        }
    }
}
```

<br>

* Bloque de código que contiene los enlaces en los que se indica para qué entidad se usa CodePen:

```scss
.codepen-for-wrapper {
    // se usa Grid para:
    display: grid;
    grid-template-columns: repeat(4, 1fr); // crear 4 columnas iguales
    text-align: center; // se centran los textos dentro de las columnas

    .codepen-for-item {
        // se le da un efecto de botón a los enlaces:
        background-color: #36383f; // color de fondo
        border: 1px solid #676767; // borde
        padding: 20px 0; // padding
        color: white; // color del texto
        text-decoration: none; // se quita el subrayado
        font-weight: 700; // grosor del texto
        font-size: 1.2em; // tamaño del texto

        &:hover {
            // al hacer hover, se le cambia el color de fondo
            background-color: #5a5f73;
        }

        span {
            // el span de cada enlace tiene un tipo de fuente distinta a la genérica
            font-family: 'Noto Sans JP', sans-serif;
            font-size: 1.3em; // tamaño del texto
            letter-spacing: -2px; // espaciado entre letras
        }
    }
}
```

<br>

El tipo de fuente `'Noto Sans JP'` no coincide con el del enunciado de la imagen, pero ha sido la fuente más parecida que se ha podido encontrar.

<br>

* Bloque referido al final de la página:

```scss
.page-end {
    width: 100%;
    height: 90px;
    background-color: #191a1d;
}
```

<br>

Con este código se pretendía dejar un pequeño espacio al final de la página con ese color de fondo, que ocupara todo el ancho, y simulara que la página continuaba hacia abajo.


<br><hr><br>


<h2 id="media-queries">_media-queries.scss</h2>

Finalmente, se encuentra el archivo dedicado a hacer que la página web posea un diseño responsive para que pueda visualizarse de forma correcta en los dispositivos de distintos tamaños.

Por ello, se ha decidido crear dos *breakpoints* en base al tamaño de pantalla, de tal forma que cuando el ancho de la pantalla sea mayor a 1280px se vea de una forma, cuando sea mayor de 768px pero de máximo 1280px se vea de otra, y finalmente, la disposición vuelva a variar cuando el ancho de pantalla sea de máximo 768px.

He aquí los dos bloques de código, el primero, para un ancho de pantalla entre 769px y 1280px:

```scss
@media (max-width: 1280px) {
    .navigation-wrapper {
        // tamaño del panel de navegación
        width: 100%; // ancho
        height: 100%; // alto
        flex-direction: column; // cambia la disposición a columna
        padding: 10px 0; // añade un espacio arriba y abajo

        .logo-links-wrapper {
            width: 80%; // para que el logo y los links ocupen un 80% del "navigation-wrapper"
            flex-direction: column; // cambia la disposición a columna

            .links-column {
                width: 100%; // para que ocupe todo el ancho del "logo-links-wrapper"
                text-align: center; // para centrar el bloque de links y el texto "EXPLORE"
                margin-bottom: 40px; // margen debajo de los links hasta los botones

                .links-wrapper {
                    width: 100%; // para que ocupe todo el ancho del "links-column"
                    justify-content: space-around; // para separar los links con espacios iguales
                }
            }
        }

        .create-login-signup {
            width: 100%; // para que ocupe todo el ancho del panel de navegación
            justify-content: center; // para centrar los elementos
        }
    }	

    .features-section {
        height: 100%; // para que ocupe todo el alto de su contenido
        flex-direction: column; // para cambiar la disposición a columna

        .description-section {
            width: 80%; // para que ocupe un 80% del ancho de "features-section"
            margin: 0 0 50px; // margen inferior solo

            .text-content > .bottom-header {
                width: 100%; // para que ocupe el ancho entero posible
            }
        }
    }

    .codepen-for-wrapper {
        width: 100%; // para que ocupe todo el ancho
        grid-template-columns: 1fr 1fr; // crea dos columnas iguales
    }
}
```

<br>

Y finalmente, el código para cuando se dispone de una pantalla inferior a 769px:

```scss
@media (max-width: 768px) {
    .navigation-wrapper > .logo-links-wrapper {
        width: 90%; // se agranda un poco más el ancho
    }

    .features-section {
        .description-section {
            align-items: center; // se alinean los elementos en el centro del eje X

            .text-content {
                font-size: 0.7em; // tamaño del texto

                .top-header, .bottom-header {
                    width: 100%; // ambos textos ocupan el 100% permitido
                    text-align: center; // se alinea el texto

                    img {
                        height: 20px; // cambio del tamaño del emoji
                    }
                }
            }

            .buttons-wrapper {
                font-size: 0.5em; // cambio del tamaño del texto de los botones
            }
        }

        .projects-section img {
            width: 400px; // cambio del ancho de la imagen
        }
    }

    .codepen-for-wrapper {
        grid-template-columns: 1fr; // los links ocupan cada uno el ancho entero, única columna
    }
}
```


<br><hr><br>

[Volver a la página README principal.](../README.md)

# Requests Package to communicate with APIs

Para poder trabajar con APIs desde Python, se puede instalar el parquete `requests` desde la terminal:

```bash
pip install requests
```

<br>

Una vez instalado, utilizando Python, podemos importar el paquete y utilizarlo para hacer peticiones a una API. Además, podemos utilizar el paquete `pprint` para poder visualizar mejor los datos que nos devuelve la API:

```python
import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts') # Hacemos una petición GET a la API de DailySmarty
r.json() # Devuelve los datos de la API en formato JSON

# el formato devuelto es dificil de leer
# podemos utilizar el paquete pprint para visualizarlo mejor
pprint.pprint(r.json())
```

<br>

Como los archivos JSON son muy similares a los diccionarios de Python, podemos utilizar los métodos de los diccionarios para acceder a los datos que nos devuelve la API:

```python
r.json()['posts'][0]
# devolvería el primer post de la API con su información

r.json()['posts'][0]['url_for_post']
# devolvería la url del primer post de la API
```
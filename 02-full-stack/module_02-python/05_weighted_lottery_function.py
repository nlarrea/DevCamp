""" ENUNCIADO
teniendo un diccionario cualquiera, queremos que la probabilidad de que una
función devuelva el nombre de una de las llaves sea el valor de esa llave

si la función recibiera este diccionario:

weights = {
    "winning":1,
    "losing":1000
}

weighted_lottery(weights)

entonces, por cada 1001 veces, 1000 se imprimiría 'losing' y 1 se imprimiría 'winning'

Si se le pasa este diccionario:

other_weights = {
    "winning":1,
    "break_even":2,
    "losing":3
}

la probabilidad de que se devuelva 'losing' será 3 veces mayor que la probabilidad
de 'winning', y la de 'break_even' será el doble de 'winning'
"""

weights = {
    "winning":1,
    "break_even":2,
    "losing":3
}

import numpy as np

def weighted_lottery(weights):
    container_list = []

    # loop para movernos por todos los pares clave-valor del diccionario
    for (name, weight) in weights.items():
        # por cada valor, almacenamos la clave en el container_list
        for _ in range(weight):
            container_list.append(name)
    
    # usamos numpy para que escoja un string aleatorio del container_list
    return np.random.choice(container_list)

print(weighted_lottery(weights))
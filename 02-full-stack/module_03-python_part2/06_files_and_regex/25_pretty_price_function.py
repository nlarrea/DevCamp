""" ENUNCIADO
función recibe 3.21 -> devuelve 3.99 ó 3.95, como queramos

pretty_price(3.20, 99) -> 3.99
pretty_price(3.20, 0.99) -> 3.99
"""


def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension /= 100
    
    return int(gross_price) + extension


print(pretty_price(3.21, 99))           # 3.99
print(pretty_price(3.21, 0.99))         # 3.99

"""
isinstance(value, class) -> comprueba si el valor es una instancia de esa clase

como todo en python son objetos, los elementos de tipo int() son instancias de
esa clase, por lo que si queremos saber si un valor es del tipo integer, podemos
utilizar la función 'isinstance()'
"""
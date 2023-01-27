""" ENUNCIADO
histogram = type of chart used in statistics and machine learning thar allows
us to see patterns and basic types of trends with data

El ejercicio consiste en conseguir imprimir este histograma utilizando lo aprendido
con los diccionarios:

g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales = {
    "google": 20,
    "facebook": 42,
    "twitter": 10,
    "offline": 12
}

for (name, qty) in sales.items():
    print(f"{name[0]} {'$' * qty}")

""" this is what is printed
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""
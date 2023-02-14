""" ENUNCIADO
calcular el valor medio de los elementos de una lista utilizando 'reduce'
"""

from functools import reduce

def get_average(num_list):
    total = reduce((lambda total, element: total + element), num_list)

    return total / len(num_list)


num_list = [1, 2, 3, 4, 5, 6]
print(get_average(num_list))
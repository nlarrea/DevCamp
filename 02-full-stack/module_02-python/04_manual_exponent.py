""" MANUAL EXPONENT
manual_exponent(2, 3)
#> 8

manual_exponent(10, 2)
#> 100

2 opciones -> iterar o usar 'reduce()'
"""

# usando la iteración

def manual_exponent_iterative(num, exp):
    counter = exp - 1
    result = num

    while counter > 0:
        result *= num
        counter -= 1

    return result
    
print(manual_exponent_iterative(2, 3))      # 8
print(manual_exponent_iterative(10, 2))     # 10



# usando la función reduce

from functools import reduce

def manual_exponent(num, exp):
    return reduce(lambda acum, current: acum * current, [num] * exp)

print(manual_exponent(2, 3))    # 8
print(manual_exponent(10, 2))   # 10



"""
si queremos crear una lista y todos los elementos de la lista son números conocidos
o el mismo número, podemos hacer lo siguiente:

my_list = [num] * times

eso crea una lista con el número 'num' repetido 'times' veces

sería lo mismo que hacer esto:

[num for _ in range(times)]
"""
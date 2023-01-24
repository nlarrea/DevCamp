""" ENUNCIADO:
se tiene una función que realiza lo siguiente:
dynamic_reducer([1,2,3], '+')   # 1+2+3     ->      operator.add(a, b)
dynamic_reducer([1,2,3], '-')   # 1-2-3     ->      operator.sub(a, b)
dynamic_reducer([1,2,3], '*')   # 1*2*3     ->      operator.mul(a, b)
dynamic_reducer([1,2,3], '/')   # 1/2/3     ->      operator.truediv(a, b)

va a haber que importar:
- operator
- reduce de la librería functools           ->      reduce(function, iterable)
"""

import operator
from functools import reduce

def dynamic_reducer(list, operation):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    return reduce(lambda total, element: operators[operation](total, element), list)

"""
estamos llamando directamente a la función desde lambda, porque operators[operation] contiene
'operator.add' (por ejemplo), entonces, nosotros al hacer 'operators[operation](total, element)'
es lo mismo que hacer 'operator.add(total, element)'
"""

print(dynamic_reducer([1, 2, 3], "+"))    # 6
print(dynamic_reducer([1, 2, 3], "-"))    # -4
print(dynamic_reducer([1, 2, 3], "*"))    # 6
print(dynamic_reducer([1, 2, 3], "/"))    # 0.16666666666666666
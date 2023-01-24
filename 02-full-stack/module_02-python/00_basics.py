# INDENTATION

def sum(num_one, num_two):
    print(num_one + num_two)

sum(2, 4)

# si no usamos indentación, el programa dará un IndentationError



# MATRIX IN PYTHON -> this should come later
""" ENUNCIADO
Crea una función que sea capaz de crear el siguiente tipo de matriz:
[
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8]
]

Esta matriz debería ser el resultado de la siguiente llamada a la función:
manual_incremetning_matrix(5)
"""

""" MI RESULTADO
def manual_incrementing_matrix(number):
    matrix, vector = [], []
    
    # creación de la matriz
    for i in range(number):
        for j in range(number):
            vector.append(j + i)
        matrix.append(vector)
        vector = []
    
    return matrix

print(manual_incrementing_matrix(5))
"""

# SOLUCIÓN DE DEVCAMP

def manual_incrementing_matrix(n):
    # matrix n x n
    matrix = [ [None for y in range(n)] for x in range(n)] # crea una matriz llena de None de dimensión n x n
    
    counter = 0

    for idx, element in enumerate(matrix):
        for nested_idx, nested_element in enumerate(element):
            matrix[idx][nested_idx] = counter + nested_idx
        counter += 1
        
    return matrix

print(manual_incrementing_matrix(5))



# VARIABLES

# valid type names
name = "Cristina"

# use snake case to type variable's names
post_count = 42
a_long_sentence_with_words = ''

print(name)         # Cristina
print(post_count)   # 42

# avoid using names that are not descriptive:
x = 123
y = 456
# this would be better:
num_one = 123
num_two = 456
""" ENUNCIADO
remove_first_and_last(list_to_clean)                -> tipo de sintaxis para llamar a la función
    return cleaned_list

# ejemplo 1:
html = ['<h1>', 'some content', '</h1>']

remove_first_and_last(html)
=> ['some content']


# ejemplo 2:
html2 = ['<h1>', 'some content', 'more', '</h1>']

remove_first_and_last(html2)
=> ['some content', 'more']
"""

""" MI RESULTADO
def remove_first_and_last(list_to_clean):
    if len(list_to_clean) < 3:
        return list_to_clean

    return list_to_clean[1:-1]
"""

""" RESULTADO DEL PROFESOR
usa la desestructuración para asignar el primer y último valor a una variable
('_' porque no las vamos a usar) y todo lo demás lo guarda en otra ('*content')

El * sirve para indicar que guarde TODOS los elementos que pueda en esa variable,
como el primero y el último los guardamos en '_', coge todo lo demás y luego lo
devuelve usando 'return content'

EJEMPLO:
one, *two, three = [1, 2, 3, 4]
    - one -> 1
    - two -> [2, 3]
    - three -> 4
"""

def remove_first_and_last(list_to_clean):
    if len(list_to_clean) < 3:
        return list_to_clean
    
    _, *content, _ = list_to_clean
    return content

html = ['<h1>', 'some content', '</h1>']
print(remove_first_and_last(html))                  # ['some content']

html2 = ['<h1>', 'some content', 'more', '</h1>']
print(remove_first_and_last(html2))                 # ['some content', 'more']
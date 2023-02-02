# DEFAULT ARGUMENTS
def greeting(name = "Guest"):
    print(f"Hi {name}!")


greeting()             # Hi Guest!
greeting("Cris")       # Hi Crist!

"""
NUNCA utilizar una lista como valor por defecto en una función, porque se guarda
la referencia a esa lista de la memoria y si llamas a la función desde dos sitios
diferentes del programa (incluso desde otro archivo), estarás llamando a la misma
lista que antes, por lo que tú creerás que es una lista vacía, pero ya la habías
usado antes, ya tendrá los datos almacenados de la primera vez que la llamaste
"""



# NAMED FUNCTION ARGUMENTS
def full_name(first, last):
    print(f"{first} {last}")


full_name("Naia", "Larrea")                     # Naia Larrea
full_name(last="Larrea", first="Naia")          # Naia Larrea
full_name(first="Naia", last="Larrea")          # Naia Larrea

"""
siempre que la función tenga más de 2 argumentos, se recomienda utilizar named
arguments, para asegurar que no se mandan a otro argumento sin querer
"""



# FUNCTION ARGUMENT UNPACKING
def greeting2(time_of_day, *args):          # primer argumento = time_of_day, el resto de argumentos = args
    print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting2("Morning", "Tiffany", "Hudgens")
# Hi Tiffany Hudgens, I hope that you're having a good Morning
greeting2("Afternoon", "Kristine", "M", "Hudgens")
# Hi Kristine M Hudgens, I hope that you're having a good Afternoon

"""
no importa cuántos argumentos pasemos a la función, siempre va a cogerlos todos
y juntarlos separándolos por un espacio
"""
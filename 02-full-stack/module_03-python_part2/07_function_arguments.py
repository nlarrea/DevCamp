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

las functiones que tengan * en un argumento, harán que ese argumento se comporte
como una tupla

se le puede llamar de cualquier forma al argumento con *, pero por norma general
en python, se le suele llamar 'args'
"""



# KEYWORD ARGUMENTS IN FUNCTIONS -> combination between arg. unpacking and named arg.
def greeting3(**kwargs):
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
    else:
        print("Hi Guest, have a great day!")


greeting3(first_name = "Kristine", last_name = "Hudgens")
# Hi Kristine Hudgens, have a great day!
greeting3()
# Hi Guest, have a great day!

"""
las funciones que tengan ** en un argumento, harán que ese argumento se
comporte como un diciconario, al llamar a la función se le asignan names a las
variables, y éstas son tratadas como claves del diccionario

ejemplo:

greeting3(first_name = "Kristine", last_name = "Hudgens")

hace que ocurra lo siguiente dentro de la función:

kwargs = {
    'first_name': 'Kristine',
    'last_name': 'Hudgens'
}

el argumento puede tomar el nombre que sea, pero por norma convencional en python,
a este tipo de 'keyword argument' de le seuele llamar 'kwargs'
"""



# COMBINE ALL TYPE OF ARGUMENTS IN FUNCTIONS
def greeting4(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope that you're having a great {time_of_day}")

    if kwargs:
        print("\nYour tasks for the day are:")
        for key, val in kwargs.items():
            print(f"\t- {key} => {val}")


greeting4(
    "Morning",                          # time_of_day -> porque está en primera posición
    "Kristine", "Hudgens",              # *args -> coge todos los demás argumentos
    # estos argumentos tienen nombre, por lo que se recogen en '**kwargs' como diccionario:
    first = "Empty dishwasher",
    second = "Take pupper outside",
    third = "Math homework"
)

""" esta función imprime:
Hi Kristine Hudgens, I hope that you're having a great Morning

Your tasks for the day are:
    - first => Empty dishwasher
    - second => Take pupper outside
    - third => Math homework
"""
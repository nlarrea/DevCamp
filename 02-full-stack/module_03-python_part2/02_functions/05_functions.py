# FUNCIONES

""" PARA QUÉ SIRVEN
- tenemos un input
- la función realiza lo que tenga que hacer
- obtenemos un output

este proceso puede ser llamado después desde cualquier parte del programa, lo
que evita que tengamos código repetido varias veces

SINTAXIS para función que recibe argumentos (inputs) y devuelve datos (outputs):

def function_name(inputs):
    return output

recibir y devolver datos es algo opcional, pero es lo más común
"""

def full_name(first, last):
    print(f"{first} {last}")


full_name("Haizea", "Albarracín")
full_name("Naia", "Larrea")


# otro ejemplo
def auth(email, password):
    if email == "kristine@hudgens.com" and password == "secret":
        print("Authorized")
    else:
        print("Not authorized")


auth("kristine@hudgens.com", "secret")


# otro ejemplo
def hundred():
    for num in range(1, 101):
        print(num)


hundred()


# otro ejemplo:
def counter(max):
    for num in range(1, max):
        print(num)


counter(50)



# DEVOLVER DATOS DE UNA FUNCIÓN -> return
# así sería el flujo de trabajo real:
def return_full_name(first, last):
    return f"{first} {last}"


kristine = return_full_name("Kristine", "Hudgens")

def greeting(name):
    print(f"Hi {name}!")


greeting(kristine)
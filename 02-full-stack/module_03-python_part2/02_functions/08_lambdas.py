# LAMBDAS
full_name = lambda first, last: f"{first} {last}"

print(full_name("Naia", "Larrea"))          # Naia Larrea


def greeting(name):
    print(f"Hi there {name}")


greeting(full_name("Cris", "Albarracín"))   # Hi there Cris Albarracín

"""
lambda = herramienta que permite recoger una función simple en una variable y
pasarla de forma muy sencilla a otras funciones

SINTAXIS:
lambda <arguments>: what_is_returned
"""
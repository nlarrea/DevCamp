# NESTED FUNCTIONS -> una función dentro de otra

def greeting(first, last):
    # la función 'hija' puede acceder a las variables de la función 'padre'
    def full_name():
        return f"{first} {last}"
    
    print(f"Hi {full_name()}!")


greeting("Naia", "Larrea")      # Hi Naia Larrea!

""" CUÁNDO USAR NESTED FUNCTIONS?
si creas un programa con una función que va a tener que ser llamada en algún
otro momento a lo largo del programa, es mejor no usar nested functions

si solo vas a usar esa función para que sea llamada desde una única función,
entonces sí debería ser una nested function (como en el ejemplo)
"""
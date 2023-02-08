# CLASES
""" SINTAXIS
en python es buena práctica usar la primera letra mayúscula para diferenciar
que se trata de una clase

class Name:
    some_code

    def method(self):
        more_code


las clases pueden tener datos y/o funciones en su interior
"""

class Invoice:
    def greeting(salef):    # method of the class -> pasar siempre el 'self' a los métodos
        return "Hi there"


"""
no va a ocurrir nada con la clase a no ser que creemos un objeto con esa clase

crear un objeto = instanciar
"""

inv_one = Invoice()
print(inv_one)
# <__main__.Invoice object at 0x00000167F5F0B460> -> pointer to the object created

inv_two = Invoice()
print(inv_two)
# <__main__.Invoice object at 0x0000023C92A2B430>

print(inv_two.greeting())



# CONSTRUCTOR __init__
class Invoice2:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f"{self.client} owes: ${self.total}"


google = Invoice2("Google", 100)
snapchat = Invoice2("SnapChat", 200)

print(google.formatter())       # Google owes: $100
print(snapchat.formatter())     # SnapChat owes: $200



# GETTER AND SETTER FUNCTIONS
"""
en python estas funciones vienen dadas solas, no tenemos que preocuparnos por
crearlas como en otros lenguajes
"""

class Invoice3:
    def __init__(self, client, total):
        self.client = client
        self.total = total
    
    def formatter(self):
        return f"{self.client} owes: ${self.total}"
    

google = Invoice3("Google", 100)

# get the data -> getter
print(google.client)            # Google
print(google.total)             # 100

# modify the data -> setter
google.client = "Yahoo"
print(google.client)            # Yahoo
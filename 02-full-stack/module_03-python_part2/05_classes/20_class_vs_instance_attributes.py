# CLASS VS INSTANCE ATTRIBUTES
# ATRIBUTOS DE INSTANCIA
"""
son atributos propios de cada instancia

en el ejemplo de abajo, 'title' es un atributo de instandia, para cada una de
las instancias, puede cambiarse
"""
class Website:
    def __init__(self, title):
        self.title = title
    

ws = Website("My website title")

# atributo de instancia -> atributo específico de la propia instancia
print(ws.__dict__)              # {"title": "My website title"}

# otro ejemplo de atributo de instancia
ws_two = Website("Second title")
print(ws_two.__dict__)          # {"title": "Second title"}

"""
__dict__ -> crea un diccionario con los atributos de la instancia, en este caso
el único atributo que tienen es 'title'
"""



# ATRIBUTOS DE CLASE
"""
son atributos de la clase, son 'hard coded', y van a tener el mismo valor para
cada una de las instancias
"""

class DifferentWebsite:
    title = "My class title"


dw = DifferentWebsite()
print(dw.__dict__)              # {}
print(dw.title)                 # My class title

dw_two = DifferentWebsite()
print(dw_two.title)             # My class title
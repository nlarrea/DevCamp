# PROPERTIES AND DECORATORS
"""
para crear atributos PROTEGIDOS -> _
para crear atributos PRIVADOS -> __
"""

class Invoice:
    def __init__(self, client, total):
        self._client = client       # protected attribute
        self._total = total         # protected attribute
    
    def formatter(self):
        return f"{self._client} owes: ${self._total}"

    """
    al ser atributos protegidos, no podemos acceder a ellos desde fuera de la
    clase, pero haciendo así con @property, podemos crear métodos que tengan el
    nombre del atributo y obtener sus valores desde fuera (getters)
    """
    @property                   # GETTER
    def client(self):
        return self._client

    @client.setter              # SETTER
    def client(self, client):
        self._client = client

    @property                   # GETTER
    def total(self):
        return self._total

"""
GETTER SINTAXIS:
@property
def attribute(self):
    return self._attribute

SETTER SINTAXIS:
@attribute.setter
def attribute(self, attribute):
    self._attribute = attribute
"""


google = Invoice("Google", 100)

print(google.formatter())               # Google owes: $100

# obtener los valores de los atributos protegidos gracias al @property
print(google.client)                    # Google
print(google.total)                     # 100

# modificar valores con un setter
google.client = "Yahoo"                 # modificación
print(google.client)                    # Yahoo

# como 'total' no tiene setter, si intentamos modificar, pasa esto:
#google.total = 200                     # AttributeError: can't set attribute 'total'
# DUNDER METHODS
"""
son los métodos que tienen doble _ a cada lado. Ejemplo -> __init__

sirven para diferenciar los métodos dados directamente por python de aquellos
métodos que hayamos definido nosotros
"""

# __str__
"""
normalmente se usa para casos de debbuging, porque nos permite ver las diferencias
entre los valores de los atributos de las diferentes instancias de una misma clase
"""

# __repr__
"""
similar a __str__, se usa para mostrar la salida, pero se suele utilizar más
para mostrar directamente los valores, de una forma más 'objeto'
"""

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f"Infoice from {self.client} for {self.total}"

    def __repr__(self):
        return f"Invoice <value: client: {self.client}, total: {self.total}>"


inv = Invoice("Google", 100)

print(str(inv))     # Infoice from Google for 100
print(repr(inv))    # Invoice <value: client: Google, total: 100>
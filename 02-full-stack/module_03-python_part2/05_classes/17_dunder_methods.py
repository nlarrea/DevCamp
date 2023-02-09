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

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total - total

    def __str__(self):
        return f"Infoice from {self.client} for {self.total}"


inv = Invoice()

print(str(inv))     # This is the invoice class!
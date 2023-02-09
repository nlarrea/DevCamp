# GENERATORS
"""
vamos a repetir el objetivo que en el archivo anterior, pero utilizando otras
opciones que proporciona Python -> los generadores

usando yield 'se mantiene' el valor del bucle para cuando vuelva a llamarse a
la función, al haber escrito 'yield', se le indica a python que puede usarse la
función next para iterar a través de la lista de nombres
"""

class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0                     # index

        while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]
            
            idx += 1
    
    # as good practices: __repr__ and __str__ to check the data
    def __repr__(self):
        return f"<InfiniteLineup({self.players})"
    
    def __str__(self):
        return f"InfiniteLineup with the players: {self.players}"


astros = [
    "Springer",
    "Bregman",
    "Altuve",
    "Correa",
    "Reddick",
    "Gonzalez",
    "McCann",
    "Davis",
    "Tucker"
]

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

# process
print(next(astros_lineup))      # Springer
print(next(astros_lineup))      # Bregman
print(next(astros_lineup))      # Altuve
print(next(astros_lineup))      # Correa
print(next(astros_lineup))      # Reddick
print(next(astros_lineup))      # Gonzalez
print(next(astros_lineup))      # McCann
print(next(astros_lineup))      # Davis
print(next(astros_lineup))      # Tucker
print(next(astros_lineup))      # Springer
print(next(astros_lineup))      # Bregman
print(next(astros_lineup))      # Altuve
print(next(astros_lineup))      # Correa
print(next(astros_lineup))      # Reddick

print(repr(astros_lineup))
print(str(astros_lineup))
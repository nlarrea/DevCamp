# __iter__ and __next__
""" __iter__()
returns an iterator for the given object (array, set, tuple, etc), it creates
an object that can be accessed one element at a time usign __next__()

__iter__() function returns an iterator object that goes through each element of
the given object. The next element can be accessed through __next__() function

In addition, to make the protocol easier to use, every iterator should also be
an iterable, returning itself in the __iter__ method.
"""

""" __next__()
returns the next item for the iteration.
"""

class Lineup:
    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0          # to keep track and know where we are in the list
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player


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

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
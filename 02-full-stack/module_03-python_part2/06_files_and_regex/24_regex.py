# REGULAR EXPRESSIONS

import fnmatch      # librería propia de Python -> no hace falta instalarla
import os

def list_files():
    for file in os.listdir("./02-full-stack/module_03-python_part2/06_files_and_regex/regex_files/"):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files: ", file)

        if fnmatch.fnmatch(file, "*.rb"):
            print("Ruby files: ", file)

        if fnmatch.fnmatch(file, "*.yml"):
            print("Yalm files: ", file)

        if fnmatch.fnmatch(file, "*.py"):
            print("Python files: ", file)


# list_files()      # comentado para que no ejecute la función



# si queremos encontrar solo parte de un string
from fnmatch import fnmatchcase

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]
# busca los jugadores que acaben con ' 2B'

print("Players that play second base: ", second_base_players)
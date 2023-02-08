# BUCLES FOR Y WHILE

# FOR LOOP
# BUCLES EN LISTAS
players = ["Altuve", "Bregman", "Correa", "Gattis"]

for player in players:
    print(player)



# BUCLES EN TUPLAS
players = ("Altuve", "Bregman", "Correa", "Gattis")

for player in players:
    print(player)
# funciona igual que en las listas



# BUCLES EN DICCIONARIOS
players = {
    "2b": "Altuve",
    "3b": "Bregman",
    "ss": "Correa",
    "dh": "Gattis"
}

# recorrer claves y valores
for position, player in players.items():
    print("Position:", position)
    print("Player name:", player)

# recorrer claves
for position in players:
    print("Position:", position)
    print("Player name:", players[position])

# recorrer los valores
print("List of players:")
for player in players.values():
    print(f"\t- {player}")



# BUCLES EN STRINGS
alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    print(letter)



# BUCLES CON RANGOS
for num in range(1, 10):
    print(num)

for num in range(1, 11, 2):
    print(num)



# CONTINUE Y BREAK
usernames = [
    "jon",
    "tyrion",
    "theon",
    "cersei",
    "sansa"
]

# continue
for username in usernames:
    if username == "cersei":
        print(f"Sorry, {username}, you are not allowed")
        continue
    print(f"{username} is allowed")

# break
for username in usernames:
    if username == "cersei":
        print(f"{username} was found at index {usernames.index(username)}")
        break
    print(f"{username}")



# WHILE LOOP
nums = [*range(1, 100)]     # es lo mismo que: list(range(1, 100))

while len(nums) > 0:
    print(nums.pop())       # se imprimirán todos los números del 99 al 1



# GUESSING GAME
def guessing_game():
    while True:
        print("What is yout guess?")
        guess = input()

        if guess == "42":
            print("You correctly guessed it!")
            return False    # this is telling to the 'True' of the loop to stop (become a False)
        else:
            print(f"No, {guess} is not the answer, please try again!\n")

#guessing_game()    # remove the '#' to play



# MERGE LISTS
legacy_customers = ["Alice", "Bob"]
new_customers = ["Tiffany", "Kristine"]

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)



# LIST COMPREHENSION
num_list = range(1, 11)

# traditional way
cubed_nums = []
for num in num_list:
    cubed_nums.append(num ** 3)
print(cubed_nums)       # it works!

# using list comprehension
cubed_nums = [num ** 3 for num in num_list]
print(cubed_nums)       # it also works!


# ANOTHER EXAMPLE
num_list = range(1, 11)

# traditional way
even_numbers = []
for num in even_numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# list comprehension
even_numbers = [num for num in even_numbers if num % 2 == 0]
print(even_numbers)
from decimal import Decimal
import math


# EXERCISE 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list = ["Woodman", "Scarratt", "Alphonsi", "Fisher"]

my_tuple = ("Kolbe", "McCaw", "Dupont")

my_float = 17.99

my_int = 23

# from decimal import Decimal
my_decimal = Decimal(20.88)

my_dict = {
    "key1": "value1",
    "key2": "value2"
}



# EXERCISE 2: Round your float up.

""" my float:
my_float = 17.99
"""

# import math
print(math.ceil(my_float))          # 18



# EXERCISE 3: Get the square root of your float.

# import math
print(math.sqrt(my_float))          # 4.241462012089699



# EXERCISE 4: Select the first element from your dictionary.

""" my dictionary:
my_dict = {
    "key1": "value1",
    "key2": "value2"
}
"""

# primer par clave-valor
dict_elements = my_dict.items()
print(list(dict_elements)[0])       # ('key1', 'value1')

# primer valor
print(my_dict["key1"])              # value1

# primera clave
dict_keys = my_dict.keys()
print(list(dict_keys)[0])           # key1



# EXERCISE 5: Select the second element from your tuple.

""" my tuple:
my_tuple = ("Kolbe", "McCaw", "Dupont")
"""

print(my_tuple[1])                  # McCaw



# EXERCISE 6: Add an element to the end of your list.

""" my list:
my_list = ["Woodman", "Scarratt", "Alphonsi", "Fisher"]
"""

my_list.append("Nievas")
print(my_list)              # ['Woodman', 'Scarratt', 'Alphonsi', 'Fisher', 'Nievas']



# EXERCISE 7: Replace the first element in your list.

my_list[0] = "Larrea"
print(my_list)              # ['Larrea', 'Scarratt', 'Alphonsi', 'Fisher', 'Nievas']



# EXERCISE 8: Sort your list alphabetically.

my_list.sort()
print(my_list)              # ['Alphonsi', 'Fisher', 'Larrea', 'Nievas', 'Scarratt']



# EXERCISE 9: Use reassignment to add an element to your tuple.

""" my tuple:
my_tuple = ("Kolbe", "McCaw", "Dupont")
"""

my_tuple += ("Carter",)
print(my_tuple)             # ('Kolbe', 'McCaw', 'Dupont', 'Carter')
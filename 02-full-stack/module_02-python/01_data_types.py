# BOOLEANS

# True or False

meal_completed = True
is_prime = False



# NUMBERS

# integers, floats or complex numbers

sub_total = 100
tip = sub_total * 0.2       # same as: tip = sub_total * 1/5
total = sub_total + tip
print(total)

product_id = 123
sale_price = 14.99
tip_percentage = 1/5
print(tip_percentage)               # 0.2
new_product = 150
# integers and floats can work together
print(sale_price + new_product)     # 164.99

# OPERATORS
# addition -> +
addition_value = 100 + 42
print(addition_value)               # 142
# subtraction -> -
subtraction_value = 100 - 42.3
print(subtraction_value)            # 57.7
# division -> /
print(100 / 42.3)                   # 2.364066193853428
# floor division -> //
print(100 // 42)                    # 2 -> rounds the value to smallest
# multiplication -> *
print(100 * 38)                     # 3800
# modulus -> %
print(10 % 2)                       # 0 -> even numbers always return a 0 when calculating %2
print(11 % 2)                       # 1 -> odd numbers always return a 1 when calculating %2
print(10 % 3)                       # 1
# exponents -> **
print(11 ** 2)                      # 121

# ORDER OF OPERATIONS
calculation = 8 + 2 * 5 - (9  + 2) ** 2
print(calculation)                  # -103
""" this is the order:
P = ()
E = **
M = * and D = / -> the one on the left is the first being executed
A = +
S = -
"""

# ASSIGNMENT OPERATOR
total = 100
total = total + 10
print(total)                # 110
# now using the operator:
total = 100
total += 10
print(total)                # 110
total -= 20
print(total)                # 90
total *= 2
print(total)                # 180
total /= 10
print(total)                # 18.0
total //= 5
print(total)                # 3
total **= 2
print(total)                # 9
total %= 2
print(total)                # 1

# DECIMALS VS FLOATS
product_cost = 88.40
commission_rate = 0.08
qty = 450
product_cost += (commission_rate * product_cost)
print(product_cost * qty)           # 42962.4
# let's repeat it but with decimals
from decimal import Decimal         # to use decimals in python
product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450
product_cost += (commission_rate * product_cost)
print(product_cost * qty)           # 42962.40000000000282883716451
# decimals give much more precision -> a MUST TO when it comes to anything that is finance related

# CONVERTION BETWEEN NUMERIC DATA TYPES
product_cost = 88.80
commission_rate = 0.08
qty = 450
print(int(product_cost))            # 88 -> ignores whatever is not the integer number part
print(float(qty))                   # 450.0
from decimal import Decimal
print(Decimal(product_cost))        # 88.7999999999971578...
print(complex(commission_rate))     # (0.08 + 0j)

# FUNCTIONS FOR NUMBER DATA TYPES
import math
loss = -20.25
product_cost = 89.99
print(abs(loss))                    # 20.25 -> doesn't need to import math
print(math.floor(product_cost))     # 89 -> rounds down
print(math.ceil(product_cost))      # 90 -> rounds up
print(abs(math.floor(loss)))        # 21 -> math.floor is called before abs -> math.floor(-20.25) = -21 -> abs(-21) = 21
print(math.floor(abs(loss)))        # 20
print(round(product_cost))          # 90 -> rounds up or down, to the nearest
print(math.sqrt(product_cost))      # 9.486305919587455
print(math.pow(5, 2))               # 25.0
print(5 ** 2)                       # 25
print()



# STRINGS

# can be created using '' or ""

receipt = f"Your total is " + str(total)
print(receipt)
receipt = f"Your total is {total}"
print(receipt)

# both give us the same response

# CASE-FUNCTIONS
sentence = "the quick brown fox jumped over the lazy dog"
print(sentence)
print(sentence.capitalize())    # first letter of the string in uppercase
print(sentence.title())         # first letter of every word from the string in uppercase
print(sentence.upper())
print(sentence.lower())
print(sentence)                 # original string doesn't get modified

# ACCESS TO PART OF THE STRING
sentence = "The quick brown fox jumped"
print(sentence[0])              # T
print(sentence[12])             # o
print(sentence[-1])             # d -> the last char
print(sentence[-3])             # p -> the third starting from the back
# we can't do this:
# sentence[1] = 'r' -> Python doesn't let change the value of a char from a string
print(sentence[0:5])            # The q -> the range doesn't take the last char, it only takes the first 4 instead of 5
first_word = sentence[0:3]
print(first_word)               # The
new_sentence = "Thy" + sentence[3:] # all the sentence from the 4th char untill the end (start counting from 0 -> 4th char = index 3)
print(new_sentence)             # thy quick brown fox jumped

# HEREDOC = multiline string
content = """
Nullam id dolor id nibh ultricies vehivula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis partutient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip() # .strip() deletes the whitespaces at the end and beginning of the string
print(content)

content = """
Nullam id dolor id nibh ultricies vehivula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis partutient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
"""         # the same as before, but not using .strip(), so it adds \n at the beginning and at the end
print(repr(content))    # shows the string as the computer is reading it. Great to see the new line characters, etc.

# how to write the same in a single line:
content = "\nNullam id dolor id nibh ultricies vehivula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis partutient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n"

# STRING INTERPOLATION -> strings that can change during the program using code like variables
name = "Cristina"
greeting = f"Hi {name}!"
print(greeting)     # Hi Cristina!

# this kind of strings can't scape special chars with "\", this is the way it should be done:
sentence = f"this is my {{bracket}} blog post"
# it prints: this is my {bracket} blog post
#
# this would return an error: f"this is my \{bracket\} blog post"

# it is a great way to create a dynami email!
name = "Naia"
product = "Python learning course"
email_content = f"""
Hi {name},

Thank you for purchasing {product}!

Regards,
Sales Team
"""

# FIND A SUBSTRING IN ANOTHER STRING -> 3 options
sentence = "The quick brown fox jumped over the lazy dog"
# 1st option -> .find()
print(sentence.find("quick"))           # 4 -> index of where 'quick' starts
print(sentence.find("oops"))            # -1 -> it doesn't exist in the sentence
# 2nd option -> .index()
print(sentence.index("quick"))          # 4 -> index of where 'quick' starts
#print(sentence.index("oops"))          # error -> throws an error whenever the substring doesn't exist
# 3rd option -> 'in' operator
print("quick" in sentence)              # True
print("oops" in sentence)               # False

# REPLACE PART OF THE STRING
sentence = "The quick brown fox jumped over the lazy dog"
sentence = sentence.replace("quick", "slow")
print(sentence)     # The slow brown fox jumped over the lazy dog

# STRIP STRINGS
url = "   https://google.com      "
url = url.strip()               # remove whitespaces from both sides
url = url.lstrip("https://")    # remove 'https://' from the left
url = url.rstrip(".com")        # remove '.com' from the right
url = url.capitalize()
print(url)                      # Google

# PARTITION -> returns a tuple with 3 elements
heading = "Python: An Introduction"
header, _, subheader = heading.partition(": ")
# it's gonna give us the header, the partition element and the subheader
print(header)                   # Python
print(_)                        # ': ' -> data we don't want (we save it into variable called "_")
print(subheader)                # An Introduction
# -> even if it finds another match, the second value will only be the first partition match
heading = "Python: An Introduction, and Python: Advanced"
header, _, subheader = heading.partition(": ")
print(header)                   # Python
print(_)                        # ': '
print(subheader)                # An Introduction, and Python: advanced

# SPLIT
# this let us separate strings using a partition, but creates a list with every parts
tags = "python, coding, programming, development"
list_of_tags = tags.split(",")
print(list_of_tags)             # ["python", "coding", "programming", "development"]
# if no arguments are given to .split(), it tryes to split from whitespaces

# CHECK IF THERE ARE NUMBERS IN A STRING
api_data = "5"
greeting = "Hi"
# check if is alphanumeric -> careful! whitespaces are no alphanumeric
print(api_data.isalpha())       # False
print(greeting.isalpha())       # True
print("Hi there". isalpha())    # False
# check if is numeric -> this one is a better option to make sure it is a number
print(api_data.isnumeric())     # True
print(greeting.isnumeric())     # False



# Bytes and byte arrays

# not gonna get into it in this course, is way more advanced



# None

# good to create a variable but not giving a value to it yet
#
# great option to create an "empty" list with a specific dimmension



# COLLECTIONS

# Lists -> []

# great to store multiple data types with an order

users = ["Cristina", "June", "Naia"]
print(users)                    # [ 'Cristina', 'June', 'Naia' ]

# INSERT NEW ELEMENTS
users.insert(2, "Raquel")       # [ 'Cristina', 'June', 'Raquel', 'Naia' ] -> insert in index = 2
users.append("Thom")            # [ 'Cristina', 'June', 'Raquel', 'Naia', 'Thom' ] -> insert at the end

# ACCESS ELEMENTS
print(users[3])                 # Naia
print([users[3]])               # ['Naia']

# EDIT VALUES
users[4] = "Irene"
print(users)                    # [ 'Cristina', 'June', 'Raquel', 'Naia', 'Irene' ]

# REMOVE ELEMENTS FROM THE LIST
# .remove() -> when you know the value to remove
users.remove("Raquel")
print(users)                    # ['Cristina', 'June', 'Naia', 'Irene']
# .pop() -> when you want the last element and you wanna use it
popped_user = users.pop()       # pop -> removes the last element and returnes its value
print(popped_user)              # Irene
print(users)                    # ['Cristina', 'June', 'Naia']
# del -> when you only know the index of the element
del users[1]
print(users)                    # ['Cristina', 'Naia']

# MIXED LISTS
users = ["Kristine", "Tiffany", "Jordan", "Leann"]
ids = [1, 2, 3, 4]
mixed_list = [42, 10.3, "Altuve", users]        # nested list -> list inside list
print(mixed_list)                               # [42, 10.3, 'Altuve', ['Kristine', 'Tiffany', 'Jordan', 'Leann']]
user_list = mixed_list.pop()
print(user_list)                                # ['Kristine', 'Tiffany', 'Jordan', 'Leann']
print(mixed_list)                               # [42, 10.3, 'Altuve']

# NESTED LISTS
nested_lits = [[123], [234], [345]]

# LENGTH OF A LIST
tags = ["python", "development", "tutorials", "code"]
print(len(tags))                            # 4

# INDEX OF AN ELEMENT
last_item = tags[-1]
index_of_last_item = tags.index(last_item)
print(index_of_last_item)                   # 3

# SORT LISTS
print(tags)                                 # ['python', 'development', 'tutorials', 'code']
tags.sort()
print(tags)                                 # ['code', 'development', 'python', 'tutorials']
# backwards
tags.sort(reverse=True)
print(tags)                                 # ['tutorials', 'python', 'development', 'code']
# same with numbers
totals = [234, 1, 543, 2345]
totals.sort()
print(totals)                               # 1, 234, 543, 2345
totals.sort(reverse=True)
print(totals)                               # 2345, 543, 234, 1

# SORT WITHOUT CHANGING ORIGINAL LIST -> sorted()
sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]
"""
sort() doesn't return anything and modifies the original list, but sometimes
we don't want that
"""
sorted_list = sorted(sale_prices)
print(sorted_list)                      # [1, 3, 10, 40, 83, 100, 100, 220, 400]
sorted_list = sorted(sale_prices, reverse=True)
print(sorted_list)                      # [400, 220, 100, 100, 83, 40, 10, 3, 1]
print(sale_prices)                      # [100, 83, 220, 40, 100, 400, 10, 1, 3] -> not modified

# JOIN
uri = "https://www.google.com/search?q="
tags = ["python", "development", "tutorial"]
formatted_tags = "+".join(tags)             # join all of the tags using the string as separator
print(formatted_tags)                       # python+development+tutorial
query_uri = f"{uri}{formatted_tags}"
print(query_uri)                            # https://www.google.com/search?q=python+development+tutorial
# we can use whatever string we want to join the list elements

# RANGES
tags = ["python", "development", "tutorials", "code"]
tag_range = tags[1:2]
print(tag_range)                        # development -> the second argument of the range is not included
# from index to the end
tag_range = tags[1:]
print(tag_range)                        # ['development', 'tutorials', 'code']
# from beginning to index
tag_range = tags[:2]
print(tag_range)                        # ['python', 'development']
# all the values except the last one
tag_range = tags[:-1]
print(tag_range)                        # ['python', 'development', 'tutorials']
# copy the list
tag_range = tags[:]
print(tag_range)                        # ['python', 'development', 'tutorials', 'code']

# RANGES AND SLICES
tags = [
    "python",
    "development",
    "tutorials",
    "code",
    "programming",
    "computer science"
]
tag_range = tags[1:-1]                  # start with the second element to the very last element (not included)
print(tag_range)                        # ['development', 'tutorials', 'code', 'programming']
# three arguments
tag_range = tags[:-1:2]                 # the third argument is the interval
print(tag_range)                        # ['python', 'tutorials', 'programming']
# reverse the list
tag_range = tags[::-1]
print(tag_range)                        # ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

# FIND THE STATISTICAL MEDIAN
"""
tools:
- math library
- sorted function
- list slicing
- computations
"""
sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]
import math
sorted_list = sorted(sale_prices)
num_of_sales = len(sale_prices)
median = sorted_list[math.floor(num_of_sales/2)]
print(median)                                       # 83
half_slices = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slices]       # get the first slice of the list
print(first_sales_items)                            # [1, 3, 10, 40]
last_sales_items = sorted_list[-(half_slices):]     # negative index -> last slice of the list
print(last_sales_items)                             # [100, 100, 220, 400]
median = sorted_list[half_slices:(half_slices + 1)]
print(median)                                       # [83]

# SLICE CLASS
tags = [
    "python",
    "development",
    "tutorials",
    "code",
    "programming"
]
print(tags[:2])             # ['python', 'development']
# this is fine, but sometimes we don't know the slice range
slice_obj = slice(2)        # this allows us to store our slice in a variable
print(slice_obj)            # slice(None, 2, None) -> start point (None), end point (2) and the interval (None)
print(tags[slice_obj])      # ['python', 'development']
# another example
slice_obj = slice(1, 4, 2)
print(tags[1:4:2])          # ['development', 'code']
print(tags[slice_obj])      # ['development', 'code']
# we can know where the slice object starts, stops or its step
print(slice_obj.start)      # 1
print(slice_obj.stop)       # 4
print(slice_obj.step)       # 2
# this is great to don't repeat code when slicing in different lists using the same pattern

# ADD TO A LIST WITH PLACE AND COPY PROCESSES
tags = ["python", "development", "tutorials", "code"]
# wrong way to add an element
tags[-1] = "programming"        # replaces code, not adding elements
tags.extend("programming")
print(tags)                     # ['python', 'development', 'tutorials', 'programming', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
# correct way
tags = ["python", "development", "tutorials", "code"]
tags.extend(["programming"])
print(tags)                     # ['python', 'development', 'tutorials', 'code', 'programming']
# without modifying the original list
tags = ["python", "development", "tutorials", "code"]
new_tags = tags + ["programming"]
print(new_tags)                 # ['python', 'development', 'tutorials', 'code', 'programming']



# Tuples -> ()

# similar to lists, but they can not change its value

# tuples are often used to unpacking
post = ("Python Basics", "Intro guide to python", "Some cool python content")
title, sub_heading, content = post      # this is unpacking
print(title)                            # Python Basics
print(sub_heading)                      # Intro guide to python
print(content)                          # Some cool python content
""" this does the same thing that this
title = post[0]
sub_heading = post[1]
content = post[2]
"""
# when should we use use tuples and when should we use lists?
# tuples = immutable -> much more control
# lists = mutable
#
# if we use a list and there is a .sort(), the values are not gonna store in the order we want:
post = ["Python Basics", "Intro guide to python", "Some cool python content"]
post.sort()
title, sub_heading, content = post
print(title)                            # Intro guide to python
print(sub_heading)                      # Python Basics
print(content)                          # Some cool python content
# now the data is not correct
#
# but if we .sort() a tuple, that would be an error, because tuples are immutable

# ADD ELEMENTS TO TUPLES
post = ("Python Basics", "Intro guide to python", "Some cool python content")
# post = post + ("published")           # this is gonna be treated as a mathematical operation
# to solve this, we have to add a comma at the end
post += ("published",)
print(post)                             # ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')
title, sub_heading, content, status = post
print(title)                            # Python Basics
print(sub_heading)                      # Intro guide to python
print(content)                          # Some cool python content
print(status)                           # published

# ID FUNCTION
post = ("Python Basics", "Intro guide to python", "Some cool python content")
print(id(post))             # 2037450353792 -> give us the id of the object
post += ("published",)
print(id(post))             # 2037450600144 -> we can see that now, post object has changed, it's not the same as before

# LISTS NESTED IN TUPLES
post = ("Python Basics", "Intro guide to python", "Some cool python content")
tags = ["python", "coding", "tutorial"]
post += (tags,)
print(post)                 # ('Python Basics', 'Intro guide to python', 'Some cool python content', ['python', 'coding', 'tutorial'])
print(post[-1])             # ['python', 'coding', 'tutorial']
print(post[-1][1])          # coding

# SLICES
post = ("Python Basics", "Intro guide to python", "Some cool python content", "published")
print(post[:2])             # ('Python Basics', 'Intro guide to python')
print(post[1:])             # ('Intro guide to python', 'Some cool python content', 'published')
print(post[1::2])           # ('Intro guide to python', 'published')

# REMOVE ELEMENTS FROM TUPLES -> tuples are immutable -> need to slice
# remove from end
post = ("Python Basics", "Intro guide to python", "Some cool python content", "published")
post = post[:-1]
print(post)                 # ('Python Basics', 'Intro guide to python', 'Some cool python content')
# remove from beginning
post = post[1:]
print(post)                 # ('Intro guide to python', 'Some cool python content')
# remove specific element (not recommended)
post = ("Python Basics", "Intro guide to python", "Some cool python content", "published")
post = list(post)
post.remove("published")
post = tuple(post)
print(post)                 # ('Python Basics', 'Intro guide to python', 'Some cool python content')



# Sets

# similar to lists, but their elements don't follow any order, and values can't be repeated



# Disctionaries -> {}

# key-value data is stored here

# creating a dictionary
players = {
    "ss": "Correa"
}
print(players)                          # {'ss': 'Correa'}
# create disctionary with more items
players = {
    "ss": "Correa",
    "2b": "Altuve",
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer"
}
# now, instead of working with indexes, we'll work with key-value structures

# QUERY THE VALUES
second_base = players["2b"]
print(second_base)                      # Altuve
# print(players["abc"])                 # KeyError: 'abc' -> because that key doesn't exist
designated_hitter = players["DH"]
print(designated_hitter)                # Gattis

# NESTED COLLECTIONS
# lists as dictionary values
teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"]
}
print(teams["astros"])                  # ['Altuve', 'Correa', 'Bregman']
print(teams["astros"][1])               # Correa
print(teams["astros"][:2])              # ['Altuve', 'Correa']
# we can save the values (lists) in different variables
angels = teams["angels"]
print(angels)                           # ['Trout', 'Pujols']

# ADD NEW KEY-VALUE PAIRS
teams["red sox"] = ["Price", "Betts"]   # keys are strings, can have whitespaces, but not recommended
print(teams)
""" this is what is printed -> the new pair has been added
{
    'astros': ['Altuve', 'Correa', 'Bregman'],
    'angels': ['Trout', 'Pujols'],
    'yankees': ['Judge', 'Stanton'],
    'red sox': ['Price', 'Betts']
}
"""

# GET
featured_team = teams["astros"]         # this works, but if the key didn't exist, it would raise an error
# sometimes you just want to have a fallback -> .get()
featured_team = teams.get("mets", "No featured team")
print(featured_team)                    # No featured team
# if the key ('mets') doesn't exist, the featured_team will take the second argument as value
featured_team = teams.get("yankees", "No featured team")
print(featured_team)                    # ['Judge', 'Stanton']

# DICTIONARY VIEW OBJECT
players = {
    "ss": "Correa",
    "2b": "Altuve",
    "3b": "Bregman",
    "DH": "Gattis",
    "OF": "Springer"
}
teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"]
}
# GRAB ONLY THE KEYS, VALUES OR BOTH
print(players.keys())                   # dict_keys(['ss', '2b', '3b', 'DH', 'OF']) -> it is an object, not a list
print(players.values())                 # dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])
print(players.items())                  # dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])
# view objects are not lists, we can not use them as lists, but we can convert the view objects into lists
print(list(players.values()))           # ['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer']

# THREAT SAVE -> COPY THE LIST
player_names = list(players.copy().values())

# NESTED ITEMS
team_groupings = teams.items()
print(team_groupings)                   # prints all the teams and players together
print(len(team_groupings))              # 4
print(list(team_groupings))
""" this is what is printed
[
    ('astros', ['Altuve', 'Correa', 'Bregman']),
    ('angels', ['Trout', 'Pujols']),
    ('yankees', ['Judge', 'Stanton']),
    ('red sox', ['Price', 'Betts'])
]
"""
# they are tupples -> can use them almost like lists
print(list(team_groupings)[1])          # ('angels', ['Trout', 'Pujols'])
print(list(team_groupings)[1][0])       # angels
print(list(team_groupings)[1][1])       # ['Trout', 'Pujols']
print(list(team_groupings)[1][1][0])    # Trout

# REMOVE ELEMENTS FROM DICTIONARIES
teams = {
    "astros": ["Altuve", "Correa", "Bregman"],
    "angels": ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"]
}
# 'del' keyword -> useful when we know that the key exists
del teams["astros"]
print(teams)
""" this is what is printed
{
    'angels': ['Trout', 'Pujols'],
    'yankees': ['Judge', 'Stanton'],
    'red sox': ['Price', 'Betts']
}
"""
# if the key doesn't exist, it raises an error
# del teams["mets"]             # KeyError
# .pop() -> like .get(), we give to it a second argument, if the first doesn't exist, returns the message
removed_team = teams.pop("astros", "No team found by that name")
print(removed_team)             # No team found by that name
removed_team = teams.pop("yankees", "No team found by that name")
print(removed_team)             # ['Judge', 'Stanton'] -> the value of the removed item

# LISTS OF NESTED DICTIONARIES
teams = [
    {
        "astros": {
            "2B": "Altuve",
            "SS": "Correa",
            "3B": "Bregman"
        }
    },
    {
        "angels": {
            "OF": "Trout",
            "DH": "Pujols"
        }
    }
]
print(teams)
""" this is what is printed
[{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}, {'angels': {'OF': 'Trout', 'DH': 'Pujols'}}]
"""
# it is a list, so we can use it as it is
print(teams[0])                     # {'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}
angels = teams[1].get("angels", "Team not found")
print(angels)                       # {'OF': 'Trout', 'DH': 'Pujols'}
print(list(angels.values()))        # ['Trout', 'Pujols']
print(list(angels.values())[1])     # Pujols
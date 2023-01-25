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



# Bytes and byte arrays

# not gonna get into it in this course, is way more advanced



# None

# good to create a variable but not giving a value to it yet
#
# great option to create an "empty" list with a specific dimmension



# COLLECTIONS

# Lists

# great to store multiple data types with an order



# Tuples

# similar to lists, but they can not change its value



# Sets

# similar to lists, but their elements don't follow any order, and values can't be repeated



# Disctionaries

# key-value data is stored here
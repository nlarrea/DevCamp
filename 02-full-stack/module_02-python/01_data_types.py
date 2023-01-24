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
# we can't do this:
# sentence[1] = 'r' -> Python doesn't let change the value of a char from a string
print(sentence[0:5])            # The q -> the range doesn't take the last char, it only takes the first 4 instead of 5
first_word = sentence[0:3]
print(first_word)               # The
new_sentence = "thy" + sentence[3:]     # takes all the sentence from the 4th char untill the end (start counting from 0 -> 4th char = index 3)
print(new_sentence)             # thy quick brown fox jumped



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
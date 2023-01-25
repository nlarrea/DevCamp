# EXERCISE 1: Create a string, number, list, and boolean, each stored in their own variable.

my_str = "Hello world!"
my_number = 5
my_list = [True, 11, "hola", 1.62]
my_boolean = False



# EXERCISE 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

first_three = my_str[:3]
print(first_three)



# EXERCISE 3: Use an index to grab the first element from your list.

print(my_list[0])



# EXERCISE 4: Create a new number variable that adds 10 to your original number

add_ten = my_number + 10
print(add_ten)



# EXERCISE 5: Use an index to get the last element in your list

print(my_list[-1])



# EXERCISE 6: Use split to transform the following string into a list

names = "harry,alex,susie,jared,gail,conner"
list_of_names = names.split(",")
print(list_of_names)



"""
EXERCISE 7: Get the first word from your string using indexes. Use the upper
function to transform the letters into uppercase. Create a new string that
takes the uppercase word and the rest of the original string.
"""

first_word = my_str[:5]
my_new_str = first_word.upper() + my_str[5:]
print(my_new_str)



# EXERCISE 8: Use string interpolation to print out a sentence that contains your number variable.

sentence = f"Mi variable contiene el número {my_number}"
print(sentence)



# EXERCISE 9: Print "hello world"

print("hello world")
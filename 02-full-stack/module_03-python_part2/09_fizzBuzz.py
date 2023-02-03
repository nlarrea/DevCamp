"""
Write a program thar prints the numbers from 1 to 100. But for multiples of
three print 'Fizz' instead of the number, and for the multiples of five print
'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'

- function
- looping
- conditionals
- math operators
"""

def fizz_buzz(max):
    for num in range(1, max + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


fizz_buzz(100)
""" EXERCISE 1
Create a dictionary called student with the keys: name, age, major, year, and
classes.
"""

student = {
    "name": "Naia",
    "age": 24,
    "major": "electronics",
    "year": 4,
    "classes": [
        "digital control systems",
        "virtual instrumentation",
        "electronics"
    ]
}



""" EXERCISE 2
Use the get method to print the value of the key “name”.
"""

print(student.get("name", "Key not found"))



""" EXERCISE 3
Use the pop method to remove “year” from the dictionary.
"""

print(student)

student.pop("year")
print(student)



""" EXERCISE 4
Add the key/value pair of “gpa” : 3.9 to the dictionary.
"""

student["gpa"] = 3.9
print(student)



""" EXERCISE 5
Change the “gpa” value from 3.9 to 4.0
"""

student["gpa"] = 4.0
print(student)



""" EXERCISE 6
Create a new dictionary with the name collegeStudents and make it so the keys
are name, age, major, year, and gpa. The values are in a list, where each index
in the list is a student. Next, add a few students.
"""

collegeStudents = {
    "name": ["Cris", "June", "Sheila"],
    "age": [28, 24, 20],
    "major": ["physiology", "economics", "electronics"],
    "year": [4, 4, 3],
    "gpa": [4.0, 3.7, 3.3]
}

collegeStudents["name"].append("Asier")
collegeStudents["age"].append(19)
collegeStudents["major"].append("mathematics")
collegeStudents["year"].append(2)
collegeStudents["gpa"].append(4.0)

print(collegeStudents)



""" EXERCISE 7
Sort the dictionary
"""

print(sorted(collegeStudents))
# DICTIONARY

• A Dictionary is a collection of data stored as key-value pairs.
• It is enclosed within curly braces {}.
• Keys must be unique.
• Values can be of any data type.
• It is mutable (can be modified after creation).

# Example :

student = {
    "name": "Arun",
    "age": 20,
    "grade": "A"
}

print(student)

# Accessing Values

• Values are accessed using their keys.

# Example :

student = {
    "name": "Arun",
    "age": 20,
    "grade": "A"
}

print(student["name"])
print(student["age"])

# Output

Arun
20

# Modifying Values

• Existing values can be updated using their keys.

# Example :

student = {
    "name": "Arun",
    "age": 20
}

student["age"] = 21

print(student)

# Output

{'name': 'Arun', 'age': 21}

# Adding New Elements

• New key-value pairs can be added to a dictionary.

# Example :

student = {
    "name": "Arun",
    "age": 20
}

student["city"] = "Chennai"

print(student)

# Output

{'name': 'Arun', 'age': 20, 'city': 'Chennai'}

# Dictionary Methods

• keys()
  Returns all keys.

• values()
  Returns all values.

• items()
  Returns key-value pairs.

• pop()
  Removes a specified key.

• clear()
  Removes all elements.

• len()
  Returns the number of key-value pairs.

# Example :

student = {
    "name": "Arun",
    "age": 20,
    "city": "Chennai"
}

print("Keys :", student.keys())
print("Values :", student.values())
print("Items :", student.items())

student.pop("city")
print("After pop() :", student)

print("Length :", len(student))

student.clear()
print("After clear() :", student)

# Output

Keys : dict_keys(['name', 'age', 'city'])
Values : dict_values(['Arun', 20, 'Chennai'])
Items : dict_items([('name', 'Arun'), ('age', 20), ('city', 'Chennai')])
After pop() : {'name': 'Arun', 'age': 20}
Length : 2
After clear() : {}

# Traversing a Dictionary

# Example :

student = {
    "name": "Arun",
    "age": 20,
    "city": "Chennai"
}

for key, value in student.items():
    print(key, ":", value)

# Output

name : Arun
age : 20
city : Chennai

# Passing Dictionary to a Function

def display_student(data):
    for key, value in data.items():
        print(key, ":", value)

student = {
    "name": "Arun",
    "age": 20,
    "grade": "A"
}

display_student(student)

# Output

name : Arun
age : 20
grade : A

# FILE HANDLING

• File Handling is used to store and retrieve data from files.
• Python provides built-in functions to create, read, write and append files.
• open() function is used to open a file.

# File Modes

• "r"  - Read mode
• "w"  - Write mode
• "a"  - Append mode
• "x"  - Create mode

# Creating and Writing to a File

• Write mode creates a new file if it does not exist.
• Existing content will be overwritten.

# Example :

file = open("sample.txt", "w")

file.write("Welcome to Python Programming")

file.close()

print("Data Written Successfully")

# Output

Data Written Successfully

# Reading a File

• Read mode is used to read the contents of a file.

# Example :

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

# Output

Welcome to Python Programming

# Appending Data to a File

• Append mode adds new data without removing existing data.

# Example :

file = open("sample.txt", "a")

file.write("\nLearning File Handling")

file.close()

print("Data Appended Successfully")

# Output

Data Appended Successfully

# Reading File Line by Line

# Example :

file = open("sample.txt", "r")

for line in file:
    print(line)

file.close()

# Output

Welcome to Python Programming
Learning File Handling

# Using with Statement

• The with statement automatically closes the file.

# Example :

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Output

Welcome to Python Programming
Learning File Handling

# File Methods

• read()
  Reads the entire file.

• readline()
  Reads one line at a time.

• write()
  Writes data into a file.

• close()
  Closes the file.

# Example :

file = open("sample.txt", "r")

print(file.readline())

file.close()

# Output

Welcome to Python Programming

# Passing File Content to a Function

def display_content(text):
    print("File Content:")
    print(text)

with open("sample.txt", "r") as file:
    data = file.read()

display_content(data)

# Output

File Content:
Welcome to Python Programming
Learning File Handling


# Ex 5

employee = {
    'emp_id': 101,
    'name': "Elakiya",
    'department': "IT",
    'salary': 45000
}

for i, j in employee.items():
    print(i, " : ", j)

# Output

emp_id  :  101
name  :  Elakiya
department  :  IT
salary  :  45000

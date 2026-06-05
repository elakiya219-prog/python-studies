# LIST

• A List is a collection that stores multiple items in a single variable.
• Items are enclosed within square brackets [ ].
• A list can contain different data types.
• It is mutable (elements can be changed after creation).
• Duplicate values are allowed.

# Example :

colors = ["Red", "Blue", "Green"]
print(colors)

details = ["Rahul", 20, 9.1]
print(details)

# Accessing List Elements

• Every item in a list has a position called an Index.
• Index numbering starts from 0.
• Elements can be accessed using their index value.

# Example :

colors = ["Red", "Blue", "Green"]

print(colors[0])
print(colors[2])

# Output

Red
Green

# Negative Indexing

• Negative indexes are used to access elements from the end of the list.
• -1 represents the last element.

# Example :

colors = ["Red", "Blue", "Green"]

print(colors[-1])

# Output

Green

# Updating Elements in a List

• Existing elements can be replaced using their index value.

# Example :

colors = ["Red", "Blue", "Green"]

colors[0] = "Yellow"

print(colors)

# Output

['Yellow', 'Blue', 'Green']

# Common List Methods

• append()
  Adds an element to the end of the list.

• insert()
  Inserts an element at a specified index.

• remove()
  Deletes a particular element.

• pop()
  Removes an element using its index.
  If no index is given, the last element is removed.

• len()
  Returns the total number of elements.

• sort()
  Arranges elements in ascending order.

• reverse()
  Reverses the order of elements.

• clear()
  Removes all elements from the list.

# Example :

numbers = [40, 10, 30]

print("Original List :", numbers)

numbers.append(50)
print("After append() :", numbers)

numbers.insert(1, 20)
print("After insert() :", numbers)

numbers.remove(30)
print("After remove() :", numbers)

deleted = numbers.pop(2)
print("After pop() :", numbers)

print("Removed Item :", deleted)

print("Length :", len(numbers))

numbers.sort()
print("After sort() :", numbers)

numbers.reverse()
print("After reverse() :", numbers)

numbers.clear()
print("After clear() :", numbers)

# Output

Original List : [40, 10, 30]
After append() : [40, 10, 30, 50]
After insert() : [40, 20, 10, 30, 50]
After remove() : [40, 20, 10, 50]
After pop() : [40, 20, 50]
Removed Item : 10
Length : 3
After sort() : [20, 40, 50]
After reverse() : [50, 40, 20]
After clear() : []

# Sending a List to a Function

• A list can be passed to a function as an argument.
• The function can access and process all elements of the list.

# Example : Display Student Names

def show_students(students):
    print("Student Names:")

    for student in students:
        print(student)

students = ["Arun", "Priya", "Kavin"]

show_students(students)

# Output

Student Names:
Arun
Priya
Kavin

# FOR LOOP

• A for loop is used to repeat a block of code multiple times.
• It is mainly used to iterate through a sequence such as a list, tuple, string, or range.
• The loop continues until all items in the sequence are processed.

# Example :

for i in range(5):
    print(i)

# Output

0
1
2
3
4

# Using for loop with a String

• A string consists of characters.
• A for loop can access each character one by one.

# Example :

name = "Python"

for letter in name:
    print(letter)

# Output

P
y
t
h
o
n

# Using for loop with a List

• A for loop can be used to traverse all elements in a list.

# Example :

fruits = ["Apple", "Mango", "Grapes"]

for fruit in fruits:
    print(fruit)

# Output

Apple
Mango
Grapes

# Using range() Function

• range() generates a sequence of numbers.
• The starting value is 0 by default.

# Example :

for num in range(1, 6):
    print(num)

# Output

1
2
3
4
5

# Nested for Loop

• A for loop inside another for loop is called a nested loop.

# Example :

for i in range(3):
    for j in range(2):
        print(i, j)

# Output

0 0
0 1
1 0
1 1
2 0
2 1

# break Statement

• break is used to terminate the loop immediately.

# Example :

for num in range(1, 6):
    if num == 4:
        break
    print(num)

# Output

1
2
3

# continue Statement

• continue skips the current iteration and moves to the next iteration.

# Example :

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Output

1
2
4
5

# Passing Data to a Function using for Loop

def display_numbers(numbers):
    print("Numbers are:")

    for num in numbers:
        print(num)

numbers = [10, 20, 30, 40]

display_numbers(numbers)

# Output

Numbers are:
10
20
30
40

# TUPLE

• A Tuple is an ordered collection of elements.
• It is enclosed within parentheses ().
• Different data types can be stored in a tuple.
• It is immutable (cannot be modified after creation).
• Duplicate values are allowed.

# Example :

colors = ("Red", "Blue", "Green")
print(colors)

student = ("Karthik", 21, 8.9)
print(student)

# Accessing Tuple Elements

• Each element in a tuple has an index value.
• Index starts from 0.

# Example :

colors = ("Red", "Blue", "Green")

print(colors[0])
print(colors[1])

# Output

Red
Blue

# Negative Indexing

• Negative indexing accesses elements from the end.

# Example :

colors = ("Red", "Blue", "Green")

print(colors[-1])

# Output

Green

# Tuple Slicing

• Slicing is used to access multiple elements.

# Example :

colors = ("Red", "Blue", "Green", "Yellow")

print(colors[1:3])

# Output

('Blue', 'Green')

# Tuple Methods

• count()
  Returns the number of times an element appears.

• index()
  Returns the position of a specified element.

# Example :

numbers = (10, 20, 10, 30, 10)

print("Count of 10 :", numbers.count(10))
print("Index of 30 :", numbers.index(30))

# Output

Count of 10 : 3
Index of 30 : 3

# Length of Tuple

• len() returns the total number of elements.

# Example :

numbers = (5, 10, 15, 20)

print(len(numbers))

# Output

4

# Traversing a Tuple using for Loop

# Example :

cities = ("Chennai", "Coimbatore", "Madurai")

for city in cities:
    print(city)

# Output

Chennai
Coimbatore
Madurai

# Passing Tuple to a Function

• A tuple can be passed as an argument to a function.

# Example :

def display_subjects(subjects):
    print("Subjects List:")

    for subject in subjects:
        print(subject)

subjects = ("Maths", "Physics", "Chemistry")

display_subjects(subjects)

# Output

Subjects List:
Maths
Physics
Chemistry

#TASK 
movies = {
    "Vijay": ["Ghilli", "Thuppakki", "Mersal", "Master", "Leo", "Pokkiri", "Kaththi", "Bigil", "Theri", "Sarkar"],

    "Ajith": ["Mankatha", "Billa", "Viswasam", "Veeram", "Vedalam",  "Aarambam", "Yennai Arindhaal", "Citizen", "Thunivu", "Valimai"],

    "Rajinikanth": ["Baasha", "Sivaji", "Enthiran", "Jailer", "Padayappa", "Annamalai", "Kabali", "Petta", "Muthu", "Chandramukhi"],

    "Suriya": ["Ghajini", "Vaaranam Aayiram", "Singam", "Ayan", "Soorarai Pottru", "Jai Bhim", "24", "Kaakha Kaakha", "Vel", "Pasanga 2"],

    "Dhanush": ["Asuran", "VIP", "Karnan", "Thiruchitrambalam", "Polladhavan", "Aadukalam", "Maari", "Velaiilla Pattadhari", "Captain Miller", "Raayan"],

    "Sivakarthikeyan": ["Doctor", "Don", "Amaran", "Remo", "Maaveeran", "Ethir Neechal", "Rajini Murugan", "Namma Veettu Pillai", "Varuthapadatha Valibar Sangam", "Kedi Billa Killadi Ranga"]
}

top_x = int(input("Please enter top x number (1-10): "))
actor = input("Please enter the actor name: ")

if actor in movies and 1 <= top_x <= 10:
    print(f"\nHere are the top {top_x} super hit movies of {actor}")

    for i in range(top_x):
        print(f"{i+1}. {movies[actor][i]}")
else:
    print("Invalid actor name or number")

# Output 
Please enter top x number (1-10): 7
Please enter the actor name: Suriya

Here are the top 7 super hit movies of Suriya
1. Ghajini
2. Vaaranam Aayiram
3. Singam
4. Ayan
5. Soorarai Pottru
6. Jai Bhim


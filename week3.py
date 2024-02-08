## Week 3
# This is an IDE, but it has a terminal built into it, it also has a terminal running python, which I'll be using to
# demonstrate the basic functions of Python

# Use option + shift + e to run specific lines in the console

## Booleans
# We've already talked about what booleans are and why they're important in programming. In python True and False are each
# evaluated as booleans. Any number, or other data is evaluated as True, while 0 or an empty data set will be evaluated
# as False.

bool(0)
bool(1)
bool(23)
bool([])
bool([1, 2, 3])
bool([False])

# there are a few ways to evaluate the boolean value of statements as well, these will be useful later for controlling
# loops and functions

2 > 1
2 == 2
1 != 2
2 * 8 == 2 ** 4
1 > 2
1 == 10
5 + 2 == 8


## Integers and Floats
# Integers are whole numbers, floats are decimals. Each can be useful in its own way, and the difference is more important
# in lower level programming languages. Python will automatically typecast them appropriately, but you can manually change
# the type if you want.
type(5)
type(5.0)
type(2)
type(5/2)
int(5/2)
int(2.9)
float(5)

# you can do any kind of math in python, either using the basic built in commands and building your own functions to handle
# more complex problems, or using modules like 'math' which is great for algebraic problems; 'numpy' which is used for arrays
# and matrices; and 'scipy' for calculus, statistics, and many other higher level maths

# for now, here are the basic math operators in python
1 + 9    # addition
1 - 9    # subtraction
2 * 6    # multiplication
4 ** 2   # exponents
4 ** .5  # also exponents
4 / 3    # division
4 % 3    # modulus division
4 // 3   # floor division


## Strings
# Strings are text, and can be printed to the output. They're useful for mapping where errors are happening in your
# code, or for feedback to the user. Strings are a very simple form of data storage, you can assign a string of data to
# a variable and call it later. You can't actually edit strings once they're stored, they're 'immutable,' but you can
# circumvent this by making the changes you want, then saving the new string to the same variable.

print("Hello, world!")
type("Hello, world!")

# concatenation
string1 = "Hello,"
string2 = " world!"
concatenatedString = string1 + string2
print(concatenatedString)

# indexing
stringIndex = "12345"
print(stringIndex[0])
print(stringIndex[4])
print(stringIndex[1:3])
print(stringIndex[:2])
print(stringIndex[2:])

# format
print("hello, {}".format("world"))


# strip, replace, split, join
messyString = "                  this string has a lot of white space             \n     and multiple lines      \n      now what?"
print(messyString.strip())
print(messyString.strip().split())
print(messyString.strip().split('\n'))
print(messyString.strip().split('a'))
print(' '.join(messyString.strip().split('\n')))

print(messyString.replace('\n', ' '))
print(messyString.replace(' ', '_'))
print(messyString.replace('string', 'text-based data structure'))

# split and join are particularly useful for data management
print(messyString)
print(' '.join(messyString.strip().split()))¯

messyData = ["A bunch of numbers:", '1', '1', '2', '3', '5', '8', '13', '21', '34']
print(messyData)
print(' '.join(messyData))
print('\n'.join(messyData))



ex = "Here's a string with some numbers that you're interest in: 1, 2, 3, 4, 5"
print(ex)

ex1 = ex.split(': ')
print(ex1)

ex1 = ex1[1]
print(ex1)

ex1 = ex1.split()
print(ex1)


## Tuples
# Tuples are another simple type of data. Like strings, they're immutable, ordered, and indexed, but where a string is one
# big piece of text, tuples can store multiple pieces of data of different types. The data stored in a tuple is fixed in
# position and not editable, which allows that data to be stored with fewer tags, so they need less space in memory and can
# be navigated faster. Tuples are set with parentheses and the items are separated by commas.

myTuple = (7, 2, "String", 5, True)
print(myTuple)
print(myTuple[0])
print(myTuple[0:3])
print(myTuple[-1])


## Lists
# Lists are one of the most useful data storage methods in Python, they're mutable, ordered, and can store all the basic
# types of data. They're almost identical to tuples aside from the mutability, and are set with square brackets instead
# of parentheses. Items are still separated with commas. Since they're mutable, there are many functions that can be applied
# to lists to add, remove, sort, or otherwise manipulate the data stored in them.

myList = [5, 3, 7, 2, 9, 8, 4, 1, 6]
myList.sort()  # since lists are mutable, this actually changes the list without having to reassign the output to its own variable
print(myList)
myList.sort(reverse=True)
print(myList)

myList = ['a', 'e', 'w', 'a', 't', 'r', 'v', 'a']
myList.sort()
print(myList)
myList.count('a')
myList.count('x')

myList.append('x')
myList.count('x')

myList.insert(-3, 'u')
print(myList)

myList.remove('a')
print(myList)

myList.pop(1) # pop without an argument will just pop the last value in the list
print(myList)

## list comprehensions
# the following is copied from the python documentation:
# example 1
# creating a list with a for-loop
squares = []
for x in range(10):
    squares.append(x**2)
squares

# example 2
# list comprehension
squares = [x**2 for x in range(10)]
squares
# example 2 is more efficient and readable. list comprehension lets you create a list in-place with a function


## Dictionaries
# Dictionaries are the most complex of the basic python data types. They're also the most detailed. They consist of an
# array of Key:Value pairs. The keys are immutable and unique, while the values are mutable. So, the Keys can be
# any immutable data type (string, integers, tuples), while the values can be any data type (strings, tuples, lists, so on).
# The dictionary as a whole is mutable. They're indexed by their keys. Dictionaries are assigned with the curly brackets {},
# and in the Key:Value pattern, separated by commas.

myDict = {1:1, 2:4, 3:9, 4:16, 5:25}
print(myDict)
print(myDict[3])
print(myDict.keys())
print(myDict.values())
print(myDict.items())
bool(1 in myDict.keys())

# Mutability
myDict[1] = "one"
print(myDict)
myDict.update({1: "uno"})
print(myDict)

myDict[6] = 36
print(myDict)
myDict.update({"new key": "new value"})
print(myDict)

myDict.pop('new key')
del(myDict[1])
print(myDict)

myDict.clear()
print(myDict)

del(myDict)
print(myDict)

myDict = {}
for i in range(1,11):
    myDict[i] = i**2
print(myDict)


## Functions
# Functions let you easily repeat a series of code for different inputs. In python, they are defined using the `def` keyword.
# They can accept parameters and return outputs, making code reusable and modular.

# Defining a function
def newFunction():
    """
    This is a docstring, it can be called with help(function). It starts and ends with three quotation marks.
    Notice the naming convention for python functions. It's not mandatory, but this is called camelCase. The first letter
    is lower case while each subsequent word in the name is capitalized. This just makes it more readable, and is my
    personal preferred method. The officially recommended style (according to Python Enhancement Protocol 8, PEP8) is
    snake_case, where words are lower case but separated by underscores.
    """
    pass


def multiply(x, y):
    product = x * y
    return product


# Calling a function
multiply(2, 3)

print(f"The product of 2 and 3 is {multiply(2, 3)}")

if multiply(5, 10) == 5 * 10:
    print(True)

for x in range(10):
    for y in range(10):
        print(multiply(x, y))

# Functions can have default parameters
def greet(name="World"):
    """Greet a person with a given name, default is 'World'."""
    print(f"Hello, {name}!")


greet()  # Outputs: Hello, World!
greet("Pythonista")  # Outputs: Hello, Pythonista!


# Functions can return multiple values as a tuple
def arithmetic_operations(x, y):
    """Return basic arithmetic operations between two numbers."""
    sum = x + y
    difference = x - y
    product = x * y
    division = x / y if y != 0 else None
    return sum, difference, product, division


# Unpacking returned tuple
sum, difference, product, division = arithmetic_operations(10, 5)
print(f"Sum: {sum}, Difference: {difference}, Product: {product}, Division: {division}")


## Classes
# Classes are the blueprint for creating objects in Python, they contain variables and functions (methods) in a single entity.
# Python is an object-oriented programming language, and classes play a significant role in this paradigm.

class Calculator:
    """A simple calculator class."""

    def __init__(self, value=0):
        """Initialize the calculator with a default value."""
        self.value = value

    def add(self, x):
        """Add a number to the calculator's value."""
        self.value += x

    def multiply(self, x):
        """Multiply the calculator's value by a number."""
        self.value *= x

    def get_value(self):
        """Return the current value."""
        return self.value


# Creating an instance of Calculator
calc = Calculator()
calc.add(5)
calc.multiply(2)
print(f"The current value of the calculator is {calc.get_value()}")





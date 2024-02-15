## Week 4
# Reminder:
# Use "option + shift + e" to run only the selected lines in the python console. You can run one line at a time, or multiple highlighted lines

## Dictionaries
# just to recap from last week, and because dictionaries are very useful for organizing data
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

## Loops
# loops let you iteratively perform a function, either continuously while a condition is met, or for each item in a sequence

## for
# the for loop iterates through a sequence of items and performs some action for each
myList = ["apple", "banana", "cookie"]
for item in myList:
    print(item)

for item in myList:
    if 'a' in item:
        print(item)

for i, item in enumerate(myList):
    print(i, item)

for i, item in enumerate(myList):
    myList[i] = item + "s"
print(myList)


numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numList:
    if num ** .5 == 3:
        print(num)

# the i convention, index or item
for i in range(100):
    if i % 2 == 0:
        print(i)

# nests
for i in range(10):
    for j in range(10):
        print(i*j)

## while
# the while loop repeats a chunk of code so long as some condition is met
x = 0
while x < 10:
    print("x < 10")

x = 0
while x < 10:
    print(x, " <10")
    x += 1
print("done")

x = 0
while True:
    if x**2 == 625:
        False
        # break
    else:
        print(x)
        x += 1


## input()
# this lets you take input from the user to use in your script, be careful about type casting. Input will be read as a
# string. If you want a specific type of data, cast it as such eg: int(input("type your input here")) to convert whatever
# input to an integer

input()
x = input("type your input below:\n")
print(x)

x = input("What's the square root of 625")
if x == "25":
    print("correct")
else:
    print("Absolutely not")

## Practice problem 1
# write a script that takes a filename or path as input and returns the name and the extension as a key:value pair
# examples: "/users/nick/documents/r02a.rdf" "numbers.2019.csv" "Slides_feb_2024.ppt"



## Modules
# Existing scripts that you can import into your code to execute their functions and use the returned data, or use their
# classes to create your objects. Modules will also execute when imported, so beware of malware. Pycharm's builtin "Python Packages"
# uses the Python Package Index (PyPI) which includes official and community packages. Official packages are safe to use,
# and community packages with a lot of support and documentation are generally safe, but you should review less-known
# packages before executing them.
import os


## OS module
# this lets you access the operating system directly, similar to when you use the terminal or command line

os.getcwd()
os.chdir('/')
os.getcwd()

os.chdir('/users/nick/desktop/anth299a')
os.listdir()
type(os.listdir())
os.listdir().sort()

for i in os.listdir():
    print(i)

# There's also the following which can be useful sometimes, but we won't be using them
# os.mkdir(path, mode=0o777) creates a directory with read/write/execute permissions for all groups
# os.rmdir() removes the specified directory
# os.path.exists() checks existence of a path

## Practice problem 2
# write a script that will return the names and extension of files/subdirectories within a directory on your computer
# example: create a new folder on your desktop to save the class material you've downloaded so far, then use that to test your script



## re
# Regular expressions are patterns that your interpreter can search for. This will be a major tool in the rest of the class.
# We'll spend an entire lecture talking about how to use regexes, how to design and trouble shoot them, then do a lot of
# practice.


## Pandas module
# Pandas is a comprehensive data analysis tool built for Python. Before you can use it, you'll need to install it through
# the Python Packages tool. Pandas has two types of organizational models for data: series and dataframes. We'll go more
# in depth next week, but here's an example of how useful Pandas is

import pandas as pd

file = "/users/nick/documents/wastewater.csv"
df = pd.read_csv(file)

rows = df.shape[0]
print(rows) #572955

filtered_df = df.loc[df['wwtp_jurisdiction'] == 'Maryland']

print(filtered_df)

pd.set_option('display.max_rows', None)
print(filtered_df)


## beautifulsoup4
# the bs4 module is a great in-between step for webscraping. Specifically, it contains many tools for parsing HTML or XML
# This is one of the other main modules we'll be using.


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
    pass    #this is an empty statement, similar to null

# pass allows you to have an empty function. It tells the interpreter to just pass over that statement. Otherwise, since
# your function has a colon ":", your interpreter is expecting some line of code to execute, and will give you an error
# if it doesn't find one. "pass" tells the interpeter that his is intentional, and to do nothing, just exit the function.
# This can be useful if you're just organizing your functions and don't have executable code in them yet. It's also useful
# for trouble shooting, since you can add a pass statement ahead of questionable code to see if everything up to that
# point runs successfully.



def multiply(x, y):
    product = x * y
    print(product)
    # return product


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


greet()
greet("Nick")


# Functions can return multiple values as a tuple
def arithmetic_operations(x, y):
    """Return basic math operations for two numbers."""
    sum = x + y
    difference = x - y
    product = x * y
    division = x / y if y != 0 else None
    return sum, difference, product, division


# Retrieving the returned data takes some precision. Each item is returned in the order you asked for it in the return
# method, so the variables have to be assigned in that same order

outputs = arithmetic_operations(10, 5)
print(outputs) # note that this is a tuple. It has parentheses and each item is separated by commas.
outputs[0]
outputs[1]
outputs[-1]

sum, difference, product, division = arithmetic_operations(10, 5)
print(f"Sum: {sum}, Difference: {difference}, Product: {product}, Division: {division}")

## Practice problem 3
# Create a function that asks the user for a directory in their computer, then return that directory along with the file
# extensions present and their descriptions



## Classes
# Classes are the outline for creating objects in Python, they contain variables and functions (methods) in a single entity.
# Python is an object-oriented programming language, and classes play an important role in this practice.

class Calculator:
    """A simple calculator class"""

    def __init__(self, value=0):
        """Initialize the calculator with a default value"""
        self.value = value

    def add(self, x):
        """Add a number to the calculator's value"""
        self.value += x

    def multiply(self, x):
        """Multiply the calculator's value by a number"""
        self.value *= x

    def get_value(self):
        """Return the stored value"""
        return self.value


# Creating an instance of Calculator
calc = Calculator()
calc
calc2 = Calculator()
calc2
calc.add(5)
calc.multiply(2)
print(f"The current value of the calculator is {calc2.get_value()}")



# Appendix

ext_dict = {
    "__meta_data__":{"title": "File Extension Dictionary", "description":"This is a dictionary containing several types of file extensions as keys, with a brief description stored as their values", "size":10},
    'pdf': "Portable Document Format, similar to printing a document, a PDF allows you to dsiplay content digitally in a consistent format regardless of the application used",
    'txt': "A plain text file, displays strings and characters with very basic formatting",
    'docx': "A fancier version of a text file with more complex formatting",
    'ppt': "Powerpoint slides, good for presentations",
    'csv': "Comma-Separated Values, values organized into columns and rows, similar to an excel spreadsheet",
    'xlsx': "Excel document, it is what it is",
    'py': "Python file, executes python code when run as an executable",
    'sql': "Structured Query Language, executes code to create, modify, or delete databases, or a series of queries to return information",
    'db': "Database, stores information in a structured, computer-accessible way. Not human-readable.",
    'sh': "Shell script, executes shell commands in the specified shell interpreter",
    'rdf': "Resource Description Framework, originally meant to be a framework for website metadata, it's now used for storing graph data"
}

mut_dict = {
    'G9610358': '13973T 189C 794A 9100G',
    'G7958610': '13973T 189C 3921T 794A',
    'G7925831': '13973T 189C 794A 8531G',
    'G7802158': '13973T 189C 7444A 794A 9100G',
    'G7653278': '13973T 189C 3921T 794A',
    'G5748816': '13973T 189C 794A 9100G',
    'G4166258': '13973T 189C 7444A 794A 9100G',
    'G3519680': '13973T 189C 3921T 794A',
    'G2256450': '13973T 189C 794A 8531G',
    'G8359235': '13973T 15172A 189C 794A',
    'G7796189': '13973T 189C 794A 9100G',
    'G7042478': '13395G 13973T 189C 794A',
    'G7036930': '13973T 189C 794A 9100G',
    'G5360000': '13973T 189C 5177A 794A',
    'G4514895': '13191C 13973T 15790T 189C 794A',
    'G3946282': '11617C 13973T 15773A 189C 794A 8531G',
    'G2624978': '13973T 189C 794A 9100G',
    'M7075511': '12630A 16352C 3921A 9365T',
    'M1257559': '16297C',
    'G4402217': '13973T 16263C 189C 794A 8531G',
    'G3724950': '13973T 14198A 189C 794A',
    'G2908230': '13973T 189C 794A',
    'M3119807': '9100G',
    'G8984148': '13973T 185A 189C 794A',
    'G6646803': '13973T 16293G 189C 794A 8531G',
    'G2084869': '13973T 143A 189C 794A',
    'G8311346': '13973T 16274A 189C 794A 8531G',
    'G9952523': '13973T 14198A 189C 794A',
    'G9781010': '13973T 189C 3921T 794A',
    'G8296409': '13973T 189C 794A 9100G',
    'G6709576': '13191C 13973T 189C 794A',
    'G6296555': '10586A 13973T 189C 794A 9100G',
    'G6235448': '13973T 14198A 1780C 189C 794A',
    'G5219004': '13973T 189C 794A',
    'G4774700': '13973T 189C 794A 9100G',
    'G3320095': '13973T 189C 794A',
    'G2734018': '13973T 189C 794A 9100G',
    'G2730569': '13973T 189C 794A 9100G',
}





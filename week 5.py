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

def multiply(x, y):
    product = x * y
    # print(product)
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
print(outputs) # note that this is a tuple. It has parentheses and each item is separated by commas. (indexed, ordered)
outputs[0]
outputs[1]
outputs[-1]

sum, difference, product, division = arithmetic_operations(10, 5)
print(f"Sum: {sum}, Difference: {difference}, Product: {product}, Division: {division}")



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

## Pandas
# This is a major data analysis tool. It's particularly useful in manipulating .csvs, or any 2-D array of information
# It works similarly to excel, but it's fully integrated into python.

# it's conventional to import with the variable 'pd' :
import pandas as pd


## Basics

# 1D series
# creates and indexed sequence of data, similar to a list, but you can make the index whatever you want
myList = [1, 2, 3, 4, 5]
mySeries = pd.Series(myList)
mySeries # each piece of data (1,2,3,4,5) has an index label (0-5)
mySeries[0]

myDict = {"Alice": 47392839, "Bob": 3132793, "Eve": 23980498}
mySeries = pd.Series(myDict)
mySeries # again, each piece of data (47392839, 3132793, 23980498) has an index label (Alice, Bob, Eve)
mySeries[0]
mySeries["Alice"]


# importing data from .csv
file = '/users/nick/desktop/anth299a/Data Sets/Historic Global Temperatures.csv'
df = pd.read_csv(file, index_col="Date")
print(df)

pd.set_option('display.max_rows', None)
print(df)
df.shape[0]
pd.reset_option('display.max_rows')
df
df.head()
df.tail()

## Navigation

# .loc lets you navigate by column titles and index positions
# : can be used as a wildcard, or slice
df.loc[191001, 'Africa']
df.loc[191001, 'Europe':'Asia']
df.loc[:, 'Africa']

# .iloc lets you navigate by integer location
# same mechanics, just using a number instead. This is more convenient for iterating through loops
df.iloc[0, 2]

df.iloc[0:5, 0:5]
rows = df.shape[0]
cols = df.shape[1]
for i in range(rows):
    for j in range(cols):
        print(df.iloc[i, j])

df.sort_values(by='Asia')


## Basic stats
df.describe()
type(df.describe())
df.loc[198001:, :].describe()
df.mean()
df.mean(axis=1)
df.loc[:, 'North America'].mean()

for i in list(df):
    print(f'The mean temperature variation of {i} is {df.loc[:, i].mean()}')

# Transpose
df.T
df

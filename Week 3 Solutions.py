## Problem 1
messyString = "define Any genetics. can biologist"
myList = messyString.split()
myList.sort()
myList
newString = ' '.join(myList)
print(newString)

## Problem 2
base = 2
height = 10
area = base*height/2
print(area)

## Problem 3
file = input("Type in a file name")
pos = 0
while file[pos] != '.':
    pos += 1
print(file[pos:])
# optional
# create a dictionary defining the different possible file extensions and return that as well

## Problem 4
list = [1,1, 2, 3, 5, 8, 13]
sum = 0
for i in list:
    sum += i

## Problem 5
word = "abba"
# word = "racecar"
# word = "palindrome"
count = 0
for i in range(len(word)):
    if word[i] == word[-(i+1)]:
        count += 1
if count >= len(word):
    print(word, " is a palindrome")
else:
    print(word, " is not palindrome")

## Problem 6
import random

# This just creates a random nucleotide sequence 1000 characters long to demonstrate that the code works for any
# nucleotide sequence
sequence = ''.join(random.choices(('A', 'C', 'G', 'T'), k=1000))

a = sequence.count('A')
c = sequence.count('C')
g = sequence.count('G')
t = sequence.count('T')

cg = str(((c+g)/(a+c+g+t))*100)
print(cg[:4], '%')
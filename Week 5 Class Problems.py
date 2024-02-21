## Problem 1
# Using the "1976-2020-president.csv" data set, write a function that allows the user to get total votes cast for a
# specific person in a specific state in a specific year.
# Bonus, also include the percentage of the total vote that that candidate got by state and year.

# hint use input(), nested for loops, elif series, and df.loc[]
# don't forget input() takes inputs as string data types, and don't forget cases sensitivity













## A solution



import pandas as pd
file = '/users/nick/desktop/anth299a/Data Sets/1976-2020-president.csv'
df = pd.read_csv(file)
names = []
rows = df.shape[0]
for i in range(rows):
    if df.loc[i, 'candidate'] not in names:
        names.append(df.loc[i, 'candidate'])


def myFunc(person = None, year = None, state = None):
    if person == None:
        person = input("Choose a person:\n")
    if year == None:
        year = int(input("Choose a year:\n"))
    if state == None:
        state = input("Choose a state:\n")

    if person not in names:
        person = input("Not in list of candidates, double check capitalization and grammar, then try again:\n")

    for i in range(rows):
        if df.loc[i, 'year'] == year:
            if df.loc[i, 'state'] == state:
                if df.loc[i, 'candidate'] == person:
                    print(df.loc[i, 'candidatevotes'])

myFunc('CARTER, JIMMY', 1976, 'ALABAMA')
myFunc()
## Week 7
## Review

# Formatted strings
name = "world"
print("Hello, {}".format(name))
print(f"Hello, {name}")
name = input("What's your name?\n")
print("Hello, {}".format(name))
print(f"Hello, {name}")

# Raw strings
# Adding an 'r' before your string tells the interpreter to read it as raw text. This ignores escape characters.
# This is useful for regular expressions with special sequences, or for Windows filepaths
string = "Line 1\nLine 2"
print(string)
string = r"Line 1\nLine 2"
print(string)

# Boolean operations
# There are a few ways to evaluate the boolean value of statements as well, these will be useful later for controlling
# loops and functions
2 > 1
2 == 2
1 != 2
2 * 8 == 2 ** 4
1 > 2
1 == 10
5 + 2 == 8

# Pandas filters
# Filtering is a technique to return a new series or dataframe that only includes data that meets your specified criteria
import pandas as pd

file = '/users/nick/desktop/anth299a/Data Sets/Historic Global Temperatures.csv'
df = pd.read_csv(file)

# Here we create a series that filters out just the "Date" column from our df
df["Date"]
type(df["Date"])

# This part creates another series, where each value is the boolean value of the right side of the statement
boolean_series = df["Date"] > 198001
type(boolean)

filter1 = df[df["Date"] > 198001]
filter1

filter2 = df[(df["Date"] > 198001) & (df["Europe"] > 0)]
filter2
type(filter1)

# dictionaries
# functions
# when to use what

import pandas as pd
df1 = pd.DataFrame(columns=["Haplogroup", "Shared", "HaploFamily"])
df2 = df1.copy(deep=False)
list1 = ["A1", "A1b12a", "C1a1a", "C1a1b", "C1a1c", "C1a1d", "B2b1a", "B2b1b", "B2b1c", "B2b1d"]
list2 = ["C1b2", "C2b2", "C3b2", "A11b12a", "A1b12a", "C1a1d", "B2b1b", "B2b11c", "B2b1e", "A1b"]
for i in range(len(list1)):
    df1.loc[i, "Haplogroup"] = list1[i]
    df1.loc[i, "HaploFamily"] = list1[i][:2]
    df2.loc[i, "Haplogroup"] = list2[i]
    df2.loc[i, "HaploFamily"] = list2[i][:2]

rows = df1.shape[0]
list3 = []
for i in range(rows):
    if (df1.loc[i, "Haplogroup"] == df2["Haplogroup"]).any():
        list3.append(df1.loc[i, "Haplogroup"])

haplotypes = []
for i in df1["Haplogroup"]:
    for j in df2["Haplogroup"]:
        if i == j:
            list3.append(i)

lst = [1, 2, 3, 3, 3]



## Week 10
# SQLite3
import sqlite3      # you might need to install from your package manager

database = "/users/nick/desktop/anth299a/example.db"
conn = sqlite3.connect(database)
cursor = conn.cursor()

# Data tyoes
# NULL, INTEGER, REAL, BLOB, TEXT
cursor.execute("DROP TABLE example") # This is just here to get rid of the table in case it already exists
cursor.execute('''
    CREATE TABLE example (
    name TEXT,
    rank INTEGER,
    score REAL
)
''')

cursor.execute("INSERT INTO example (name, rank, score) VALUES (?, ?, ?)", ('Alice', 1, 10.0))
cursor.execute("SELECT * FROM example")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT name FROM example")
data = cursor.fetchall()
print(data)

more_info = [('Bob', 3, 9.6), ('Eve', 5, 8.4), ('Darryl', 2, 9.8), ('Fred', 4, 8.9)]
for i in more_info:
    cursor.execute("INSERT INTO example (name, rank, score) VALUES (?, ?, ?)", (i[0], i[1], i[2]))

cursor.execute("SELECT * FROM example ORDER BY rank")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT * FROM example WHERE rank <= 3")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT * FROM example WHERE rank <= 3 ORDER BY rank")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT * FROM example WHERE rank <= 3 ORDER BY name")
data = cursor.fetchall()
print(data)

cursor.execute("SELECT * FROM example WHERE score < 9.0 AND score > 8.0")
data = cursor.fetchall()
print(data)


# Some statistics methods
# SUM, AVG, MIN, MAX, COUNT are all interchangeable in the following
cursor.execute("SELECT SUM(score) FROM example")
data = cursor.fetchall()
print(data)





#######################################################################################################################
## Part 2
# Reset the console here
# Use the script below to create the presidents database on your own local disk

import sqlite3
import pandas as pd

database = "/users/nick/desktop/anth299a/presidents.db"
conn = sqlite3.connect(database)
cursor = conn.cursor()

file = "/users/nick/desktop/anth299a/data sets/1976-2020-president.csv" # this csv can be found in the Week 5 module
df = pd.read_csv(file)

years = list(set(df['year']))
votes = df.groupby(['year', 'candidate'])['candidatevotes'].sum().reset_index()


for year in years:
    table_name = f"data{year}"
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            candidate TEXT,
            votes INTEGER,
            percent REAL
        );
    """)

for year in years:
    table_name = f"data{year}"
    insertion = f"INSERT INTO {table_name} (candidate, votes, percent) VALUES (?, ?, ?)"
    df = votes[votes['year'] == year]
    total = df['candidatevotes'].sum()
    for i in range(df.shape[0]):
        candidate = df.iloc[i]['candidate']
        candidatevotes = int(df.iloc[i]['candidatevotes'])
        percent = float(candidatevotes / total) * 100
        cursor.execute(insertion, (candidate, int(candidatevotes), percent))


# check that it works with this
cursor.execute("SELECT * FROM data1976")
print(cursor.fetchall())

years.sort()
for year in years:
    selection = f"SELECT SUM(votes) FROM data{year}"
    cursor.execute(selection)
    print(year, ":\n", cursor.fetchall())

conn.close()

# my interpreter did something weird and returned the votes as a byte. restarting the application fixed it.
# this is easy enough to convert back to human-readable integers though:
import struct
struct.unpack('<I', b'{A\x02\x00\x00\x00\x00\x00'[:4])[0]
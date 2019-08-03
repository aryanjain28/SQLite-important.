import sqlite3
import random

connection = sqlite3.connect("aryandb.db")
cursor = connection.cursor()

def createTables():
    cursor.execute("CREATE TABLE IF NOT EXISTS aryantableone (name TEXT, id INT, marks REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS aryantabletwo (name TEXT, points REAL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS aryantablethree (name TEXT, grade TEXT, age INT)")
    connection.commit()

def insertIntoTableOne(x,y,z):
    cursor.execute("INSERT INTO aryantableone (name, id, marks) VALUES (?, ?, ?)", (x,y,z))
    connection.commit()

def insertIntoTableTwo(x,y):
    cursor.execute("INSERT INTO aryantabletwo (name, points) VALUES (?, ?)", (x, y))
    connection.commit()

def insertIntoTableThree(x,y,z):
    cursor.execute("INSERT INTO aryantablethree (name, grade, age) VALUES (?, ?, ?)", (x, y, z))
    connection.commit()

def displayTable(x):
    draw = cursor.execute("SELECT * FROM "+x)
    [print(row) for row in draw.fetchall()]

def innerJoin():
    draw = cursor.execute("SELECT aryantableone.name FROM aryantableone "
                          "INNER JOIN aryantabletwo ON aryantableone.name = aryantabletwo.name "
                          "INNER JOIN aryantablethree ON aryantableone.name = aryantablethree.name ")
    [print(row) for row in draw.fetchall()]

def leftJoin():
    draw = cursor.execute("SELECT aryantableone.name FROM aryantableone "
                          "LEFT JOIN aryantabletwo ON aryantableone.name = aryantabletwo.name ")
                          # "LEFT JOIN aryantablethree ON aryantableone.name = aryantablethree.name ")
    [print(row) for row in draw.fetchall()]

def union():
    draw = cursor.execute("SELECT * FROM aryantableone "
                          "UNION "
                          "SELECT * FROM aryantablethree")
    [print(row) for row in draw.fetchall()]

def likeOperator():
    draw = cursor.execute("SELECT name FROM aryantableone "
                          "WHERE name LIKE '%n%' ")
    [print(row) for row in draw.fetchall()]

def globOperator():
    draw = cursor.execute("SELECT name FROM aryantableone "
                          "WHERE name GLOB '*[0-9]' ")
    [print(row) for row in draw.fetchall()]

def average():
    draw = cursor.execute("SELECT avg(marks) FROM aryantableone WHERE id<5")
    [print(row) for row in draw.fetchall()]

def count():
    draw = cursor.execute("SELECT count(*) FROM aryantableone")
    [print(row) for row in draw.fetchall()]

def sum():
    draw = cursor.execute("SELECT sum(marks) FROM aryantableone WHERE id<5")
    [print(row) for row in draw.fetchall()]

def min():
    draw = cursor.execute("SELECT min(marks) FROM aryantableone")
    [print(row) for row in draw.fetchall()]

def max():
    draw = cursor.execute("SELECT max(marks) FROM aryantableone")
    [print(row) for row in draw.fetchall()]



print("\n")
displayTable("aryantableone")

print("\n\n")
displayTable("aryantabletwo")

print("\n\n")
displayTable("aryantablethree")

# print("\n\n")
# innerJoin()

# print("\n\n")
# leftJoin()

# print("\n\n")
# union()

# print("\n\n")
# likeOperator()

# print("\n\n")
# globOperator()

# print("\n\n")
# average()

# print("\n\n")
# count()

# print("\n\n")
# sum()

# print("\n\n")
# sum()

# print("\n\n")
# max()

# print("\n\n")
# min()



#Code to change color back to white
#print('\033[38;2;225;225;225m')


import sqlite3

conn= sqlite3.connect('QuarterA2.db')
curse = conn.cursor()

curse.execute("SELECT * FROM sqlite_master WHERE type='table'")
#Reads all table
print(curse.fetchall())
print()

curse.execute("SELECT * FROM ACCT")
print(curse.fetchall())
print()

curse.execute("SELECT question FROM ACCT WHERE id = 1 ")
print(curse.fetchall())
print()
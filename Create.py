import sqlite3
import random


conn= sqlite3.connect('QuarterA2.db')
curse = conn.cursor()

#Table 1 labled ACCT
curse.execute('''CREATE TABLE IF NOT EXISTS ACCT
              question TEXT, answer TEXT''')


#Table 2 labled Databaase
curse.execute('''CREATE TABLE IF NOT EXISTS Database
              question TEXT, answer TEXT''')



#Table 3 labeld AssablyProg
curse.execute('''CREATE TABLE IF NOT EXISTS AssablyProg
              question TEXT, answer TEXT''')



#Table 4 labeled PythonProg
curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              question TEXT, answer TEXT''')


#Table 5 labled ComputerHardWear
curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              question TEXT, answer TEXT''')

# make a question array to store questions and answers as normal strings
#questions = []
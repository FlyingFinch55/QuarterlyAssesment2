import sqlite3
import random


conn= sqlite3.connect('QuarterA2.db')
curse = conn.cursor()

curse.execute('''CREATE TABLE IF NOT EXISTS ACCT
              question TEXT, answer TEXT''')

curse.execute('''CREATE TABLE IF NOT EXISTS Database
              question TEXT, answer TEXT''')

curse.execute('''CREATE TABLE IF NOT EXISTS AssablyProg
              question TEXT, answer TEXT''')

curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              question TEXT, answer TEXT''')

curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              question TEXT, answer TEXT''')

# make a question array to store questions and answers as normal strings
questions = []
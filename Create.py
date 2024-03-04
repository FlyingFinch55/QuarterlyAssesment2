import sqlite3
import random


conn= sqlite3.connect('QuarterA2.db')
curse = conn.cursor()

#Table 1 labled ACCT
curse.execute('''CREATE TABLE IF NOT EXISTS ACCT
              question TEXT, answer TEXT''')
curse.execute(''' INSERT INTO ACCT VALUES
              'What does Liabilty + Equaty=', 'Assets' 
              'What is the Net Income equation?', 'Revenue - Expenses'
              'Does Gross Profit= Revenue - Cost of Goods Sold? y/n, 'y'
              'What is the ratio of Current Assets divided by Current Liabilities?','Current Ratio'
              'True or False, Invetory Turnover messures how fast mechedise is sold.', 'True'
              'Sales are $18,000 with a discount of $500 and returns of $1,500. What is the Net Sales?', '16000'
              'What does COGS stand for?', "Cost of Goods Sold'
              'Is cash an Assest or an Liability?', "Asset
              'What does LIFO mean?', 'Last in First out'
              'What does FIFO mean?', 'First in Last out'
              ''')

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
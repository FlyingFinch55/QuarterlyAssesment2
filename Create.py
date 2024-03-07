import sqlite3

#Have to add all the questions one at a time 
#Between the insert and the conn.commit I will have all the questions commented

conn= sqlite3.connect('QuarterA2.db')
curse = conn.cursor()

#Code to add another question
#curse.execute('''INSERT INTO tableName VALUES
#              ('Question?','Answer')
#              ''')



#Table 1 labled ACCT
curse.execute('''CREATE TABLE IF NOT EXISTS ACCT
              (question TEXT, answer TEXT)''')


#The list of the 10 questions added
#1('What does Liabilty + Equity=', 'Assets' )
#2('What is the Net Income equation?', 'Revenue - Expenses')
#3('Does Gross Profit = Revenue - Cost of Goods Sold? y/n', 'y')
#4('What is the ratio of Current Assets divided by Current Liabilities?','Current Ratio')
#5('True or False, Inventory Turnover measures how fast merchandise is sold.', 'True')
#6('Sales are $18,000 with a discount of $500 and returns of $1,500. What is the Net Sales?', '16000')
#7('What does COGS stand for?', 'Cost of Goods Sold')
#8('Is cash an Asset or a Liability?', 'Asset')
#9('What does LIFO mean?', 'Last in First out')
#10('What does FIFO mean?', 'First in Last out')
#conn.commit()

#Table 2 labled Databaase
curse.execute('''CREATE TABLE IF NOT EXISTS Database
              (question TEXT, answer TEXT)''')


#The list of the 10 questions added
#1('Name the key that is the Primary Key of another entity.', 'Foreign Key')
#2('Name the key that is made of more than one attribute.', 'Compound Key')
#3('True or False, the Primary Key is not a unique attribute.','False' )
#4('True or False, there are 3 main types of anomalies.','True')
#5('Relationships are made using what?','Foreign Key')
#6('What color on the stop light method are 1 to 1 relationship?','Yellow')
#7('What color on the stop light method are 1 to many relationships?','Green')
#8('What color on the stop light method are many to many relationships?','Red')
#9('What entity is used to clear up many to many relationships?',' Intersection Entities')
#10('How many entities are in a binary model?(Number value)','2')
#conn.commit()

#Table 3 labeld AssablyProg
curse.execute('''CREATE TABLE IF NOT EXISTS AssablyProg
              (question TEXT, answer TEXT)''')




#Table 4 labeled PythonProg
curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              (question TEXT, answer TEXT)''')


#Table 5 labled ComputerHardWear
curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              (question TEXT, answer TEXT)''')


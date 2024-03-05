import sqlite3



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
curse.execute(''' INSERT INTO Database VALUES
              'Name the key that is the Primary Key of another entite.', 'Foreign Key'
              'Name the key that is made of more than one attrabute.', 'Compound Key'
              'True or False, the Primary Key is not a unique attrabute.','False' 
              'True or False, there are 3 main types of anomalies.','True'
              'Relationships are made using what?','Foreign Key'
              'What color on the stop light method are 1 to 1 relationships?','Yellow'
              'What color on the stop light mehtod are 1 to many relationships?','Green'
              'What color on the stop light method are many to many relationships?','Red'
              'What entite is used t clear up many to many relationships?',' Intersection Entities'
              'How many enitites are in a binary modle?(Number value)','2'
              ''')



#Table 3 labeld AssablyProg
curse.execute('''CREATE TABLE IF NOT EXISTS AssablyProg
              question TEXT, answer TEXT''')
curse.execute('''INSERT INTO AssablyProg VALUES
              'What does LDR stand for?','Load'
              'What does STR stand for?'.'Store'
              'What does MOV stand for?','Move'
              'What size is DCD?','word'
              'What size is DCW?','half word'
              'What size is DCB?','byte'
              'True or False ENDP ends the program.','True'
              'True or False, Array1 DCD 0, 0, 0, 0 makes an array of words all values 0.','True'
              'What does 0011 + 0010 equal?','0101'
              'What does 0100 + 0011 equal?','0111'
              ''')



#Table 4 labeled PythonProg
curse.execute('''CREATE TABLE IF NOT EXISTS PythonProg
              question TEXT, answer TEXT''')
curse.execute('''INSERT INTO PythonProg VALUES
              'What is the exstention for a python file?(Do not include the dot)',' py'
              'What is the exstention for a database file?(Do not include the dot)','db'
              'What is the varable type for strings?','str'
              'What is the varable type for integers?','int'
              'What is the varable type for real numbers?','float'
              'What is the varable type for booleans?','bool'
              'What type of varble does print("55") print?','string'
              'What type of varble does print(100) print?','int'
              'What symbol is used to comment a line?','#'
              'What does print(5+5) print?','10'
              ''')


#Table 5 labled ComputerHardWear
curse.execute('''CREATE TABLE IF NOT EXISTS ComputerHardWear
              question TEXT, answer TEXT''')


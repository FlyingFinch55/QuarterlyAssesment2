import sqlite3
import random

conn= sqlite3.connect('QuarterA2.db')
curse = conn.cursor()

print("Pick a topic for the quiz bowl.(Type in a number)")
catagory = input(" 1.Accoutning 2.Databases 3.Assebly Programing 4.Python Programming 5.Computer Hardware ")

if catagory == "1":
    curse.execute("SELECT * FROM ACCT")
    rows = curse.fetchall()
    questions = []
    for row in rows:
        questions.append((row[0], row[1]))

    selected_questions = random.sample(questions, 5)

if catagory == "2":
    curse.execute("SELECT * FROM Database")
    rows = curse.fetchall()
    questions = []
    for row in rows:
        questions.append((row[0], row[1]))

    selected_questions = random.sample(questions, 5)

if catagory == "3":
    curse.execute("SELECT * FROM AssablyProg")
    rows = curse.fetchall()
    questions = []
    for row in rows:
        questions.append((row[0], row[1]))

    selected_questions = random.sample(questions, 5)

if catagory == "4":
    curse.execute("SELECT * FROM PythonProg")
    rows = curse.fetchall()
    questions = []
    for row in rows:
        questions.append((row[0], row[1]))

    selected_questions = random.sample(questions, 5)


if catagory == "5":
    curse.execute("SELECT * FROM ComputerHardWear")
    rows = curse.fetchall()
    questions = []
    for row in rows:
        questions.append((row[0], row[1]))

    selected_questions = random.sample(questions, 5)




#rows = curse.fetchall()

#questions = []

#filling in the question array with questions and answers gotton from the fetch all
#for row in rows:
#    questions.append((row[0], row[1]))

# Select 5 random questions for the quiz
#selected_questions = random.sample(questions, 10)


score = 0
for TheQuestion, CorrAnswer in selected_questions:
    print(TheQuestion)
    userAns = input("Your Answer: ")
    if userAns.lower() == CorrAnswer.lower():
        print('\033[38;2;0;225;0m'+"Correct!")
        print('\033[38;2;225;225;225m')
        score = score + 1
    if userAns.lower() != CorrAnswer.lower():
        print('\033[38;2;225;0;0m'+"Wrong. The correct answer is " + CorrAnswer)
        print('\033[38;2;225;225;225m')

print ("Quiz End. Your score is " + str(score) + "/5")
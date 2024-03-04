import sqlite3

conn= sqlite3.connect('QuarterA2.db')
curse = conn.cursor()

rows = curse.fetchall()

questions = []

#filling in the question array with questions and answers gotton from the fetch all
for row in rows:
    questions.append((row[0], row[1]))

# Select 5 random questions for the quiz
selected_questions = (questions, 10)


score = 0
for TheQuestion, CorrAnswer in selected_questions:
    print(TheQuestion)
    userAns = input("Your Answer: ")
    if userAns.lower() == CorrAnswer.lower():
        print("Correct!")
        score = score + 1
    if userAns.lower() != CorrAnswer.lower():
        print("Wrong. The correct answer is " + CorrAnswer)

print ("Quiz End. Your score is " + str(score) + "/5")
from test import Question
from data import question_data
from quiz_brain2 import QuizBrain

question_bank = []

for i in question_data:
    question = i["text"]
    answer_1 = i["answer"]
    question_bank1 = Question(question, answer_1)
    question_bank.append(question_bank1)


test = QuizBrain(question_bank)
while test.still_has_questions():
    test.next_question()

print("You have completed the quiz")
print(f"Your final score was: {test.score} /{len(question_bank)} ")

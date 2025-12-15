from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Create a Question object from each entry in question_data
for question in question_data:
	question_text = question["text"]
	question_answer = question["answer"]
	new_question = Question(question_text, question_answer)
	question_bank.append(new_question)

# question_bank now contains Question objects for each entry in data.py
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_scrore()
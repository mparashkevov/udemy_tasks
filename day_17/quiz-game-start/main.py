from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Create a Question object from each entry in question_data
for item in question_data:
	q_text = item['text']
	q_answer = item['answer']
	new_question = Question(q_text, q_answer)
	question_bank.append(new_question)

# question_bank now contains Question objects for each entry in data.py
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_scrore()
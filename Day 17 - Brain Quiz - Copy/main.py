from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
#for question in question_data:
for i in range(0, 12):
    #question_text = question["text"]
    question_text = question_data[i]["text"]
    #question_answer = question["answer"]
    question_answer = question_data[i]["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print(f"Your Final Score is: {quiz.score}/{len(question_bank)}")
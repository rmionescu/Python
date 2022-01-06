from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_difficulty = question["difficulty"]
    question_category = question["category"]
    new_question = Question(question_text, question_answer, question_difficulty, question_category)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print(quiz_ui)
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

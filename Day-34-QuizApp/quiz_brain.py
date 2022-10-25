from html import unescape
from data import get_question_data
from question_model import Question


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = None
        self.set_questions()
        self.current_question = None
        self.isFinished = False

    def set_questions(self, diff=None, cat_id=None):
        question_bank = []
        for question in get_question_data(diff, cat_id):
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        self.question_list = question_bank

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text}"
        else:
            self.isFinished = True
            return f'Test Finished. Final score was: {self.score}/{self.question_number}. Play again?'

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def reset(self):
        self.score = 0
        self.question_number = 0
        self.isFinished = False

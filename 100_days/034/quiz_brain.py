import html
import data
from question_model import Question

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def reset(self):
        """Fetches 10 new questions and resets the quiz state."""

        new_data = data.get_questions()

        new_question_bank = []
        for question in new_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            new_question_bank.append(new_question)

        self.question_list = new_question_bank

        self.question_number = 0
        self.score = 0
        self.current_question = None

    def next_question(self):
        try:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text}"
        except IndexError:
            return f"Thanks, no more questions."


    def check_answer(self,user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            return True
        else:
            return False


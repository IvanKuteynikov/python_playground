class QuizBrain:
    def __init__(self, data):
        self.number_of_question = 0
        self.question_list = data
        self.total_questions = len(data)
        self.score = 0
    
    def still_has_questions(self):
        if self.number_of_question < self.total_questions:
            return True
        else:
            print("End of the game! Thanks for playing")
            print(f"Your score is: {self.score}/{self.total_questions}")
            
    def validate_input(self, prompt, options):
        while True:
            users_input = input(prompt).lower()
            if users_input in options:
                return users_input
            else:
                print(f"Please enter {" or ".join(options)}")
        
    def next_question(self):
        current_question = self.question_list[self.number_of_question]
        self.number_of_question += 1
        users_answer = self.validate_input(f"Q.{self.number_of_question} {current_question.text} (t)rue / f(alse)? ",['t','f'])
        self.check_answer(users_answer, current_question.answer)
        
        
    def check_answer(self, users_answer, right_answer):
        if users_answer.lower() == right_answer.lower()[0]:
            print("You are right")
            self.score += 1
        else:
            print(f"You're wrong, right answer is {right_answer}")
        print(f"Your current score is {self.score}/{self.number_of_question}")
        print("\n")

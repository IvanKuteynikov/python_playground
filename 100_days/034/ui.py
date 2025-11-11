import tkinter as tk
THEME_COLOR = "#375362"

class QuizUI:

    def __init__(self, quiz):
        self.score = 0
        self.end_quiz = False
        self.mark = ''
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: {self.score}", fg="white", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.check_mark_label = tk.Label(font=("Arial", 14, 'bold'), fg="white", background=THEME_COLOR)
        self.check_mark_label.grid(row=3, column=0, columnspan=2)


        self.window.mainloop()


    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        if q_text == "Thanks, no more questions.":
            final_score = f'Your score is {self.score}/10'
            self.canvas.itemconfig(self.question_text, text=final_score)
            self.false_button.grid_forget()
            self.true_button.grid_forget()
            self.restart_button = tk.Button(text="Restart", highlightthickness=0, command=self.restart_game, font=("Arial", 30, 'bold'))
            self.restart_button.grid(row=2, column=0, columnspan=2)

            self.end_quiz = True
        else:
            self.canvas.itemconfig(self.question_text, text=q_text)

    def restart_game(self):
        self.score = 0
        self.end_quiz = False
        self.mark = ""

        self.quiz.reset()

        self.score_label.config(text=f"Score: {self.score}")
        self.check_mark_label.config(text=self.mark)

        self.restart_button.grid_forget()

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

    def give_feedback(self, is_correct):
        if self.end_quiz:
            pass
        else:
            if is_correct:
                self.score += 1
                self.mark += "✅"
                self.score_label.config(text=f"Score: {self.score}")
                self.canvas.config(bg="green")
            else:
                self.mark += "⛔"
                self.canvas.config(bg="red")
            self.check_mark_label.config(text=self.mark)
            self.window.after(1000, self.get_next_question)

    def check_answer_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def check_answer_false(self):
        is_correct = self.quiz.check_answer("False")
        print(is_correct)
        self.give_feedback(is_correct)
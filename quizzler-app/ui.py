from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
Q_FONT = ("arial", 20, "italic")
SCORE_FONT = ("arial", 12, "bold")
INFO_FONT = ("arial", 10, "bold")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Labels
        self.score_label = Label(text=f"Score: 0/{len(self.quiz.question_list)}",
                                 font=SCORE_FONT,
                                 bg=THEME_COLOR,
                                 fg="white"
                                 )
        self.score_label.grid(column=1, row=0)
        self.info_label = Label(text="Info: ", font=INFO_FONT, bg=THEME_COLOR, fg="white", width=25)
        self.info_label.grid(column=0, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=Q_FONT)
        self.canvas.grid(column=0, row=2, columnspan=2, pady=(30, 30))

        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=3, column=1, padx=(0, 50))
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=3, column=0, padx=(0, 0))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            category = self.quiz.current_question.category.split(":")[-1]
            self.info_label.config(text=f"{category} : {self.quiz.current_question.difficulty.title()}")
        else:
            # Reach the end
            self.canvas.itemconfig(self.question_text,
                                   text=f"Finished with score {self.quiz.score}/{self.quiz.question_number}")
            self.info_label.config(text="Congratulations!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, user_answer: bool):
        if user_answer:
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


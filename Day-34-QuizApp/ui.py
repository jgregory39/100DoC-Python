from tkinter import *
from tkinter.ttk import Combobox
from quiz_brain import QuizBrain
import data

THEME_COLOR = "#375362"
FONT = ('Arial', 12)


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20, borderwidth=0)

        # Category Menu
        self.category = StringVar()
        category_lbl = Label(text='Category:', font=FONT, bg=THEME_COLOR, fg='White')
        category_lbl.grid(row=0, column=0)

        cat_list = data.get_categories()
        cat_list.insert(0, 'Any')
        self.category_box = Combobox(textvariable=self.category, state='readonly', values=cat_list, font=FONT)
        self.category_box.current(0)
        self.category_box.grid(row=1, column=0)
        self.category_box.bind('<<ComboboxSelected>>', func=self.new_questions)

        # Difficulty Menu
        self.difficulty = StringVar()
        diff_lbl = Label(text='Difficulty:', font=FONT, bg=THEME_COLOR, fg='White')
        diff_lbl.grid(row=0, column=1)

        diff_options = ('Any', 'Easy', 'Medium', 'Hard')
        self.diff_box = Combobox(textvariable=self.difficulty, state='readonly', values=diff_options, font=FONT)
        self.diff_box.current(0)
        self.diff_box.grid(row=1, column=1)
        self.diff_box.bind('<<ComboboxSelected>>', func=self.new_questions)

        # Score Label
        self.score_lbl = Label(text='Score: 0', font=FONT, bg=THEME_COLOR, fg='White', pady=5)
        self.score_lbl.grid(row=2, column=1)

        self.canvas = Canvas(width=300, height=250, borderwidth=0)
        self.q_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=('Arial', 20, 'italic'),
            anchor=CENTER,
            fill=THEME_COLOR)
        self.canvas.grid(row=3, column=0, rowspan=2, columnspan=2, pady=50)

        # Yes/No Buttons
        self.yes_img = PhotoImage(file='images/true.png')
        self.yes_button = Button(image=self.yes_img, bg=THEME_COLOR, highlightthickness=0, command=self.check_true)
        self.yes_button.grid(row=5, column=0)

        self.no_img = PhotoImage(file='images/false.png')
        self.no_button = Button(image=self.no_img, bg=THEME_COLOR, highlightthickness=0, command=self.check_false)
        self.no_button.grid(row=5, column=1)

        self.change_question()

        self.window.mainloop()

    def new_questions(self, x=None):
        diff = self.difficulty.get().lower() if not self.difficulty.get() == 'Any' else None
        cat_id = data.get_cat_id(self.category.get()) if not self.category.get() == 'Any' else None
        self.quiz.set_questions(diff, cat_id)

    def change_question(self):
        new_q = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=new_q)
        self.canvas.config(bg='white')
        self.canvas.update()
        self.score_lbl.config(text=f"Score: {self.quiz.score}")

    def check_true(self):
        if self.quiz.isFinished:
            self.quiz.reset()
            self.new_questions()
            self.change_question()
            return
        if self.quiz.check_answer('True'):
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, func=self.change_question)

    def check_false(self):
        if self.quiz.isFinished:
            self.window.destroy()
        if self.quiz.check_answer('False'):
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, func=self.change_question)



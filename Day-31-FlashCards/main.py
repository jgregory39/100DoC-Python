from tkinter import *
import pandas
import random
import messagebox
import os

BACKGROUND_COLOR = "#B1DDC6"
timer = None


# -------DATA------ #
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
words_list = [word for word in data.French.array]
active_word = random.choice(words_list)


def update_words_to_learn():
    learn_data = data[data.French.isin(words_list)]
    learn_data.to_csv('data/words_to_learn.csv', index=False)


def get_translation(fr_word):
    en_data = data[data.French == fr_word]
    en_word = en_data.English.values[0]
    return en_word


# ------Card------- #
def flip_card():
    fr_word = active_word
    en_word = get_translation(fr_word)
    canvas.itemconfig(word_text, text=en_word, fill='white')
    canvas.itemconfig(lang_text, text='English', fill='white')
    canvas.itemconfig(card_item, image=back_img)


def new_card():
    global active_word
    if words_list:
        active_word = random.choice(words_list)
    else:
        messagebox.showinfo(title='Congratulations', message='You have completed all words in this list!\n'
                                                             'This list will reset!')
        os.remove('data/words_to_learn.csv')
        exit()
    canvas.itemconfig(word_text, text=active_word, fill='black')
    canvas.itemconfig(lang_text, text='French', fill='black')
    canvas.itemconfig(card_item, image=front_img)

    global timer
    timer = screen.after(3000, func=flip_card)


# -----Buttons----- #
def correct():
    screen.after_cancel(timer)
    words_list.remove(active_word)
    new_card()


def incorrect():
    screen.after_cancel(timer)
    new_card()


# --------UI------- #
screen = Tk()
screen.title('Flashy')
screen.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Image Declarations
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

# Card Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_item = canvas.create_image(400, 263, image=front_img)

lang_text = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'), fill='black')
word_text = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=correct)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=incorrect)
wrong_button.grid(column=0, row=1)

new_card()

screen.mainloop()

update_words_to_learn()

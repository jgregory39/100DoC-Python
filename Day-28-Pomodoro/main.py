from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    title_lbl.config(text="Timer", fg=GREEN)
    check_lbl.config(text='')
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_lbl.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_lbl.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        title_lbl.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = int(count / 60)
    sec = count % 60
    if min < 10:
        min = f"0{min}"
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        works = int(reps/2)
        checks = '✔' * works
        check_lbl.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2,row=2)

title_lbl = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
title_lbl.grid(column=2, row=1)

check_lbl = Label(font=(FONT_NAME, 24, 'bold'), fg=GREEN, bg=YELLOW)
check_lbl.grid(column=2, row=4)

start_btn = Button(text='Start', font=(FONT_NAME, 14), bg=PINK, highlightthickness=0, command=start_timer)
start_btn.grid(column=1, row=3)

reset_btn = Button(text='Reset', font=(FONT_NAME, 14), bg=PINK, highlightthickness=0, command=reset_timer)
reset_btn.grid(column=3, row=3)

window.mainloop()
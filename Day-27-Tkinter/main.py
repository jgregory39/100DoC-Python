from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width=500, height = 300)
def button_clicked():
    text = input.get()
    my_label.config(text=text)


#Label
my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#New Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry()
input.grid(column=3,row=2,pady=5)

window.mainloop()
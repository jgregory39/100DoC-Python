from tkinter import *
FONT = ('Arial', 16)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=335, height=150)
window.config(padx=5, pady=30)


def calculate():
    try:
        miles = getdouble(miles_entry.get())
    except:
        print('INVALID INPUT')
        return
    km = miles * 1.6
    result_label.config(text=km)

#Miles entry
miles_entry = Entry(width=10, font=FONT)
miles_entry.insert(END,0)
miles_entry.grid(column=1, row=0, padx=2, pady=5)

#Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0, pady=5)

equal_to_label = Label(text='is equal to', font=FONT)
equal_to_label.grid(column=0, row=1, padx=10, pady=5)

unit_label = Label(text='Km', font=FONT)
unit_label.grid(column=2, row=1, pady=5, padx=10)

#Result Label
result_label = Label(text=0.0,font=FONT)
result_label.grid(column=1, row=1)

#Button
calc_button = Button(text='Calculate', command=calculate, font=FONT)
calc_button.grid(column=1, row=2)


window.mainloop()
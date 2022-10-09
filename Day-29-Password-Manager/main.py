from tkinter import *
from tkinter import messagebox
from password_generator import make_password
import pyperclip

FONT_NAME = 'Arial'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = make_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    site = site_entry.get()
    user = user_entry.get()
    pwd = password_entry.get()

    if site == "" or user == "" or pwd == "":
        messagebox.showinfo(title='INVALID', message='Please do not leave any blank entries!')
        return

    # Confirm Details
    if messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail/Username: {user} \n"
                                                  f"Password: {pwd} \nIs it ok to save?"):
        password_data = f"{site} | {user} | {pwd}\n"
        with open("data.txt", mode='a') as file:
            file.write(password_data)

        site_entry.delete(0, END)
        user_entry.delete(0, END)
        user_entry.insert(0, "example@email.com")
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(width=110, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(55, 95, image=logo_img)
canvas.grid(column=2, row=1)

# Labels
site_label = Label(text='Website:', font=(FONT_NAME, 12))
site_label.grid(column=1, row=2)
user_label = Label(text='Email/Username:', font=(FONT_NAME, 12))
user_label.grid(column=1, row=3)
password_label = Label(text='Password:', font=(FONT_NAME, 12))
password_label.grid(column=1, row=4)

# Input boxes
site_entry = Entry(width=41)
site_entry.grid(column=2, row=2, columnspan=2, sticky='w')
site_entry.focus()

user_entry = Entry(width=41)
user_entry.grid(column=2, row=3, columnspan=2, sticky='w')
user_entry.insert(0, "example@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=2, row=4, sticky='w')

# Buttons
generate_pwd_button = Button(text='Generate Password', font=(FONT_NAME, 9), command=generate_password)
generate_pwd_button.grid(column=3, row=4, sticky='w')
add_button = Button(text='Add', width=35, font=(FONT_NAME, 9), command=save_password)
add_button.grid(column=2, row=5, columnspan=2, sticky='w')

window.mainloop()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = 'Arial'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def make_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password


def set_password():
    password = make_password()
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SEARCH LOGINS ------------------------------- #


def search():
    website = site_entry.get().title()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Failed", message="No data file present.")
    else:
        if website in data:
            password = data[website]['password']
            messagebox.showinfo(title="Login Found!", message=f"Password for {website} is: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Failed", message=f"No password found for {website}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = site_entry.get().title()
    email = user_entry.get()
    pwd = password_entry.get()

    if website == "" or email == "" or pwd == "":
        messagebox.showinfo(title='INVALID', message='Please do not leave any blank entries!')
        return

    # Create login dictionary
    login_data = {
        website: {
            'email': email,
            'password': pwd
        }
    }

    # Attempt to load and update json file to 'data' variable
    try:
        with open("data.json", mode='r') as file:
            data = json.load(file)
            data.update(login_data)
    # Catch exception and manually create 'data' variable from login dict
    except FileNotFoundError:
        data = login_data
    # Write 'data' variable to json file
    finally:
        with open('data.json', mode='w') as file:
            json.dump(data, file, indent=4)

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
site_entry = Entry(width=21)
site_entry.grid(column=2, row=2, sticky='w')
site_entry.focus()

user_entry = Entry(width=41)
user_entry.grid(column=2, row=3, columnspan=2, sticky='w')
user_entry.insert(0, "example@email.com")

password_entry = Entry(width=21)
password_entry.grid(column=2, row=4, sticky='w')

# Buttons
generate_pwd_button = Button(text='Generate Password', font=(FONT_NAME, 9), command=set_password)
generate_pwd_button.grid(column=3, row=4, sticky='w')

search_button = Button(text='Search', font=(FONT_NAME, 9), width=16, command=search)
search_button.grid(column=3, row=2, sticky='w')

add_button = Button(text='Add', width=35, font=(FONT_NAME, 9), command=save_password)
add_button.grid(column=2, row=5, columnspan=2, sticky='w')

window.mainloop()

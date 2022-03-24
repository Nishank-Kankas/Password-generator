from random import choice, randint, shuffle
from tkinter import messagebox
from tkinter import *
import pyperclip
import json

CharCount = (8, 10)
symbCount = (2, 3)
intCount = (2, 4)

def password_gen():
    # possible letter, num and symbole
    letters = [chr(c) for c in range(ord('a'), ord('z')+1)] + [chr(c) for c in range(ord('A'), ord('Z')+1)]
    numbers = [str(i) for i in range(10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # generate pass
    chars = [choice(letters) for _ in range(randint(CharCount[0], CharCount[1]))]
    symb = [choice(symbols) for _ in range(randint(symbCount[0], symbCount[1]))]
    num = [choice(numbers) for _ in range(randint(intCount[0], intCount[1]))]
    password_list = chars + symb + num
    shuffle(password_list)

    # list to str
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not password:
        messagebox.showinfo(title="ERROR", message="Fields are empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# GUI
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)


# adding photo
canvas = Canvas(height=225, width=225)
img = PhotoImage(file="lock.png")
canvas.create_image(112, 112, image=img)
canvas.grid(row=0, column=1)


# lables
website_label = Label(text="site:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "placeholder@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_gen)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
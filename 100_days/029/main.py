import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import json

WHITE = "#ffffff"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    character_pool = []
    character_pool.extend(string.ascii_letters)
    character_pool.extend(string.digits)
    character_pool.extend(string.punctuation)
    password_list = [random.choice(character_pool) for _ in range(12)]
    random.shuffle(password_list)
    final_password = "".join(password_list)
    if len(input_pass.get()) > 0:
        input_pass.delete(0, tk.END)
        input_pass.insert(0, final_password)
        pyperclip.copy(final_password)
    else:
        input_pass.insert(0, final_password)
        pyperclip.copy(final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def read_json(filename, new_data):
    with open(filename, 'r') as file:
        data = json.load(file)  # read
    data.update(new_data)  # add new
    print(data)
    return data

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)  # save with the new data to the file
    input_website.delete(0, tk.END)
    input_pass.delete(0, tk.END)

def save():
    website = input_website.get()
    user = input_user.get()
    password = input_pass.get()
    new_data = {website:
        {
            "email":user,
            "password":password
        }
    }
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields")
    else:
        try:
            data = read_json('data.json', new_data)
            save_json('data.json', data)
        except FileNotFoundError:
            save_json('data.json', new_data)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message=f"No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f'Info for website: {website}', message=f'email: {email}\npassword: {password}')
        else:
            messagebox.showerror(title="Error", message=f"No such website: {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
padlock_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

lb_website = tk.Label(text="URL:", font=(FONT_NAME, 14, 'bold'))
lb_website.grid(column=0, row=1)


lb_user = tk.Label(text="Email/User:", font=(FONT_NAME, 14, 'bold'))
lb_user.grid(column=0, row=2)


lb_password = tk.Label(text="Password", font=(FONT_NAME, 14, 'bold'))
lb_password.grid(column=0, row=3)

input_website = tk.Entry(width=20)
input_website.grid(column=1, row=1, columnspan=1)
input_website.focus()

input_user = tk.Entry(width=35)
input_user.grid(column=1, row=2, columnspan=2)
input_user.insert(0,'myrandomemail@email.com')

input_pass = tk.Entry(width=18)
input_pass.grid(column=1, row=3)

button_generate = tk.Button(text="Generate", highlightthickness=0, command=generate, width=13)
button_generate.grid(column=2, row=3)

button_save = tk.Button(text="Save", highlightthickness=0, command=save, width=32)
button_save.grid(column=1, row=4, columnspan=2)

button_search = tk.Button(text="Search", highlightthickness=0, command=find_password, width=13)
button_search.grid(column=2, row=1, columnspan=1)


window.mainloop()
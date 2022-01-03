from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from cryptography.fernet import Fernet


KEY = b'2C5oRGmK2SCjXU_4v6g8iBRlZ6ySOac7jrqXLGkCA10='


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    f = Fernet(KEY)
    token = f.encrypt(password.encode('utf-8')).decode('utf-8')
    new_data = {
        website: {
            "email": email,
            "password": token,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file_r:
                data = json.load(data_file_r)
        except FileNotFoundError:
            with open("data.json", "w") as data_file_w:
                json.dump(new_data, data_file_w, indent=4)
        except json.JSONDecodeError:
            with open("data.json", "w") as data_file_w:
                json.dump(new_data, data_file_w, indent=4)
        else:
            # Update the existing file with the new site/pass
            data.update(new_data)
            with open("data.json", "w") as data_file_w:
                json.dump(data, data_file_w, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    ws = website_entry.get().title()
    if len(ws) != 0:
        try:
            with open("data.json", "r") as data_file_r:
                data = json.load(data_file_r)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="File data.json was not yet created")
        except json.JSONDecodeError:
            messagebox.showinfo(title="Oops", message="File data.json it's corrupted")
        else:
            if ws in data:
                # Clean up
                password_entry.delete(0, END)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                # Fill in the values
                website_entry.insert(0, ws.title())
                email_entry.insert(0, data[ws]['email'])
                # Decrypt the password
                f = Fernet(KEY)
                token = data[ws]['password'].encode('utf-8')
                password = f.decrypt(token)
                password_entry.insert(0, password.decode("utf-8"))
            else:
                website_entry.delete(0, END)
                messagebox.showinfo(title="Oops", message=f"No entry for {ws}")


# ---------------------------- SHOW PASSWORD ------------------------------- #
def show_password():
    if pass_check_value.get() == 0:
        # Unchecked
        password_entry.config(show="*")
        # pass_check_box.config(text="Show password")
    else:
        # Checked
        password_entry.config(show="")
        # pass_check_box.config(text="Hide password ")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "razvan@gmail.com")
password_entry = Entry(width=34, show="*")
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=15, padx=0, pady=2, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", padx=0, pady=5, width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, padx=0, pady=2, command=find_password)
search_button.grid(row=1, column=2)

# Checkbox
pass_check_value = IntVar()
pass_check_box = Checkbutton(window, padx=10, variable=pass_check_value, command=show_password)
pass_check_box.grid(row=3, column=3)


window.mainloop()

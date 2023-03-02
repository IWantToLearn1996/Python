from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def gen_pas_but():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    #nr_numbers = random.randint(2, 4)

    password_letters = [ random.choice(letters) for letter in range(nr_letters)]

    password_symbols = [ random.choice(symbols) for symbol in range(nr_symbols)]

    password_numbers = [ random.choice(numbers) for number in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)

    #print(f"Your password is: {password}")

# -------------------------------- SEARCH ---------------------------------- #
def search_but():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        search_message_error = messagebox.showerror(title="Error 404", message="No Data File")
    else:
        if website in data:
            search_message = messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error 404", message=f"Website '{website}' does not exist")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_but():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }

    if len(website) == 0 or len(password) == 0:
        empty = messagebox.showerror(title="Error 404", message="Empty Website or Password")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Writing data to JSON file as a Dictionary, "w"
                # json.dump(new_data, data_file, indent=4)

                # Reading data from JSON file, "r"
                data = json.load(data_file)
                # print(data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update data on JSON file without overwriting it or appending, "r"
            data.update(new_data)

            # Saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            # email_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50, bg= "White")


canvas = Canvas(width=200, height=200, bg= "White", highlightthickness=0)
mypass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:", bg="White")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg="White")
email_label.grid(column=0, row=2)


password_label = Label(text="Password:", bg="White")
password_label.grid(column=0, row=3)


website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan= 2)
email_input.insert(0, "nikosmardas96@gmail.com")

password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=1)


generate_button = Button(text="Generate Password", width=15, command= gen_pas_but)
generate_button.grid(column=3, row=3, columnspan=1, padx=8)

search_button = Button(text="Search", width=15, command= search_but)
search_button.grid(column=3, row=1, columnspan=1, padx=8)

add_button = Button(width=30, text="Add", command= add_but)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
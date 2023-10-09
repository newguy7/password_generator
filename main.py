from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# --------------------------- PASSWORD GENERATOR ----------------------- #

def generate_password():  

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10)) ]
    password_list += [choice(symbols) for char in range(randint(2, 4)) ]
    password_list += [choice(numbers) for char in range(randint(2, 4)) ]   

    shuffle(password_list)

    password = "".join(password_list) 
    
    password_entry.insert(0, password)
    #to copy on clipboard
    pyperclip.copy(password)


# -------------- SAVE THE PASSWORD ------------------------------------- #
def add():

    website = website_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    # Check if Website entry is empty:
    if len(website) == 0 or len(username) == 0 or len(password) == 0:        
        messagebox.showwarning(title="OOPS", message="Please don't leave any fields empty!")

    else:
        # verify before saving the passwords
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{username}"
                            f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:        
                file.write(" | ".join([website, username, password]) + "\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()


# --------------------------- UI SETUP --------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

# create canvas
canvas = Canvas(width=200, height=200)
# add image to canvas
img_file=PhotoImage(file="logo.png")
#create_image(x,y,image)
canvas.create_image(100,100,image=img_file)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
# sets the cursor on website entry
website_entry.focus()

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=add)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()


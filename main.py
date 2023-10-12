from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json

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
    email = user_entry.get()
    password = password_entry.get()

    #Create a dictionary to save the user's data
    new_data = {
        website: {
            "email": email,
            "password" : password
        }
    }

    # Check if Website entry is empty:
    if len(website) == 0 or len(email) == 0 or len(password) == 0:        
        messagebox.showwarning(title="OOPS", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as file: 
                #Reading old data
                data = json.load(file)
                
        except FileNotFoundError:
            with open("data.json", "w") as file: 
                #writing the data
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file: 
                #Saving updated data
                json.dump(data, file, indent=4) 
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()

#---------------------------- SEARCH ----------------------------------- #
def search_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as file: 
            #Reading old data
            data = json.load(file)          
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="File Not Found")    
    else:
        if website in data:            
            email = data[website]['email']
            password = data[website]['password']
            print(data)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"Details for {website} not found")

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

website_entry = Entry(width=17)
website_entry.grid(column=1, row=1)
# sets the cursor on website entry
website_entry.focus()

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=add)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search",width=13, command=search_password)
search_button.grid(column=2, row=1)



window.mainloop()


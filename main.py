from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json


def generatorPassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0,"end")
    password_input.insert(0,string=password)
    pyperclip.copy(password)


def savePassword():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    
    if len(website)==0 or len(email)==0 or len(password)==0 :
        messagebox.showinfo(title="Oops",message="Don't leave any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"""These are the details entered: :
                                   \n Email : {email} \n Password : {password} """)
        new_data ={
            website :{
                "Email" : email,
                "Password" : password
            }
        }
        
        if is_ok:
            try:
                with open("mypasswords.json",mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("mypasswords.json",mode="w") as data_file:
                    json.dump(new_data, data_file,indent=4)
            else:
                data.update(new_data)
                with open("mypasswords.json",mode="w") as data_file:
                    json.dump(data, data_file,indent=4)

            finally:
                website_input.delete(0,"end")
                email_input.delete(0,"end")
                password_input.delete(0,"end")
                website_input.focus()

    
def findPassword():
    website = website_input.get()

    if not website:
        messagebox.showerror(title="Error", message="Please enter a website name.")
    else:
        try:
            with open("mypasswords.json",mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Password file not found!")
            website_input.delete(0,"end")
        except json.JSONDecodeError:
            messagebox.showerror(title="Error", message="Password file is empty or corrupted!")
            website_input.delete(0,"end")
        else:
            if website in data:
                email_used = data[website]["Email"]
                password_used = data[website]["Password"]
                messagebox.showinfo(title=website, message=f"Email: {email_used}\nPassword: {password_used}")
            else:
                messagebox.showerror(title="Error", message=f"No details found for {website}.")


window = Tk()
window.title("PassWord Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website :")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username :")
email_label.grid(column=0,row=2)

password_label = Label(text="Password :")
password_label.grid(column=0,row=3)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2, sticky="w")

email_input = Entry(width=35)
email_input.grid(column=1,row=2, columnspan=2, sticky="w")

password_input = Entry(width=35)
password_input.grid(column=1,row=3, columnspan=2, sticky="w")

generate_button = Button(text="Generate Password", width=15, command=generatorPassword)
generate_button.grid(column=3,row=2)

add_button = Button(text="Add",width=30,command=savePassword)
add_button.grid(column=1,row=5,columnspan=2, sticky="w")

search_button = Button(text="Search", width=15, command=findPassword)
search_button.grid(column=3,row=1)


window.mainloop()
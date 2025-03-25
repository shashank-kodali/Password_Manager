from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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

    password_input.insert(0,string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    
    if len(website)==0 or len(email)==0 or len(password)==0 :
        messagebox.showinfo(title="Oops",message="Don't leave any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"""This are the details entered :
                                   \n Email : {email} \n Password : {password} """)
        
        if is_ok:
            with open("mypassword.txt",mode="a") as data:
                data.write(f"{website} || {email} || {password}\n")
                website_input.delete(0,"end")
                email_input.delete(0,"end")
                password_input.delete(0,"end")
                website_input.focus()

    

    
# ---------------------------- UI SETUP ------------------------------- #
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
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=35)
email_input.grid(column=1,row=2, columnspan=2)

password_input = Entry(width=35)
password_input.grid(column=1,row=3, columnspan=2)

generate_button = Button(text="Generate Password",width=30, command=generatorPassword)
generate_button.grid(column=1,row=4,columnspan=2)

add_button = Button(text="Add",width=30,command=savePassword)
add_button.grid(column=1,row=5,columnspan=2)


window.mainloop()
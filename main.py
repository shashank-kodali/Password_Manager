from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    website_input.delete(0,"end")
    email_input.delete(0,"end")
    password_input.delete(0,"end")

    website_input.focus()

    with open("mypassword.txt",mode="a") as data:
        data.write(f"{website} || {email} || {password}\n")
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

generate_button = Button(text="Generate Password",width=30)
generate_button.grid(column=1,row=4,columnspan=2)

add_button = Button(text="Add",width=30,command=savePassword)
add_button.grid(column=1,row=5,columnspan=2)


window.mainloop()
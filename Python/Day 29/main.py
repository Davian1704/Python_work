# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")


canvas = Canvas(width=200,height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=2,row=1)
window.config(padx=20,pady=20)

website_text=Label(text="Website:")
website_text.grid(row=2,column=1)

website_field=Text(width=35,height=1)
website_field.grid(row=2,column=2,columnspan=2)

email_text=Label(text="Email/Username:")
email_text.grid(row=3,column=1)

email_field=Text(width=35,height=1)
email_field.grid(row=3,column=2,columnspan=2)

password_text=Label(text="Password: ")
password_text.grid(row=4,column=1)

password_field=Text(width=21,height=1)
password_field.grid(row=4,column=2)

password_generate=Button(text="Generate Password")
password_generate.grid(row=4,column=3)

add_button=Button(text="Add",width=36)
add_button.grid(row=5,column=2,columnspan=2)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()
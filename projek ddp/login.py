import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import subprocess

def login():
    username = "admin"
    password = "123"
    entered_username = Entry1.get() 
    entered_password = Entry2.get()  
    if entered_username == username and entered_password == password:
        messagebox.showinfo(title="Login Success", message="You Successfully Logged in")
        open_main_menu()

    else:
        messagebox.showerror(title="Error", message="Invalid Login")

def open_main_menu():
    subprocess.run(["weather1.py"], check=True)


root = ttk.Window(themename="solar")

root.title("Login - System Management Data Students")
root.geometry('600x300')
root.resizable(False,False)

Label1 = ttk.Label (root, text="Login - System", font=("Halvetica", 20), bootstyle=DANGER).place(x=200, y=30)

Label2 = ttk.Label (root, text="Username :",  bootstyle=SUCCESS).place(x=170, y=100)
Entry1 = ttk.Entry (root, show='',  bootstyle=SUCCESS)
Entry1.place(x=270, y=100)

Label3 = ttk.Label (root, text="Password :",  bootstyle=SUCCESS).place(x=170, y=150)
Entry2 = ttk.Entry (root, show='*',  bootstyle=SUCCESS)
Entry2.place(x=270, y=150)

button1 = ttk.Button(root, text="Login", bootstyle=SUCCESS, command=login)
button1.place(x=260, y=200)
root.mainloop()
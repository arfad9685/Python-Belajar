#Create login system with background image in tkinter

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
root = Tk()
root.title("Login System")
root.resizable(0,0)
bg = Image.open('loginbg1.png')
bg.thumbnail((700, 700))
width, height = bg.size
bg = ImageTk.PhotoImage(bg)
def new():
    if user_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Username")
    elif password_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Password")
    elif user_entry.get()=="" and password_entry.get()=="":
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    elif user_entry.get()=="admin" and password_entry.get()=="admin123":
        root.withdraw()
        paswd.set("")
        new_window = Toplevel(root)
        def home_page():
            new_window.withdraw()
            root.deiconify()
            
        home = Button(new_window, text="Go to Login page", font=("Ariel 22 bold"), relief=GROOVE, bd=2, command=home_page)
        home.pack(padx=30, pady=30)
    else:
        messagebox.showinfo("Login System", "Please enter the correct Username and Password")
        
        
canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
label = Label(root, text="Login Page", font=("Ariel 25 bold"), bg='#5500FF', fg='white')
canvas.create_window(260, 40, anchor="nw", window=label)
user_label = Label(root, text="User name:", font=("Ariel 18 bold"),bg='#5500FF',fg='white')
canvas.create_window(140, 130, anchor="nw", window=user_label)
password_label = Label(root, text="Password:", font=("Ariel 18 bold"),bg='#5500FF',fg='white')
canvas.create_window(140, 210, anchor="nw", window=password_label)
user_entry = Entry(root, font=("Ariel 18 bold"))
user_entry.focus()
canvas.create_window(290, 130, anchor="nw", window=user_entry)
paswd=StringVar()
password_entry = Entry(root, textvar=paswd, font=("Ariel 18 bold"), show="*")
canvas.create_window(290, 210, anchor="nw", window=password_entry)
login = Button(root, text="Log In", font=("Ariel 22 bold"),
               width=8, bg="blue", fg='#FFC331', relief=FLAT, command=new)
canvas.create_window(270, 290, anchor="nw", window=login)
root.mainloop()
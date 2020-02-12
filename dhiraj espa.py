from tkinter import *
from tkinter import messagebox

wn=Tk()
wn.geometry("300x250")
wn.title("Registration Form")
Label(text="choose Login or Register",bg="white",width="300",height="2",font="Calibri").pack()

def login():
	login_screen=Toplevel(wn)
	login_screen.title("Login")
	login_screen.geometry("300x250")
	username=str()
	password=str()
	Label(login_screen).pack()
	Label(login_screen,text="").pack()
	username_label=Label(login_screen,text="username")
	username_label.pack()

	username_entry = Entry(login_screen, textvariable=username)
	username_entry.pack()

	password_lable = Label(login_screen, text="Password * ")
	password_lable.pack()

	password_entry = Entry(login_screen, textvariable=password, show='*')
	password_entry.pack()

	Label(login_screen, text="").pack()
	Button(login_screen, text="Login", width=10, height=1).pack()


global Registration_Form
Button(text="Login", height="2", width="30", command=login).pack()


def register():
	register_screen=Toplevel(wn)
	register_screen.title("Register")
	register_screen.geometry("300x250")
	username = StringVar()
	password = StringVar()

	Label(register_screen, text="Please enter details below",bg="white").pack()
	Label(register_screen, text="").pack()

	username_lable = Label(register_screen, text="Username * ").pack()

	username_entry = Entry(register_screen, textvariable=username)
	username_entry.pack()

	password_lable = Label(register_screen, text="Password * ")
	password_lable.pack()

	password_entry = Entry(register_screen, textvariable=password, show='*')
	password_entry.pack()

	Label(register_screen, text="").pack()
	Button(register_screen,text="Register",width=10,height=1).pack()

	a = username_entry.get()
	b= password_entry.get()
	file = open('roy.txt', 'w')
	file.write(a)
	file.write(b)
	file.close()

global Registration_Form
Button(text="Register", height="2", width="30", command=register).pack()

wn.mainloop()
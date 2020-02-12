from tkinter import *
import pickle

def main_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Button(text="Login", height="2", width="30", command=login).pack(padx=10, pady=10)

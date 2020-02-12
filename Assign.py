from tkinter import *
from tkinter import messagebox
import pickle

def main_display():
    global rr
    rr = Tk()
    rr.title("Ola Form")
    rr.geometry("200x200")
    lbl=Label(rr,text="HOLA REGISTER FORM",fg='green',font="Ariel").pack()

    btn1 = Button(text="Register", fg="green", bg="orange", font="Ariel", command=register)
    btn1.pack(padx=10, pady=10)

    btn2 = Button(text="Log-in", fg="green", bg="orange", font="Ariel", command=login)
    btn2.pack(padx=10, pady=10)
    rr.mainloop()

def register():
    global bp
    bp=Tk()

    bp.title("Ola Registration Form")

    bp.geometry("500x700")

    lbl1 = Label(bp, text="Name", fg="blue").pack(padx=10, pady=10)
    global ent1

    ent1 = Entry(bp,fg='purple', bg='white', width=30).pack(padx=10, pady=10)
    ent1=StringVar

    lbl5 = Label(bp, text="Choose your gender", fg="blue").pack(padx=10, pady=10)

    rad1 = Radiobutton(bp, text="Male", value=1).pack(padx=10, pady=10)
    rad2 = Radiobutton(bp, text="Female", value=2).pack(padx=10, pady=10)
    rad3 = Radiobutton(bp, text="None", value=3).pack(padx=10, pady=10)

    lbl2 = Label(bp, text="Email", fg="blue").pack(padx=10, pady=10)
    global ent2

    ent2 = Entry(bp,fg='purple', bg='white', width=30).pack(padx=10, pady=10)
    ent2=StringVar

    lbl3 = Label(bp, text="Enter a Password", fg="blue").pack(padx=10, pady=10)
    global ent3

    ent3 = Entry(bp,fg='purple', bg='white', width=20).pack(padx=10, pady=10)
    ent3=StringVar

    lbl4 = Label(bp, text="Re-enter Password", fg="blue").pack(padx=10, pady=10)

    global ent4
    ent4 = Entry(bp,fg='purple', bg='white', width=20).pack(padx=10, pady=10)
    ent4=StringVar



    def getdata():

        global getdata
        a = ent1.get()
        b = ent2.get()
        c = ent3.get()
        d = ent4.get()

        if a == b == c == d == '':

            messagebox.showinfo("Empty inputs")
        else:

            global dicd
            dicd = {'name': a, 'email': b, 'password': c, "cpassword": d}

            if c == d:
                q = open('bobol.txt', 'wb')
                pickle.dump(dicd, q)
                q.close()
                messagebox.showinfo("Register Complete", 'Registered  successfully!')

            else:
                messagebox.showinfo("Password error", "Password doesn't match")

    btn_gd = Button(bp, text="SAVE", fg="green", bg="orange", font="Ariel", command=getdata)
    btn_gd.pack(padx=10, pady=10)



def login():
    global dc
    dc = Tk()
    dc.title('OLA Log-in Form')
    dc.geometry('333x444')

    wor1 = Label(dc, text='Enter your e-mail').pack(padx=10, pady=10)

    global err1
    err1 = Entry(dc, fg='black', bg='red', width=30).pack(padx=10, pady=10)

    wor2 = Label(dc, text='Enter your password').pack(padx=10, pady=10)

    global ery2
    ery2 = Entry(dc, bg='red', width=10).pack(padx=10, pady=10)






def login_entered():
    e = err1.get()
    f = ery2.get()
    global dict2
    dict2={"cemail":e, "compassword":f }


    r = open('bobol.txt','rb')
    dicd =pickle.load(r)


    if e in (dicd['password']) :
        messagebox.showinfo("LOGIN SUCCESS", 'Log-in successful!')
    else:
        messagebox.showinfo("WRONG PASSWORD OR EMAIL",'Concentrate when typing')

    btn_ln = Button(dc, text="Log-in", fg="green", bg="orange", font="Ariel", command=getdata)
    btn_ln.pack(padx=10, pady=10)



main_display()
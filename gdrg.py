from tkinter import *
from tkinter import messagebox
import pickle

bp=Tk()

bp.title("Ola Form")

bp.geometry("700x500")
lbl=Label(bp,text="HOLA REGISTER FORM",fg='green',font="Ariel")
lbl.pack(padx=10,pady=10)
lbl1=Label(bp,text="Name",fg="blue")
lbl1.pack(padx=10,pady=10)

name= StringVar()
ent1=Entry(fg='purple',bg='white',width=30,textvariable=name)
ent1.pack(padx=10,pady=10)

lbl5=Label(bp,text="Choose your gender",fg="blue")
lbl5.pack(padx=10,pady=10)

rad1=Radiobutton(bp,text="Male",value=1)
rad2=Radiobutton(bp,text="Female",value=2)
rad3=Radiobutton(bp,text="None",value=3)
rad1.pack(padx=10,pady=10)
rad2.pack(padx=10,pady=10)
rad3.pack(padx=10,pady=10)

lbl2=Label(bp,text="Email",fg="blue")
lbl2.pack(padx=10,pady=10)

ent2=Entry(fg='purple',bg='white',width=30)
ent2.pack(padx=10,pady=10)

lbl3=Label(bp,text="Enter a Password",fg="blue")
lbl3.pack(padx=10,pady=10)
ent3=Entry(fg='purple',bg='white',width=20)
ent3.pack(padx=10,pady=10)

lbl4=Label(bp,text="Re-enter Password",fg="blue")
lbl4.pack(padx=10,pady=10)

ent4=Entry(fg='purple',bg='white',width=20)
ent4.pack(padx=10,pady=10)

chk=BooleanVar()
chk.set(FALSE)

chkb=Checkbutton(bp,text="I am not robot",var=chk)
chkb.pack(padx=10,pady=10)

def data():
    a = ent1.get()
    b = ent2.get()
    c = ent3.get()
    d = ent4.get()
    uu=[a,b,c,d]
    q = open('bobol.txt', 'wb')
    pickle.dump(uu, q)
    q.close()

    if c == d:

        messagebox.showinfo("WELCOME TO OLA SANSAR","You've registered successfully!")
        dc = Tk()
        dc.title('OLA Log-in Form')
        dc.geometry('333x444')
        wor1 = Label(dc,text='Enter your e-mail')
        wor1.pack(padx=10,pady=10)

        err1 = Entry(dc,fg='black',bg='red',width=30)
        err1.pack(padx=10,pady=10)

        wor2 = Label(dc, text='Enter your password')
        wor2.pack(padx=10,pady=10)

        ery2 = Entry(dc,bg='red',width=10)
        ery2.pack(padx=10,pady=10)



        def gg():
            e = err1.get()
            f = ery2.get()

            q = open('olaa.pkl', 'rb')
            v=pickle.load(q)


            if e in v:

                messagebox.showinfo("LOGIN SUCCESS",'You are a part of ola now')
                lbn=Label(text=b)
                lbn.pack()

            else:
                messagebox.showinfo("WRONG PASSWORD OR EMAIL",'Concentrate when typing')
        bttn1 =Button(dc,text="Log-in",fg="green",bg="orange",font="Ariel",command=gg)
        bttn1.pack(padx=10, pady=10)
    else:
        messagebox.showinfo("Password Incorrect", "Re enter your password")

btn1=Button(text="Register",fg="green",bg="orange",font="Ariel",command=data)
btn1.pack(padx=10,pady=10)

bp.mainloop()
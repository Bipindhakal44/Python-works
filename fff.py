
from tkinter import *
from tkinter import messagebox

bp=Tk()

bp.title("Ola Form")

bp.geometry("700x500")

lbl1=Label(bp,text="Name",fg="blue",bg="red")
lbl1.grid(row=5,column=0)

ent1=Entry(fg='purple',bg='white',width=30)
ent1.grid(row=5,column=2)

lbl5=Label(bp,text="Choose your gender",fg="blue",bg="red")
lbl5.grid(row=10,column=0)

rad1=Radiobutton(bp,text="Male",value=7)
rad2=Radiobutton(bp,text="Female",value=9)
rad3=Radiobutton(bp,text="Chhaka",value=10)
rad1.grid(row=10,column=1)
rad2.grid(row=10,column=2)
rad3.grid(row=10,column=3)

lbl2=Label(bp,text="Email",fg="blue",bg="red")
lbl2.grid(row=15,column=0)

ent2=Entry(fg='purple',bg='white',width=30)
ent2.grid(row=15,column=1)

lbl3=Label(bp,text="Password",fg="blue",bg="red")
lbl3.grid(row=20,column=0)

ent3=Entry(fg='purple',bg='white',width=20)
ent3.grid(row=20,column=1)

lbl4=Label(bp,text="Re-type Password",fg="blue",bg="red")
lbl4.grid(row=25,column=0)

ent4=Entry(fg='purple',bg='white',width=20)
ent4.grid(row=25,column=1)

chk=BooleanVar()
chk.set(FALSE)
chkb=Checkbutton(bp,text="I am not robot",var=chk)
chkb.grid(row=30,column=0)

def reg():

    messagebox.showinfo("WELCOME TO OLA SANSAR","You've registered successfully!")

btn1=Button(text="Register",fg="green",bg="orange",font="Ariel",command=reg)
btn1.grid(row=35,column=2)

Name=ent1.get()
bp.mainloop()
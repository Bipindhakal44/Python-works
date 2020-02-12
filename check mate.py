from tkinter import *
from tkinter import messagebox
dc = Tk()
dc.title('OLA Log-in Form')
dc.geometry('333x444')
wor1 = Label(dc,text='Enter your e-mail')
wor1.pack()
b=1


err1 = Entry(dc,fg='black',bg='red',width=30)
err1.pack(padx=10,pady=10)

wor2 = Label(dc, text='Enter your password')
wor2.pack()

ery2 = Entry(dc,bg='red',width=10)
ery2.pack()

e = err1.get()
f = ery2.get()

#if b==e:
def bc():
        wor3 = Label(dc, text='You were registered with name of')
        wor3.pack()
#elif b != e:
    def bc():
        wor4 = Label(dc, text='Check your email or password and try it again!')
        wor4.pack()
bttn1 =Button(dc,text="Log-in",fg="green",bg="orange",font="Ariel", command=bc)
bttn1.pack(padx=10, pady=10)

dc.mainloop()
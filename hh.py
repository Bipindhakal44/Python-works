from tkinter import*
import pickle
vv = Tk()
vv.title('Sirens')
vv.geometry('200x300')


ent1=Entry(fg='purple',bg='white',width=30)
ent1.pack(padx=10,pady=10)


ent2=Entry(fg='purple',bg='white',width=30)
ent2.pack(padx=10,pady=10)

ent3=Entry(fg='purple',bg='white',width=20)
ent3.pack(padx=10,pady=10)

ent4=Entry(fg='purple',bg='white',width=20)
ent4.pack(padx=10,pady=10)

a = ent1.get()
b = ent2.get()
c = ent3.get()
d = ent4.get()
def data():
    q = open('mkl.pkl','wb')
    pickle.dump(a, q)
    pickle.dump(b, q)
    pickle.dump(c, q)
    pickle.dump(d, q)

    q.close()
btn1=Button(text="Register",fg="green",bg="orange",font="Ariel",command=data)
btn1.pack(padx=10,pady=10)
vv.mainloop()
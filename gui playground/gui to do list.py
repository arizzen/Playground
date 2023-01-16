import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *



home = Tk()

def add(Event):
    a= str(st1.get())
    st2.insert(0, a)



Label(home, text="TO-DO-List").pack()

st1=Entry(home, width= 30,)
st1.pack(side=LEFT, padx=10, pady=10)

but1=Button(home, text="Add")
but1.bind("<Button-1>", add)
but1.pack(side=LEFT)

st2=Entry(home, width=30,)
st2.pack(side=LEFT, padx=10,pady=10)


home.mainloop()


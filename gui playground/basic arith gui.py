'''
a program that finds the square of an inputed number
'''
import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *

def square(Event):
    a= int(num1.get())
    b= a*a
    answer.insert(0, b)

home=Tk()

Label(home, text="finding the square of a number").pack()
num1=Entry(home)
num1.pack(side=LEFT)

but1=Button(home, text="the square is:")
but1.bind("<Button-1>", square)
but1.pack(side=LEFT)

answer= Entry(home)
answer.pack(side=LEFT)

home.mainloop()
'''
a program that finds the square of an inputed number
'''
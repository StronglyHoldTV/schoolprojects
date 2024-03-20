import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

def dom(x, y):
    c.create_rectangle(x-25, y+50, x+25, y, fill='green', width=0)
    c.create_polygon(x-25, y, x+25, y, x, y-25, fill='red')

def rad():
    

def nahodne():

b = tk.Button(text = 'rad', command=rad)
b.pack()

b = tk.Button(text = 'nahodne', command=nahodne)
b.pack()

dom(250, 250)

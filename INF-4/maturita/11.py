import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

def dom(x, y):
    c.create_rectangle(x-25, y+50, x+25, y, fill='green', width=0)
    c.create_polygon(x-25, y, x+25, y, x, y-25, fill='red')

def clear():
    c.delete('all')

def rad():
    clear()
    for x in range(100,500,100):
        dom(x, 250)
    

def nahodne():
    clear()
    for _ in range(0, 4):
        dom(random.randint(25,500-25), random.randint(0, 500-50))

b = tk.Button(text = 'rad', command=rad)
b.pack()

b = tk.Button(text = 'nahodne', command=nahodne)
b.pack()

dom(250, 250)

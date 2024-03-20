import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

def delete():
    c.delete('all')

def nakresliStrom(x, y):
    c.create_rectangle(x-5, y+100, x+5, y+50, fill = 'brown')
    c.create_oval(x+45, y+50, x-45, y-40, fill='green')

def rad():
    delete()
    for x in range(100,500,100):
        nakresliStrom(x, 250)

def r():
    delete()
    for i in range(0,4):
        nakresliStrom(random.randint(45, 500-45), random.randint(40, 400))

button = tk.Button(text = 'zmaz', command=delete)
button.pack()
button = tk.Button(text = 'rad', command=rad)
button.pack()
button = tk.Button(text = 'nahodne', command=r)
button.pack()

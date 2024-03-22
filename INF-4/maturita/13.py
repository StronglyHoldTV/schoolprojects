import tkinter as tk
import math as m

c = tk.Canvas(width = 500, height=500)
c.pack()

tk.Label(text = "Hrubka ciary").pack()
v = tk.Entry()
v.pack()
v.insert(0,'2')

def draw(e):
    w = int(v.get())
    color = 'green'
    if(e.x <= 250 and e.y <= 250):
        color = 'red'
    if(e.x > 250 and e.y <= 250):
        color = 'blue'
    if(e.x <= 250 and e.y > 250):
        color = 'yellow'
    c.create_line(250, 250, e.x, e.y, width = w, fill = color)

def clear():
    c.delete('all')

tk.Button(text = 'zmaz', command=clear).pack()

c.bind('<Motion>', draw)

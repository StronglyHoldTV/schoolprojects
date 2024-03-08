import tkinter as tk

c = tk.Canvas()

c.pack()

x, y = 50, 50
a1, a2 = 180, 100

c.create_rectangle(x, y, x+a1, y+a1, fill='indian red')
c.create_rectangle(x+(a1/2)-(a2/2), y+(a1/2)-(a2/2), x+(a1/2)+(a2/2), y+(a1/2)+(a2/2), fill='light blue')
c.create_text(x, y, text='A', anchor=tk.SE)
c.create_text(x+a1, y, text='B', anchor=tk.SW)
c.create_text(x+a1, y+a1, text='C', anchor=tk.NW)
c.create_text(x, y+a1, text='D', anchor=tk.NE)
c.create_text(x+a1, y+(a1/2), text=a1, anchor=tk.W)
c.create_text(x+(a1/2), y+(a1/2)+(a2/2), text=a2, anchor=tk.S)

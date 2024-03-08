import tkinter as tk
import random as r

c = tk.Canvas(width = 500, height = 500)
c.pack()


while True:
    size = r.randint(50, 100)
    x = r.randint(0, 500-size)
    y = r.randint(0, 500-size)
    c.create_oval(x, y, x+size, y+size)
    c.update()
    c.after(300)

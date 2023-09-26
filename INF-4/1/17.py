import tkinter as tk
import math

c = tk.Canvas(width = 500, height = 500)


def slnko(n, x, y):
    c.create_oval(x-20, y-20, x+20, y+20, fill="yellow", width=0)
    for i in range(0, 360, 360//n):
        rad = math.radians(i)
        c.create_line(x, y, x+70*math.cos(rad), y+70*math.sin(rad), width=8, fill='yellow')

slnko(10, 100, 80)
slnko(20, 250, 120)

c.pack()
c.mainloop()

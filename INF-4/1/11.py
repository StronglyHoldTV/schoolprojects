import tkinter as tk
import random

c = tk.Canvas()
c.pack()


def kruhy(x, y):
    for i in range(5*10, 0, -5):
        c.create_oval(x-i, y-i, x+i, y+i, fill=f'#{random.randint(0,255**3):06x}')

for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))

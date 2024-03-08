import tkinter as tk
import random

c = tk.Canvas(width = 500, height=500)
c.pack()

x0, y0 = 500, 500
xm, ym = 0, 0

n = 7

for _ in range(0, n+1):
    x = random.randint(5, 501-5)
    y = random.randint(5, 501-5)

    c.create_oval(x-5, y-5, x+5, y+5, fill='red')

    if(xm < x):
        xm = x
    if(ym < y):
        ym = y
    if(x0 > x):
        x0 = x
    if(y0 > y):
        y0 = y
c.create_rectangle(x0, y0, xm, ym)

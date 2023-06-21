import tkinter as tk
import random
import math

c = tk.Canvas(width = 500, height = 500)

c.pack()

x0, y0 = 180, 130
r = 110

for _ in range(0, 10001):
    
    x = random.randint(10, 351)
    y = random.randint(10, 251)
    color = 'yellow'
    if(y < 170):
        color = 'red'
    if(y < 90):
        color = 'black'
    c.create_oval(x, y, x+10, y+10, width = 0, fill=color)

import tkinter as tk
import random
import math

c = tk.Canvas(width = 300, height = 300)

c.pack()

x0, y0 = 180, 130
r = 110

for _ in range(0, 10001):
    
    x = random.randint(0, 300-10)
    y = random.randint(0, 300-10)
    color = 'blue'
    if ((x0-x)**2+(y0-y)**2)**0.5 <= r:
        color='red'
    c.create_oval(x, y, x+10, y+10, width = 0, fill=color)

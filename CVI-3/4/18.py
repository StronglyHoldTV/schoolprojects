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
    color = 'red'
    if(y < 120):
        color = 'white'
    if(251-y > x and y > x): # y > x
        color = 'blue'
    c.create_oval(x, y, x+10, y+10, width = 0, fill=color)

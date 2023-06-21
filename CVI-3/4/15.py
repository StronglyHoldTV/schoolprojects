import tkinter as tk
import random
import math

c = tk.Canvas(width = 300, height = 300)

c.pack()

x0, y0 = 180, 130
r = 110
n = 0
for _ in range(0, 10001):
    
    x = random.randint(0, 300-4)
    y = random.randint(0, 300-4)
    color = 'blue'
    if x*x+y*y<=300*300:
        color='red'
        n+=1
    c.create_oval(x, y, x+4, y+4, width = 0, fill=color)
print((n/10000)*4)

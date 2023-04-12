import tkinter as tk
import math
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

n = 14
x, y = 250, 250
r = 100
angle = 360/n

for i in range(n+1):
    a = angle*i

    k = (x+r*math.cos(math.radians(a+angle))-(x+r*math.cos(math.radians(a))))
    l = (y+r*math.sin(math.radians(a+angle))-(y+r*math.sin(math.radians(a))))
    m = ((k**2+l**2)**0.5)/2
    c.create_oval(x+r*math.cos(math.radians(a))-m,
                  y+r*math.sin(math.radians(a))-m,
                  x+r*math.cos(math.radians(a))+m,
                  y+r*math.sin(math.radians(a))+m, fill=f'#{random.randrange(256**3):06x}')
    
    

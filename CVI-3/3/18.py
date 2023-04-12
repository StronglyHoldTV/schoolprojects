import tkinter as tk
import math

c = tk.Canvas(width = 500, height = 500)
c.pack()

n = 7
a = 100
x, y = 180, 130

v = (a**2-(a*0.5)**2)**0.5

angle = 360/n

for i in range(n):
    a = i*angle
    c.create_line(x+v*math.cos(math.radians(a)),
                  y+v*math.sin(math.radians(a)),
                  x+v*math.cos(math.radians(a+angle)),
                  y+v*math.sin(math.radians(a+angle)), width = 3)

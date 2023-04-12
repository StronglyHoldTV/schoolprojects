import tkinter as tk
import math

c = tk.Canvas(width = 500, height = 500)
c.pack()

x, y, v = 180, 130, 125
n = 7
angle = 360/n

for i in range(n):
    a = angle*i
    for j in range(n):
        b = angle*j
        c.create_line(x+v*math.cos(math.radians(a)),
                      y+v*math.sin(math.radians(a)),
                      x+v*math.cos(math.radians(b)),
                      y+v*math.sin(math.radians(b)))

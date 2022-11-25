import tkinter as tk
import random


c = tk.Canvas(width = 500, height = 500)
c.pack()

for _ in range(0,10):
    size = random.randint(25,60)
    x = random.randint(0,500)
    y = random.randint(0, 500)

    c.create_rectangle(x+(size/2)-5, y, x+(size/2)+5, y-5)
    c.create_polygon(x, y-5, x+size, y-5, x+(size/2), y- (((2*(size-5)))/3)-5)
    c.create_polygon(x+3, y-(((2*(size-5)))/3)+5, x+size-3, y-((2*(size-5)))/3+5, x+(size/2), y- 2*((2*(size-5)))/3)
    c.create_polygon(x+6, y-2*((2*(size-5)))/3+5, x+size-6, y-2*((2*(size-5)))/3+5, x+(size/2), y- 3*((2*(size-5)))/3)
    c.create_oval(x+(size/2)-(size/6), y- 3*((2*(size-5)))/3-(size/6), x+(size/2)+(size/6), y- 3*((2*(size-5)))/3+(size/6))
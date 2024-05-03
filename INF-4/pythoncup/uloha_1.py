import tkinter as tk
import random

c = tk.Canvas(width=500, height = 500)
c.pack()
x = 0
m = 5
while x + m < 250 - m:
    c.create_line(x, 0, x, 500)
    c.create_line(500-x, 0, 500-x, 500)
    x += m
    m += random.randint(1,3)
    

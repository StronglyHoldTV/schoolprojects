import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

for i in range(0, 1001):
    color = 'green'
    x = random.randint(0, 1000-10)
    y = random.randint(0, 500-10)
    if y < 250:
        color = 'red' if x < 250 else 'blue'
    c.create_oval(x, y, x+10, y+10, fill=color)
##a = 10
##b = 7
##a < b - false
##a >= b + 3 - true
##b < a < 2 * b - true
##true
##false
##true
##false
##false


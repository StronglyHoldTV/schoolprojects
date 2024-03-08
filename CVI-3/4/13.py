import tkinter as tk
import random

c = tk.Canvas(width = 300, height = 300)

c.pack()

for _ in range(0, 10001):
    x = random.randint(0, 300-10)
    y = random.randint(0, 300-10)
    #print(x-150)
    #300=75+150+50
    color = 'green'
    if(x > y):
        color = 'blue'
        if(300-x < y):
            color = 'yellow'
    if x < y and 300-x > y:
        color = 'red'
    c.create_oval(x, y, x+10, y+10, width = 0, fill=color)

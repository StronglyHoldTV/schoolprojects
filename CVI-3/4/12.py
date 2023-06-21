import tkinter as tk
import random

c = tk.Canvas(width = 300, height = 300)

c.pack()

for _ in range(0, 10001):
    x = random.randint(0, 300-10)
    y = random.randint(0, 300-10)
    #print(x-150)
    #300=75+150+50
    c.create_oval(x, y, x+10, y+10, width = 0, fill='blue'if (x < 75+150 and x > 75 and y < 75+150 and y > 75) else 'red')

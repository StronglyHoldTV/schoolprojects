import tkinter as tk
import random


c = tk.Canvas(width = 380, height = 260)
c.pack()

def kruhy(x, y):
    for i in range(50, 0, -5):
        c.create_oval(x-i, y-i, x+i, y+i, fill=f"#{random.randint(0, 256**3):06x}")
        

for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))

import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500, bg = 'navy')
c.pack()

n = 200

for _ in range(n):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    s = random.randint(10, 20)

    c.create_text(x, y, text='*', font=f'Arial {s}', fill='yellow')

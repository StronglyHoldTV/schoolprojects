import random
import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

text = input('zadaj text... ')
text = text.upper()
x = 1
for a in text:
    color = f'#{random.randint(0, 255**3):06x}'
    co = f'#{random.randint(0, 255**3):06x}'
    c.create_rectangle(x, 100, x+30, 130, fill=color)
    c.create_text(x+15, 100+15, anchor = tk.CENTER, text=a, font='arial 26', fill=co)
    x += 30

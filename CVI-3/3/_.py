import tkinter as tk
import tkinter.font as tkfont
import random

c = tk.Canvas(width=700, height=700)
font = tkfont.Font(family="Consolas", size=10, weight="normal")

c.pack()


for i in range(500):
    a = font.measure(i)
    #print(a)
    b = font.metrics()['ascent']
    x = random.randint(a, 700-a)
    y = random.randint(b, 700-b)
    c.create_text(x, y, text=i)


for i in range(500):
    a = font.measure(i)
    #print(a)
    b = font.metrics()['ascent']
    x = random.randint(a, 700-a)
    y = random.randint(b, 700-b)
    c.create_text(x, y, text=f'{x} {y}')

    sirka, vyska = 200,100

    c.create_rectangle(x, y, x+sirka, y+vyska)

import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

n = 1

for i in range(n):
    size = 50
    v = ((size**2)-((size*0.5)**2))**0.5
    x = random.randint(0, 500-size)
    y = random.randint(0, 500-size-v)
    c.create_polygon(x, y+v, x+size, y+v, x+0.5*size, y, fill = f'#{random.randrange(256**3):06x}')
    c.create_rectangle(x, y+v+size, x+size, y+v, fill = f'#{random.randrange(256**3):06x}')

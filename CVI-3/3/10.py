import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
n = 30
c.pack()

for i in range(n):
    x = random.randint(0, 500-40)
    y = random.randint(0, 500-40)

    c.create_oval(x, y, x+40, y+40, fill=f'#{random.randrange(256**3):06x}')
    c.create_text(x+20, y+20, text=f'{random.randint(0, 9)}', font='Arial 30')

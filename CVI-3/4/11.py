import tkinter as tk
import random

c = tk.Canvas(width = 550, height = 500)
c.pack()
k = 21

for y in range(10, 10+11*40, 40):
    a = 0
    r = random.randint(7, 10)
    for x in range(10, 10+(r+1)*40, 40):
        
        v = random.randint(1, 5)
        a += v
        c.create_oval(x, y, x+30, y+30)
        c.create_text(x+15, y+15, text = v, font = "Arial 20")
    if k == a:
        c.create_text(450, y+15, text = 'HURA',
                      font = "Arial 20", anchor = tk.W, fill='green')
        continue
    if k != a:
        c.create_text(450, y+15, text = 'SKODA',
                      font = "Arial 20", anchor = tk.W, fill='red')
        continue



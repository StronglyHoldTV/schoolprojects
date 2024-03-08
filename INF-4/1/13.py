import random
import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

def dom(x, y, vel1, vel2):
    c.create_rectangle(x, y, x+vel1, y-vel1,
                       fill=f'#{random.randint(0, 255**3):06x}')
    c.create_polygon(x, y-vel1, x+(vel1//2), y-vel1-vel2,
                     x+vel1, y-vel1, width=1, outline='black',
                     fill=f'#{random.randint(0, 255**3):06x}')

x, y = 10, 150
while x < 330:
    v = random.randint(20, 50)
    dom(x, y, v, random.randint(v//2, v))
    x += v

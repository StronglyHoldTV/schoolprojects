import tkinter as tk
import math
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()
tk.Label(text = 'Zadaj pocet:').pack()
pocet = tk.Entry()
pocet.pack()
v = tk.IntVar(value = 0)
tk.Radiobutton(text = 'Jedna', variable = v, value = 0).pack()
tk.Radiobutton(text = 'Viac', variable = v, value = 1).pack()

def draw():
    c.delete('all')
    n = int(pocet.get())
    x1 = 250+100*math.cos(0)
    y1 = 250+100*math.sin(0)
    x2 = 250+100*math.cos(math.radians(360//n))
    y2 = 250+100*math.sin(math.radians(360//n))
    r = (((x1-x2)**2+(y1-y2)**2)**0.5)/2
    print(r)
    for deg in range(0,360, 360//n):
        color = 'white'if v.get() == 0 else f'#{random.randint(0, 255**3):06X}'
        print(color)
        rad = math.radians(deg)
        c.create_oval(250+100*math.cos(rad)-r, 250+100*math.sin(rad)-r,
                      250+100*math.cos(rad)+r, 250+100*math.sin(rad)+r,
                      fill = color)
    return


tk.Button(text = 'Kresli', command = draw).pack()


import tkinter as tk
import math
import random as rand

c = tk.Canvas(width = 500, height = 500)
c.pack()

b = tk.IntVar()
tk.Radiobutton(text='cierne', variable=b, value=0).pack()
tk.Radiobutton(text='farebne', variable=b, value=1).pack()
tk.Label(text='Kolko guliciek')
d = tk.Entry()
d.pack()

def draw():
    c.delete('all')
    random = b.get()
    n = int(d.get())
    for i in range(0,355, 360//n):
        x = 250+math.cos(math.radians(i))*50
        y = 250+math.sin(math.radians(i))*50
        x1 = 250+math.cos(math.radians(i+360//n))*50
        y1 = 250+math.sin(math.radians(i+360//n))*50
        distance = ((x-x1)**2+(y-y1)**2)**0.5
        color = f"#{rand.randint(0,256**3):06X}"if(b.get())else"black"
        c.create_oval(x-distance//2,y-distance//2,x+distance//2,y+distance//2, fill=color)
    


tk.Button(text='Nakresli',command=draw).pack()






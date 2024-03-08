import tkinter as tk
import math

c = tk.Canvas(width = 500, height = 500)
c.pack()

b = tk.IntVar()
tk.Radiobutton(text='cierne', variable=b, value=0).pack()
tk.Radiobutton(text='farebne', variable=b, value=1).pack()
tk.Label(text='Kolko guliciek')
d = tk.Entry()
d.pack()

def draw():
    random = b.get()
    n = int(d.get())
    for i in range(0,360, 360//n):
        x = 250+math.cos(math.radians(i))*50
        y = 250+math.sin(math.radians(i))*50
        c.create_oval(x-5,y-5,x+5,y+5)
    


tk.Button(text='Nakresli',command=draw).pack()






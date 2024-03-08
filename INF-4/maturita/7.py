import tkinter as tk
import math

c = tk.Canvas(width = 500, height = 500)
c.pack()

def zRohu():
    for i in range(0,360):
        r = math.radians(i)
        c.create_line(0, 0, 500*math.sin(r), 500*math.cos(r))
        c.after(100)
        c.update()
    return

def lomena():
    for i in range(500, 0, -20):
        c.create_line(500-i, i, 500-i, i-20)
        c.create_line(500-i, i, 500-i-20, i)
        c.after(100)
        c.update()

def siet():
    for i in range(0, 500, 10):
        c.create_line(0, i, 500, i)
        c.create_line(i, 0, i, 500)
        c.after(100)
        c.update()

button = tk.Button(text = "Z rohu", command=zRohu)
button.pack()
button = tk.Button(text = "Siet ciar", command=siet)
button.pack()
button = tk.Button(text = "lomena ciara", command=lomena)
button.pack()

import tkinter as tk
import math as m

c = tk.Canvas(width = 500, height = 500)
c.pack()

isRunning = True
x = 250
y = 250
angle = m.radians(45)
speed = 10

def run():
    global x
    global y
    global angle
    while isRunning:
        c.after(100)
        c.delete('all') # toto vymazat necha ciaru
        c.create_oval(x-10, y-10, x+10, y+10)
        c.update()
        x = x+speed*m.cos(angle)
        y = y+speed*m.sin(angle)
        if(x > 450):
            angle = angle + m.radians(45)
        if(y > 450):
            angle = angle + m.radians(45)
        if(x < 50):
            angle = angle + m.radians(45)
        if(y < 50):
            angle = angle + m.radians(45)

def tap(e):
    global isRunning
    isRunning = not isRunning
    run()

c.bind('<Button-1>', tap)

run()

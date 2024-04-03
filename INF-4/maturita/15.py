import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

state = 0
x, y = random.randint(0,450), random.randint(50,500)

def draw():
    global state
    if(state == 4):
        state = 0
        global x
        global y
        x, y = random.randint(0,450), random.randint(50,500)
    if(state == 0):
        c.create_line(x, y, x, y-20, fill='green')
    if(state == 1):
        c.create_line(x, y-5, x-10, y-15, fill='green')
    if(state == 2):
        c.create_line(x, y-5, x+10, y-15, fill='green')
    if(state == 3):
        c.create_oval(x+10, y-40, x-10, y-20, fill='red')
    state += 1
    

isRunning = True

def s():
    global isRunning
    isRunning = not isRunning
    while(isRunning):
        c.after(100)
        draw()
        c.update()


tk.Button(text='START/STOP', command = s).pack()

while(isRunning):
    c.after(100)
    draw()
    c.update()


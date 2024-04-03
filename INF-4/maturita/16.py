import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

isRunning = True
x = 0

def run():
    global x
    while isRunning:
        c.after(100)
        c.delete('all')
        c.create_line(x, 250, x+50, 250, arrow=tk.LAST)
        c.update()
        x+=10
        if(x>500):
            x = 0

def tap(e):
    global isRunning
    isRunning = not isRunning
    run()

c.bind('<Button-1>', tap)

run()

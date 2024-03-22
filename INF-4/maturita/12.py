import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

def draw(x, y):
    c.create_rectangle(x-10, y-10, x+10, y+10)
    
def clear():
    c.delete('all')

def tap(e):
    if(e.state!=264): return
    draw(e.x, e.y)
        

c.bind('<Motion>', tap)
b = tk.Button(text='zmaz', command=clear)
b.pack()

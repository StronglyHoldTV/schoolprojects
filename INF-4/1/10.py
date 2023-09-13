import tkinter

def koleso(x, y, r=15, color = 'blue'):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill = color)

def doska(x, y, width = 100, height = 20, color = 'red'):
    canvas.create_rectangle(x-(width//2), y, x+(width//2), y-(height), fill = color)

def maly_vozik(x, y):
    doska(x, y)
    koleso(x-30, y)
    koleso(x+30, y)

def velky_vozik(x, y):
    doska(x, y, 150, 40, 'green')
    koleso(x-35, y, 25, 'orange')
    koleso(x+35, y, 25, 'orange')

canvas = tkinter.Canvas()
canvas.pack()

maly_vozik(200, 100)
velky_vozik(150, 200)
maly_vozik(300, 210)

tkinter.mainloop()

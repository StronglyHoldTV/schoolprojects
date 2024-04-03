import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()
y = tk.Entry()
x = tk.Entry()

l = []

def draw():
    c.delete('all')
    c.create_line(l)

def press():
    global l
    y1 = y.get()
    y2 = 0
    x1 = x.get()
    x2 = 0
    if(y1!=''):
        y2 = int(y1)
    if(x1!=''):
        x2 = int(x1)
    pos = []
    for i in l:
        pos.append((i[0]+x2, i[1]+y2))
    l = pos
    draw()
    

tk.Label(text = 'y').pack()
y.pack()
tk.Label(text = 'x').pack()
x.pack()
tk.Button(text = 'Posun', command = press).pack()

def e(e):
    l.append((e.x, e.y))
    print(e)
    draw()



c.bind('<Button-1>',e)

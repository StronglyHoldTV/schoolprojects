import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()


tk.Label(text = 'zadaj text:').pack()
text = tk.Entry()
text.pack()

def nahoda():
    c.delete('all')
    for no, i in enumerate(text.get()):
        x = 250 - 30*len(text.get())//2 + 30*no
        c.create_text(x, 250, text = i, font = 'Arial 20',
                      fill=f'#{random.randint(0,255**3):06X}',
                      anchor = tk.CENTER)
    return

def striedavo():
    c.delete('all')
    farba1 = 'black'
    farba2 = 'red'
    for no, i in enumerate(text.get()):
        x = 250 - 30*len(text.get())//2 + 30*no
        c.create_text(x, 250, text = i,
                      font = 'Arial 20', fill= farba1 if no%2==0 else farba2,
                      anchor = tk.CENTER)
    return

def posun():
    c.delete('all')
    for no, i in enumerate(text.get()):
        x = 250 - 30*len(text.get())//2 + 30*no
        y = 250 + 30*len(text.get())//2 - 30*no
        c.create_text(x, y, text = i, font = 'Arial 20', anchor = tk.CENTER)
    return

tk.Button(text = 'Nahodne', command=nahoda).pack()
tk.Button(text = 'Striedavo', command=striedavo).pack()
tk.Button(text = 'Posun', command=posun).pack()


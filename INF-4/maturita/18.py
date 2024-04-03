import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

tk.Label(text = 'Text ktory mam vykreslit').pack()
ent = tk.Entry()
ent.pack()

def rnd():
    c.delete('all')
    for x, ch in enumerate(ent.get()):
        c.create_text(10+x*15, 250, text = ch, anchor=tk.W, font='Arial 16', fill=f'#{random.randint(0, 256**3):06X}')
    return

def sc():
    c.delete('all')
    for x, ch in enumerate(ent.get()):
        c.create_text(10+x*15, 250, text = ch, anchor=tk.W, font='Arial 16', fill=f'{("black", "red")[x%2]}')
    return

def up():
    c.delete('all')
    for x, ch in enumerate(ent.get()):
        c.create_text(10+x*15, 250-x*10, text = ch, anchor=tk.W, font='Arial 16')
    return

tk.Button(text="Nahodne", command=rnd).pack()
tk.Button(text="Striedavo", command=sc).pack()
tk.Button(text="Kazdy vyssie", command=up).pack()

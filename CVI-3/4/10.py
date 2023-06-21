import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

x, y = 190, 130
r = 120
k = 6
a = 0

while r >= 15:
    r = r-3
    c.create_oval(x-r, y-r, x+r, y+r, outline='grey'if a%6 == 0 else 'black')
    a+= 1

import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

x, y = 70, 100
r = 50
dx, dy = 120, 60

c.create_oval(x, y, x+2*r, y+2*r, outline='blue', width=15)
c.create_oval(x+0.5*dx, y+dy, x+2*r+0.5*dx, y+2*r+dy, outline='yellow', width=15)
c.create_oval(x+dx, y, x+2*r+dx, y+2*r, outline='black', width=15)
c.create_oval(x+1.5*dx, y+dy, x+2*r+1.5*dx, y+2*r+dy, outline='green', width=15)
c.create_oval(x+2*dx, y, x+2*r+2*dx, y+2*r, outline='red', width=15)

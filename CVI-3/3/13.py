import tkinter as tk
c = tk.Canvas()

x, y = 50, 250
a = 280

c.pack()
v = ((a**2)-((a*0.5)**2))**0.5
print(v)
c.create_polygon(x, y, x+a, y, x+0.5*a, y-v, fill='blue')

import tkinter as tk
import random

c = tk.Canvas(width= 500, height=500)
c.pack()

x, y = 10, 100
d = 20
n = 16

for i in range(int(n/2)):
    c.create_line(x,y, x+d, y+d, x+2*d, y, width=4, fill='blue')
    x+=2*d

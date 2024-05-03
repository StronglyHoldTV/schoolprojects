import tkinter as tk
import random as r

l = []
n = -1
while n!=0:
    n = int(input("n "))
    l.append(n)

l.pop(-1)

c = tk.Canvas(width=500, height=500)
c.pack()

xsize = 500//len(l)
ysize = 500//max(l)

for no, i in enumerate(l):
    c.create_rectangle(no*xsize, 500, (no+1)*xsize, 500-(i*ysize), fill=f"#{r.randint(0,255**3):06X}", width = 0)

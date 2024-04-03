import tkinter as tk
import random

ca = tk.Canvas(width = 500, height = 500)
ca.pack()

a = (250-20, 250)
b = (250+20, 250)
c = (250+10, 240)
d = (250-30, 240)
v = (250, 200)

ca.create_line(a, b, c, d, a)
ca.create_line(a, v)
ca.create_line(b, v)
ca.create_line(c, v)
ca.create_line(d, v)

def e(e):
    print(e)
    v = (e.x, e.y)
    ca.delete('all')
    ca.create_line(a, b, c, d, a)
    ca.create_line(a, v)
    ca.create_line(b, v)
    ca.create_line(c, v)
    ca.create_line(d, v) 

ca.bind('<Motion>',e)
    
    



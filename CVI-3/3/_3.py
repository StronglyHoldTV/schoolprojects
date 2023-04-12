import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

dx = 2
width = 10

for i in range(15):
    height = random.randint(10, 500)
    c.create_rectangle(dx*i+width*i, 500, dx*i+width*(i+1), 500-height)
    

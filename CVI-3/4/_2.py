import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

for i in range(10, 110, 10):
    ch = random.choice([True, False])
    if ch:
        c.create_oval(i, 10, i+8, 18)
    else:
        c.create_rectangle(i, 10, i+8, 18)
    

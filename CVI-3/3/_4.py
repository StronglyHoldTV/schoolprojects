import tkinter as tk
import math

c = tk.Canvas(width = 500, height=500)
r = 100
c.pack()

for i in range(0, 360, 15):
    rad = math.radians(i)
    c.create_line(250, 250, 250+r*math.cos(rad), 250+r*math.sin(rad))
    c.create_text(250+r*math.cos(rad), 250+r*math.sin(rad), text=f'{i}°')

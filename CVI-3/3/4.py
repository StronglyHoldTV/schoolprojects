import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()
n = 20

color = ['yellow', 'blue', 'red']

for i in reversed(range(1 , 21)):

    a = 10*i
    c.create_rectangle(250-(a/2), 250-(a/2), 250+(a/2), 250+(a/2), fill=color[i%3])


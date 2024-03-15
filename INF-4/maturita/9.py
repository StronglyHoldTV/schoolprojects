import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

n = int(input('Zadaj n'))
m = bool(input('Farebne? True False'))
print(m)

for i in range(0, 500, 500//n):
    for j in range(0, 500, 500//n):
        color = 'black'
        c.create_oval(i, j, i+500//n, j+500//n,
                      fill='green'if((i == j or (i + j == 500-500//n)) and m)else'black')

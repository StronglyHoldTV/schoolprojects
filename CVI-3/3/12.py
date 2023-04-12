import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()

n = int(input('zadaj n: '))

w = (380-10-n*10)//n

#c.create_line(380, 0, 380, 380)

for i in range(0, n):
    c.create_rectangle(10+(w*i)+(i*10), 10, 10+w*(i+1)+(i*10), w+10)
    print((10+w*i+(i*10))-(10+w*(i+1)+(i*10)))
    print(w)
    print(10+w*(i+1)+(i*10))



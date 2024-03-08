import tkinter as tk

c = tk.Canvas(width = 500, height = 500)

c.pack()

row = int(input('zadaj pocet riadkov '))
col = int(input('zadaj pocet stlpcov '))

vel = 30
farba1, farba2 = 'maroon', 'gold'
space = 2

for i in range(10, 10+(vel+space)*row, (vel+space)):
    for j in range(10, 10+(vel+space)*col, (vel+space)):
        c.create_rectangle(i, j, i+vel, j+vel, fill = farba1)
        farba1, farba2 = farba2, farba1
        

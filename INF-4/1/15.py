import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

def rgb(r: int, g: int, b: int) -> str:
    return f'#{r:02x}{g:02x}{b:02x}'

for i in range(0, 12):
    for j in range(0, 12):
        g = round(((i+1)/12)*((j+1)/12)*255)
        print(g)
        c.create_rectangle(5+i*30, 5+j*30, 5+i*30+30, 5+j*30+30, fill=rgb(255, g, 0))

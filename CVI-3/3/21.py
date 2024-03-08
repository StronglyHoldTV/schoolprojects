import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

x, y = 30, 30
sir, vys = 325, 216
modra, cervena = '#0b4ea2', '#ee1c25'

c.create_rectangle(x, y, x+sir, y+vys, width=2)

c.create_rectangle(x, y, x+sir, x+vys*(1/3), fill='white', width=0)
c.create_rectangle(x, y+vys*(1/3), x+sir, x+vys*(2/3), fill='blue', width=0)
c.create_rectangle(x, y+vys*(2/3), x+sir, x+vys, fill='red', width=0)
img=tk.PhotoImage(file="sk.png")
c.create_image(x+100, y+108, image=img, anchor=tk.CENTER)

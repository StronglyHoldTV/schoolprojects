import tkinter as tk

c = tk.Canvas()
c.pack()

x, y = 50, 50

c.create_rectangle(x,y, x+100, y+100, fill='red')
c.create_rectangle(x+110, y, x+210, y+100, fill='blue')
c.create_text(x+50, y+50, text='cerveny', font='arial 20', fill='yellow')
c.create_text(x+50+110, y+50, text='modry', font='arial 20', fill='yellow')

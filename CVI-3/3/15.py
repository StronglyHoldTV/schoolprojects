import tkinter as tk

sirka, vyska = 300, 200


c = tk.Canvas(width = 500, height = 500)
c.pack()

c.create_rectangle(10, 10, 10+sirka, 10+vyska, width = 2)
c.create_rectangle(10, 10, 10+sirka, 10+vyska*0.5, fill = 'white', width = 0)
c.create_rectangle(10, 10+vyska*0.5, 10+sirka, 10+vyska, fill = 'red', width = 0)
c.create_polygon(10, 10, 10+sirka*0.5, 10+vyska*0.5, 10, 10+vyska, fill = 'blue')

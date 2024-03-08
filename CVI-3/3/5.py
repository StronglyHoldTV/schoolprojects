import tkinter as tk
import random
sizex, sizey = 135, 90
c = tk.Canvas(width = 3*50+2*sizex, height = 3*50+2*sizey)
c.pack()


#GERMANY

x, y = 50, 50

c.create_rectangle(x, y, x+sizex, y+sizey, width=2)
c.create_rectangle(x, y, x+sizex, y+(sizey*3/3), fill='yellow', width=0)
c.create_rectangle(x, y, x+sizex, y+(sizey*2/3), fill='red', width=0)
c.create_rectangle(x, y, x+sizex, y+(sizey/3), fill='black', width=0)

#FRANCE

x, y = 50, 50+sizey+50

c.create_rectangle(x, y, x+sizex, y+sizey, width=2)
c.create_rectangle(x, y, x+(sizex*3/3), y+sizey, fill='red', width=0)
c.create_rectangle(x, y, x+(sizex*2/3), y+sizey, fill='white', width=0)
c.create_rectangle(x, y, x+(sizex/3), y+sizey, fill='blue', width=0)

#ITALY

x, y = 50+sizex+50, 50 

c.create_rectangle(x, y, x+sizex, y+sizey, width=2)
c.create_rectangle(x, y, x+(sizex*3/3), y+sizey, fill='red', width=0)
c.create_rectangle(x, y, x+(sizex*2/3), y+sizey, fill='white', width=0)
c.create_rectangle(x, y, x+(sizex/3), y+sizey, fill='green', width=0)

#RUSSIA

x, y = 50+sizex+50, 50+sizey+50

c.create_rectangle(x, y, x+sizex, y+sizey, width=2)
c.create_rectangle(x, y, x+sizex, y+(sizey*3/3), fill='red', width=0)
c.create_rectangle(x, y, x+sizex, y+(sizey*2/3), fill='blue', width=0)
c.create_rectangle(x, y, x+sizex, y+(sizey/3), fill='white', width=0)





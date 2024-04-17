import tkinter as tk
n = 1
l = []
while(n != 0):
    n = int(input('asfasf'))
    l.append(n)
l.pop(-1)

c = tk.Canvas(width = 500, height = 500)
c.pack()

maximum = 500//max(l)
lenght = 500//len(l)


for no, x in enumerate(range(0,500, lenght)):
    y = 500 - maximum*l[no]
    c.create_rectangle(x, 500, x+lenght, y)
    




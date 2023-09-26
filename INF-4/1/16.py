import tkinter as tk
import random, math

c = tk.Canvas(width = 500, height = 500)
c.pack()


def vektor(x: int, y: int, dlzka: int, uhol: int):
    c.create_line(x, y, x+dlzka*math.cos(math.radians(uhol)),
                   y+dlzka*math.sin(math.radians(uhol)), arrow=tk.FIRST)

for i in range(10):
        vektor(random.randint(50, 300), random.randint(50, 200),
           random.randint(10, 80), random.randint(0, 359))


c.mainloop()
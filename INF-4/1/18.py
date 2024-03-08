import tkinter as tk
import math
import time

c = tk.Canvas(width = 500, height = 500)
x, y = 190, 130
c.pack()


def rucicka(uhol, dlzka, hrubka, farba):
    c.create_line(x, y, x+dlzka*math.cos(uhol), y+dlzka*math.sin(uhol),
                  width = hrubka, fill = farba, arrow = tk.LAST)
    return

def hodinky(hod, min, sek):
    c.create_oval(x - 100, y - 100, x + 100, y + 100)
    rucicka(math.radians(360/12*hod-90), 60, 10, "grey")
    rucicka(math.radians(360/60*min-90), 70, 6, "black")
    rucicka(math.radians(360/60*sek-90), 80, 2, "red")
    print(360/12*hod)
    print(360/60*min)
    print(360/60*sek)
    return

hodinky(12, 60, 60)


while True:
    c.delete('all')
    h, m, s = time.localtime()[3:6]
    hodinky(h, m, s)
    c.update()
    c.after(1000)

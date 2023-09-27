import random
import tkinter as tk

c = tk.Canvas(width=300, height=500)
c.pack()

def stv(riadok, stlpec, farba='white'):
    c.create_rectangle(5 + 30*riadok, 5 + 30*stlpec,
                       5 + 30*riadok + 30,
                       5 + 30*stlpec + 30, fill = farba, width = 0)

def nahodna_farba():
    return f'#{random.randint(0, 255**3):06x}'

for i in range(8):
    for j in range(12):
        if i == j:
            stv(i, j)
        else:
            stv(i, j, nahodna_farba())

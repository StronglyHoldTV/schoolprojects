import tkinter as tk
import random

c = tk.Canvas(width = 500, height = 500)
c.pack()
n = 10
s = 0
for i in range(n):
    hodnota = random.choice((1, 2, 5, 10, 20, 50))
    c.create_rectangle(100, 100+i*(20)-2, 100+50, 100+(i+1)*(20))
    c.create_text(100+25, 100+i*(20)-2+10, text = f'{hodnota} $', font = 'Arial 12')
    print(f'{100+i*(20)-2},, {100+i*(20)-2+10}')
    s += hodnota
c.create_text(100+50+25, 100+20, text = f'{s} $', font= 'Arial 12', anchor = tk.N) 

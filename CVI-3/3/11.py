import tkinter as tk
import random

c = tk.Canvas(height = 500, width = 500)
c.pack()

text = input('Zadaj text: ')
i = 0
for s in text:
    c.create_rectangle(i*30, 250-15, (i+1)*30, 250+15, fill=f'#{random.randrange(256**3):06x}')
    c.create_text(15+i*30, 250, text=s, font = 'Arial 26')
    i += 1

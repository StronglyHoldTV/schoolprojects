import random
import tkinter as tk

c = tk.Canvas(width = 500, height = 500)

c.pack()

def karticka(x: int, y: int, text: str):
    c.create_rectangle(x, y, x+100, y+40, fill='gray')
    c.create_text(x+50, y+20, text=text, anchor="center", font = "Arial 12")

for i in range(10):
    karticka(random.randint(0, 400), random.randint(0, 460), 'Python')

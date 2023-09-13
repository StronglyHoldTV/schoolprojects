import tkinter as tk

c = tk.Canvas()
c.pack()


def kruhy(x, y):
    for i in range(5, 5*11, 5):
        c.create_oval(x-5, y-5, x+5, y+5, fill=f'#')

for i in range(10):
    kruhy(random.randint(50, 330), random.randint(50, 210))

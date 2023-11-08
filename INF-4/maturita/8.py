import tkinter as tk
import math

c = tk.Canvas(width = 500, height = 500)
c.pack()

b = tk.IntVar()

tk.Button(text='Nakresli').pack()
tk.Radiobutton(text='cierne', variable=b, value=0).pack()
tk.Radiobutton(text='farebne', variable=b, value=1).pack()
tk.Label(text='Kolko guliciek')
d = tk.Entry().pack()


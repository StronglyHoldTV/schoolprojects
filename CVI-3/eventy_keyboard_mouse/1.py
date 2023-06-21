import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

def ovld(e):
    print(e)

c.bind("<ButtonPress>", ovld)

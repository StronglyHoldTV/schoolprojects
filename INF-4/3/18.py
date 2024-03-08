import tkinter as tk

def vypis_subor(s):
    c = tk.Canvas(width= 500, height=500)
    c.pack()
    c.create_text(250, 250)
    with open(s, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        a=250-(len(lines)*15)//2
        for i in lines:
            a += 15
            print(i)
            c.create_text(250, a, text=i, anchor='nw')


vypis_subor('text3.txt')

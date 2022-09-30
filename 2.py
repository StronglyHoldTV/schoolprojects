import tkinter as tk
import random

c = tk.Canvas(width=600, height=600)
colors = ["blue", "mediumblue", "darkblue", "royalblue", "navy"]

def water():
    for _ in range(0, random.randint(0, 100)):
        r = random.randint(20, 100)
        d = 2*r
        y = random.randint(75,600-75-r)
        x = random.randint(0, 600-r)
        #sice si myslel asi priemer ale mi sa na teba nehnevame
        color = random.choice(colors)
        c.create_oval(x, y, x+r, y+r, fill=color, outline=color)

def ladder():
    for i in range(0, 10):
        c.create_rectangle(60*i, 400, 60*(i+1), 460, fill="yellow")
        
        

for x in range(0,600):
    y = random.randint(20,70)
    c.create_rectangle(x, 0, x + 1, y, fill="green", outline="green")
    c.create_rectangle(x, 600-y, x+1, 600, fill="green", outline="green")
water()
ladder()
    
    

c.pack()
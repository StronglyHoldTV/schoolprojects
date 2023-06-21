import tkinter as tk
sirka = int(input('sirka platna n='))
c = tk.Canvas(width = sirka, height = 500)
c.pack()


x = 10
a = 20
while x*2<sirka:
    c.create_rectangle(x, 500, x+x, 500-x)
    x = x * 2
x = 10
for _ in range(5000):
    c.create_rectangle(x, 400, x+x, 400-x)
    if x*2>sirka:
        break;
    x = x * 2
     

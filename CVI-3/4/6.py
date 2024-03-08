import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

n = int(input('zadaj cislo: '))
cs = 0
x = 500
while n > 0:
    print(n % 10)
    c.create_rectangle(x, 250+25, x - 50, 250-25, fill='lightblue')
    c.create_text(x - 25, 250, anchor = tk.CENTER, text=n%10, font='Arial 25')
    cs = n % 10
    n = int(n / 10)
    x -= 55

print(f'ciferny sucet {cs}')

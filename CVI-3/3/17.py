import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

for i in range(26):
    a = 255/25
    r = int(255-(a*i))
    b = int(a*i)
   # print(i, a, r, b)
    c.create_rectangle(i*15, 0, (i+1)*15, 250, fill=f'#{r:02X}00{b:02X}', width = 0);

import tkinter as tk
c = tk.Canvas()
c.pack()
x, y = 200, 250
sirka = 200

for i in ['darkgreen', 'green', 'lime', 'springgreen']:
    c.create_rectangle(x+(sirka/2), y, x-(sirka/2), y-50, fill=i)
    sirka -= 50
    y -= 50
    

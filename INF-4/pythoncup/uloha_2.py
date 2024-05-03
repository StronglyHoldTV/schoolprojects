import tkinter as tk
c = tk.Canvas(width = 500, height = 500)

c.create_image(10,10, image = tk.PhotoImage(file = './machula0.png'), anchor = "nw")
c.pack(expand='yes')

c.create_image(10,10, image = tk.PhotoImage(file = './stvorec0.png'), anchor = "nw")

suradnice = [(260,90), (200,110), (260,60), (160,70)]
xvpravo = 350

# Kresli machule

for no, i in enumerate(range(0,3)):
    c.create_image(suradnice[no], image = tk.PhotoImage(f'machula{i}.png'), anchor = "nw")

import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()

a = tk.IntVar()

r = tk.Radiobutton(text="Kruh", variable=a, value=0)
r.pack()

r = tk.Radiobutton(text="Stvorec", variable=a, value=1)
r.pack()

tk.Label(text="Zadaj nazov farby").pack()
farba = tk.Entry()
farba.insert(0, "blue")
farba.pack()


tk.Label(text="Velkost tvaru").pack()
x = tk.Entry()
x.insert(0, "25")
x.pack()


def ovld(e):
    h = int(x.get())
    if(a.get() == 0):
        c.create_oval(e.x, e.y, e.x+h, e.y+h, fill=farba.get())
    else:
        c.create_rectangle(e.x, e.y, e.x+h, e.y+h, fill=farba.get())
    print(e)

def delete():
    c.delete("all")

c.bind("<Motion>", ovld)
button = tk.Button(text = "Zmaž", command=delete)
button.pack()

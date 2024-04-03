import tkinter as tk

c = tk.Canvas(width = 500, height = 500)
c.pack()
pozdravy = ['ahoj', 'cau', 'hello', 'tschus', 'den dobry']

def draw(t):
    print(t)
    c.delete('all')
    c.create_text(250, 250, text = t, anchor = tk.CENTER)


def keydown(e):
    print('down', e.char)
    for i in pozdravy:
        if i[0] == e.char:
            draw(i)

c.bind("<KeyPress>", keydown)
c.focus_set()

##
##import tkinter as tk
##def keyup(e):
##    print('up', e.char
##def keydown(e):
##    print('down', e.char
##
##root = tk.Tk()
##frame = tk.Frame(root, width=100, height=100)
##frame.bind("<KeyPress>", keydown)
##frame.bind("<KeyRelease>", keyup)
##frame.pack()
##frame.focus_set()
##root.mainloop()

##import tkinter as tk
##
##c = tk.Frame(tk.Tk(),width = 500, height = 500)
##
##def draw(e):
##    print(e)
##    return
##
##
##c.bind('<KeyPress>', draw)
##c.pack()


import tkinter as tk
def keyup(e):
    print('up', e.char
def keydown(e):
    print('down', e.char

root = tk.Tk()
frame = tk.Frame(root, width=100, height=100)
frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()

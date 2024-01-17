import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def kresli_text(zoznam):
    if(len(zoznam)==3):
        zoznam.append('arial 20')
    canvas.create_text(zoznam[0], zoznam[1], text = zoznam[2], font = zoznam[3])




zoz = [200, 100, 'PYTHON']
kresli_text(zoz)
kresli_text([200, 150, 'programovanie', 'consolas 35'])
kresli_text([200, 60, 'najlepšie je', 'tahoma 15'])

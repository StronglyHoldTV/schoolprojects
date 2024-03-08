import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
c = tk.Canvas(width = 500, height = 500)
c.pack()
l = []


class Item():
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

def getList():
    with open('sklad.txt', 'r') as file:
        l = []
        for line in file:
            if(line.strip()==''):
                continue
            properties = line.strip().split(' ')
            l.append(Item(properties[0], float(properties[2]), int(properties[1])))
        return l

amount_entry = tk.Entry()
name_entry = tk.Entry()


amount_label = tk.Label(text="Amount:")
amount_label.place(x=50, y=90)

    
amount_entry.place(x=50, y=106)

name_label = tk.Label(text="Name of product:")
name_label.place(x=50, y=50)

    
name_entry.place(x=50, y=66)


def update():
    c.delete("all")
    
    for no, i in enumerate(l):
        c.create_text(250, 50+no*20, text=f'{i.name} {i.count}x = {i.price}$',anchor=tk.W)
    c.create_text(250, 50+len(l)*20, text=f'SUM {sum(item.price for item in l)}$',anchor=tk.W)
    for no, i in enumerate(getList()):
        c.create_text(100, 250+no*20, text=f'{i.name}  =  {i.count}x, {i.price}$',anchor=tk.W)
        


    c.create_polygon(377,420, 450,420, 430,450, 397,450, fill="yellow", outline="")
    c.update()


update()

"""
Sell - pozaduje nazov itemu a pocet, ktory chceme predat,
preda iba ak je pocet na sklade vacsi alebo rovny pozadovanemu mnozstvu,
vrati cenu, za ktoru predal produkty, inak vrati 0
"""

def sell(name, count = 1):
    with open('sklad.txt', 'r+') as file:
        toDelete = -1
        soldFor = 0
        for no, line in enumerate(file):
            if line.lower().startswith(name):
                toDelete = no
                item = line.split(' ')
                if int(item[1]) < count:
                    return 0
                if(int(item[1])-count) != 0:
                    file.write("\n" + item[0] + " " + str(int(item[1])-count) + " " + item[2])
                soldFor = count * float(item[2])
        file.seek(0)
        lines = file.readlines()
        file.seek(0)
        lines.pop(toDelete)
        file.truncate()
        file.writelines(lines)
        return round(soldFor, 2)
    return 0




def n():
    name = name_entry.get()
    amount = int(amount_entry.get())
    price = sell(name ,amount)
    l.append(Item(name, price, amount))
    update()

def printR():
    global l
    with open('rec.txt', 'w') as file:
        for i in l:
            print(f" {i.name}  =  {i.count}x, ${i.price}",file=file)
        print(sum(item.price for item in l))

    l = []
    update()
            
                  

    
b=tk.Button(text = 'add to cart', command=n)
b.place(x=50, y=150)

b2=tk.Button(text = 'print receipt', command=printR)
b2.place(x=50, y=200)
            


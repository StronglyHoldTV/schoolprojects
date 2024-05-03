import tkinter as tk
import random
import threading
import time
c = tk.Canvas(width = 500, height = 500)
c.pack(expand='yes')


class Card:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.color = 'limegreen'
        self.solved = False
        self.clicked = 0
    def draw(self, color=None):
        if(color == None):
            color = self.color
        c.create_rectangle(self.x, self.y, self.x+50, self.y+50, fill=color)
        c.create_text(self.x+25, self.y+25, text = self.number, font = 'Arial 25')
    def check(self, x, y, delitel):
        if(x > self.x and self.x > x-50 and y > self.y and self.y > y-50):
            if(self.number%delitel==0):
                self.color = 'peru'
                self.solved = True
            else:
                self.color = 'tomato'
            self.draw()
            self.clicked = time.time()
    def checkTime(self):
        if self.clicked+5 < time.time() and not self.solved and self.color=='tomato':
            self.color = 'limegreen'
            print(self.number)
        return

d = random.randint(2,9)
m, n= random.randint(3,5), random.randint(3,10)
print(m, n)

c.create_text(250, 35, text = 'Hladaj nasobky cisla:', anchor='e')
c.create_rectangle(260, 10, 260+50, 60, fill='peru')
c.create_text(260+25, 60-25, text=d, anchor='c', font='Arial 25')

doska = []

for x, _ in enumerate(range(0, n)):
    for y, _ in enumerate(range(0, m)):
        doska.append(Card(random.randint(1, 50), 10+x*60, 70+y*60))


for card in doska:
    card.draw()

def check(e):
    for i in doska:
        i.check(e.x, e.y, d)

c.bind('<Button-1>', check)

def b(e):
    vsetky = True
    for i in doska:
        if i.number % 5 == 0 and not i.solved:
            vsetky = False
        i.checkTime()
        i.draw()
    if vsetky == True:
        c.create_text(260+50, 60, text='Nájdené všetky násobky')
    return

c.bind('<Motion>', b)


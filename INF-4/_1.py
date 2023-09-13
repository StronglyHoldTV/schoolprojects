import tkinter as tk
import random

c = tk.Canvas(width = 320, height = 320)

c.pack()



def kresli(text):
    x = random.randint(0, 300)
    y = random.randint(0, 310)
    c.create_text(x, y, text = text, anchor = tk.W)

def stars(amount: int) -> int:
    print("*"*amount)

def redCircle(x: int, y: int, r: int = 10):
    c.create_oval(x-r, y-r, x+r, y+r, fill="red")

def euraToKoruny(eur: int) -> int:
    return round(eur * 24,2)

def dlzka(l: str) -> int:
    pocet = 0
    for i in l:
        pocet += 1
    return pocet

def isEven(number: int) -> bool:
    return bool(number%2)

def rgb(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"

def randColor() -> str:
    return f"#{random.randrange(0, 256**3):02x}"

def vypisDelitelov(number: int, prt = True) -> bool:
    l = []
    for i in range(1, number+1):
        
        if number % i == 0:
            l.append(i)
    if(len(l) == 2):
        if prt: print("Prvocislo")
        return True
    if prt:
        for j in l:
            print(j, end=" ")
        print()
    return False

def primesInInterval(fr: int, to: int):
    print("Prvocisla: ", end = "") 
    for i in range(fr, to):
        if not vypisDelitelov(i, False):
            continue
        print(i, end=" ")
    print()

primesInInterval(0, 120)

print(randColor())
print(isEven(3))
print(isEven(2))
print(dlzka("xyz"))

kresli("test")
kresli("abcd")

for i in range(1, 11):
    stars(i)
    
for x in range(10, 340, 30):
    c.update()
    c.after(10)
    for y in range(0, 300, 15):
        c.update()
        c.after(10)
        redCircle(x,y, 20)
del redCircle



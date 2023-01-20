
import tkinter
from random import*
canvas = tkinter.Canvas(width=600, height=600, bg='white') 
canvas.pack()


canvas.create_rectangle(0,200,600,400,fill="grey")
canvas.create_rectangle(0,0,600,200,fill="light blue")
canvas.create_rectangle(0,400,600,600,fill="light green")

#cesta
x=0
y=300
for i in range(20):
    canvas.create_line(x,y,x+10,y,fill="white")
    x=x+30

#sneh
for i in range (100):
    v=randint(5,15)
    x=randint(0,600)
    y=randint(0,180)
    canvas.create_oval(x,y,x+v,y+v,fill="white")
#tráva
x=0
for i in range(600):
    v=randint(20,150)
    canvas.create_line(x,600,x,600-v,fill="green")
    x=x+1
#vrany
for i in range(30):
    v=randint(5,15)
    x=randint(0,600)
    y=randint(0,200)
    canvas.create_line(x,y,x-2*v,y-2*v,fill="black")
    canvas.create_line(x,y,x+2*v,y-2*v,fill="black")

#auto
x=0
y=225
x_speed=5
x2=0
x2_speed=10
def animacia_auto():
    global x,y
    canvas.delete("auto")
    canvas.create_rectangle(x,y,x+50,y+25,fill="red",tag="auto")
    canvas.create_rectangle(x2,y,x2+50,y+25,fill="yellow",tag="auto")
    x=x+x_speed
    x2=x2+x2_speed

    
    if x==650:
        x=0
        
    canvas.after(10,animacia_auto)
animacia_auto()

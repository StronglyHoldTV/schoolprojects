import tkinter as tk
import random
import math

circleList = []
c = tk.Canvas(width = 500, height = 500)
c.pack()

class Circle:
    def __init__(self, x, y, size, direction, speed):
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.speed = speed
    def doStep(self):
        m = 1
        #if(math.radians(180) < self.direction):
        #    m = -1
        self.x = self.x + math.sin(self.direction)*self.speed*m
        self.y = self.y + math.cos(self.direction)*self.speed*m
        if (self.y + self.size) >= 500:
            self.direction = math.radians(180) - self.direction
        if (self.x + self.size) >= 500:
            self.direction = math.radians(360) - self.direction
        if (self.x < 0):
            self.direction = math.radians(360) - self.direction
        if (self.y < 0):
            self.direction = math.radians(180) - self.direction
        
    def drawCircle(self):
        c.create_oval(self.x, self.y, self.x+self.size, self.y+self.size, fill="skyblue")

for i in range(0, 20):
    s = random.randint(25,75)
    circle = Circle(x = random.randint(0,500 - s), y = random.randint(0,500 - s), size = s, direction = math.radians(random.randint(0,360)), speed = random.randint(2,15))
    circleList.append(circle)


while True:
    for circle in circleList:
        circle.drawCircle()
        circle.doStep()
    #print(circleList)
    c.update()
    c.after(50)
    
    c.delete("all")

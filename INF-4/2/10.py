import random

retazec = input("Zadaj retazec")
whattodo = input("Shuffle/Order")
whattodo = whattodo.lower()

a = [*retazec]

if(whattodo == "0" or whattodo == "s" or whattodo == "shuffle"):
    random.shuffle(a)
    print("".join(a))
if(whattodo == "1" or whattodo == "o" or whattodo == "order"):
    x = ""
    y = ""
    for i, c in enumerate(a):
        if(i % 2 == 0):
            x += c
        else:
            y += c
    print(x)
    print(y)
            
    


import math

mn = int(input("zadaj krok od: "))
mx = int(input("zadaj krok do: "))
step = int(input("zadaj krok: "))

for i in range(mn, mx+1, step):
    
    a = math.radians(i)
    print(f"{i:3} {a:1:4}")

import random

l = []

for i in range(0,12):
    l.append(random.randint(-5, 6))

z = []
o = []
k = []

for i in l:
    if i > 0:
        k.append(i)
    if i == 0:
        o.append(i)
    if i < 0:
        z.append(i)
print(z+o+k)
    

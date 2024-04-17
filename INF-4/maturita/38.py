import random

l = []

for i in range(0,50):
    l.append(random.randint(-35, 35))

z = []
k = []
n = []

for i in l:
    if i < 0:
        z.append(i)
    if i == 0:
        n.append(i)
    if i > 0:
        k.append(i)

print(z+n+k)

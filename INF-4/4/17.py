import random

n = int(input('pocet hodov'))

l = []

for i in range(0, n):
    l.append(random.randint(1,6))

p = []
for i in range(1, 7):
    p.append(l.count(i))

for i in range(1, 7):
    print(i, p[i-1])

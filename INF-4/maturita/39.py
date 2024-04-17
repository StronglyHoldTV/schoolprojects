import random

n = int(input('zadaj n'))

l = [random.randint(1,6) for i in range(0, n)]

n = [l.count(i) for i in range(1, 7)]
print(n)
    

import random
l = []
for _ in range(21):
    l.append(random.randint(0,50))

l.sort()
print(l)

def bin(n, l):
    while len(l)!=1:
        ln = len(l)//2
        a = l[:ln]
        b = l[ln:]
        print(a)
        print(b)
        print(l[ln])
        if l[ln]>n:
            l = a
        else:
            l = b
        print(l)
    return l[0] == n


import random

n = 12
l = []

for i in range(n):
    l.append(random.randint(0,21))
    
def sortList(o):
    k = o
    for i in range(0, len(k)):
        for j in range(i+1, len(k)):
            if(k[i] >= k[j]):
                k[i], k[j] = k[j], k[i]
    return o
    

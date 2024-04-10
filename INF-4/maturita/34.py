import random
l = []
for _ in range(21):
    l.append(random.randint(0,50))
print(l)

def sortList(o):
    k = o
    for i in range(0, len(k)):
        for j in range(i+1, len(k)):
            if(k[i] >= k[j]):
                k[i], k[j] = k[j], k[i]
    return o

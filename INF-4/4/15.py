import random

l = []
for i in range(0,12):
    l.append(random.randint(15,35))
a = sum(l)/len(l)

print('nadpriemerne dni', len([n for n in l if n>a]))
print('podpriemerne dni', len([n for n in l if n<a]))
print(min(l), 'minimalna teplota, v', l.index(min(l))+1, 'den')
print(max(l), 'maximalna teplota, v', l.index(max(l))+1, 'den')

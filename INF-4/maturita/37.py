import random

l = []

for i in range(0, 10):
    l.append(random.randint(20, 35))

average = sum(l)/len(l)
print('priemer', average)

vyssie = len([i for i in l if average < i])
print('vyssia v', vyssie)

minimum = min(l)
maximum = max(l)

minat = [no for no, i in enumerate(l) if i == minimum]
maxat = [no for no, i in enumerate(l) if i == maximum]



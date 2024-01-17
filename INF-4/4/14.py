l = []
p = input('Zadaj priezvisko')
while p:
    l.append(p)
    p = input('Zadaj priezvisko')
l.sort()
print(l)
m = input('Vymaz priezvisko')
for i in range(0, l.count(m)):
    l.remove(m)
print(l)

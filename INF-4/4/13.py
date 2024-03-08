l = []
p = input('Zadaj priezvisko')
while p:
    l.append(p)
    p = input('Zadaj priezvisko')
l.sort()
print(l)
m = input('Zadaj dalsie priezvisko')
for i in l:
    if m == min(m, i):
        l.insert(l.index(i), m)
        break
print(l)

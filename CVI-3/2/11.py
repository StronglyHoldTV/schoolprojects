n = int(input('zadaj pocet: '))
s = 4
for i in range(0, n-1):
    #print(f'{(-1 if i%2 else 1)}, 4/{(3+2*i)}')
    s += ((1 if i%2 else -1) * (4/(3+2*i)))

print(s)

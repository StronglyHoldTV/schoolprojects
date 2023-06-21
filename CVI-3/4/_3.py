n = int(input('zadaj n: '))
p = 0
print('Delitele: ', end = '')
for i in range(1, n+1):
    if(n % i == 0):
        p += 1
        print(i, end = ' ')
    #if (p < 2):
    #    break
print()
print(f'pocet delitelov = {p}')

if(p == 2): print('AAAAAAA je to prvocislo. !JEJ!')


p = 0
a = 0
print('Delitele: ', end = '')
while a < n:
    a += 1
    if(n % a == 0):
        p += 1
        print(a, end = ' ')
    #if (p < 2):
    #    break
print()
print(f'pocet delitelov = {p}')
